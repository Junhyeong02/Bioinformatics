# 주석으로 분리된 블럭 단위로 R shell에서 실행

##############################################################################################################

# 초기 설정

workingDir = "WORKING_DIRTORY"
inputFile = "INPUT_FILE"
TOMFileBase = "PREFIX"
blockSize = 40000

##############################################################################################################

setwd(workingDir)
getwd()

##############################################################################################################

# 라이브러리 import 
library(WGCNA)
options(stringsAsFactors = FALSE);
options(scipen = 100000);

##############################################################################################################

expData <- read.table(inputFile, header = TRUE);
datExpr0 = as.data.frame(t(expData[,-1]));
names(datExpr0) = expData$GeneID;
rownames(datExpr0) = names(expData)[-1];

##############################################################################################################

# data preprocessing

gsg = goodSamplesGenes(datExpr0, verbose = 3);
gsg$allOK
if (!gsg$allOK)
{
	# Optionally, print the gene and sample names that were removed:
	if (sum(!gsg$goodGenes)>0)
	printFlush(paste("Removing genes:", paste(names(datExpr0)[!gsg$goodGenes], collapse = ", ")));

	if (sum(!gsg$goodSamples)>0)
	printFlush(paste("Removing samples:", paste(rownames(datExpr0)[!gsg$goodSamples], collapse = ", ")));

	# Remove the offending genes and samples from the data:
	datExpr0 = datExpr0[gsg$goodSamples, gsg$goodGenes]
}

##############################################################################################################

# 샘플 간 거리 계산
sampleTree  = hclust(dist(datExpr0), method  =  "average");

##############################################################################################################


sizeGrWindow(12,9)
par(cex = 0.6);
par(mar = c(0,4,2,0))
plot(sampleTree, main = "Sample clustering to detect outliers", 
sub="", xlab="", cex.lab = 1.5, cex.axis = 1.5, cex.main = 2)
###############################################################################################################

# 위 코드 실행으로 아웃라이어를 탐지, 많이 차이 나는 샘플을 제거
sampleHeightCut = 10000#
###############################################################################################################

abline(h = sampleHeightCut, col = "red");
clust = cutreeStatic(sampleTree, cutHeight = sampleHeightCut, minSize = 10)
##################################################################################################################

keepSamples = (clust==1)
datExpr = datExpr0[keepSamples, ]
nGenes = ncol(datExpr)
nSamples = nrow(datExpr)
##################################################################################################################

pdf(file = "Sample_clustering_to_detect_outliers.pdf", width = 12, height = 9);
par(cex = 0.6);
par(mar = c(0,4,2,0));
plot(sampleTree, main = "Sample clustering to detect outliers", 
sub="", xlab="", cex.lab = 1.5, cex.axis = 1.5, cex.main = 2);
abline(h = sampleHeightCut, col = "red");
dev.off();
##################################################################################################################

powers = c(c(1:10), seq(from = 12, to=20, by=2));
sft = pickSoftThreshold(datExpr, powerVector = powers, verbose = 5);

##################################################################################################################

sizeGrWindow(9, 5);
par(mfrow = c(1,2));
cex1 = 0.9;
plot(sft$fitIndices[,1], -sign(sft$fitIndices[,3])*sft$fitIndices[,2], 
xlab="Soft Threshold (power)", ylab="Scale Free Topology Model Fit,signed R^2",
type="n", main = paste("Scale independence"));
text(sft$fitIndices[,1], -sign(sft$fitIndices[,3])*sft$fitIndices[,2], 
labels=powers,cex=cex1,col="red");
abline(h=0.90,col="red");
plot(sft$fitIndices[,1], sft$fitIndices[,5], 
xlab="Soft Threshold (power)", ylab="Mean Connectivity", 
type="n", main = paste("Mean connectivity"));
text(sft$fitIndices[,1], sft$fitIndices[,5], 
labels=powers, cex=cex1,col="red");

##################################################################################################################

pdf(file = "Soft_Threshold.pdf", width = 9, height = 5);
par(mfrow = c(1,2));
cex1 = 0.9;
plot(sft$fitIndices[,1], -sign(sft$fitIndices[,3])*sft$fitIndices[,2], 
xlab="Soft Threshold (power)", ylab="Scale Free Topology Model Fit,signed R^2",
type="n", main = paste("Scale independence"));
text(sft$fitIndices[,1], -sign(sft$fitIndices[,3])*sft$fitIndices[,2], labels=powers,cex=cex1,col="red");
abline(h=0.90,col="red");
plot(sft$fitIndices[,1], sft$fitIndices[,5], 
xlab="Soft Threshold (power)",ylab="Mean Connectivity", 
type="n", main = paste("Mean connectivity"));
text(sft$fitIndices[,1], sft$fitIndices[,5], labels=powers, cex=cex1,col="red");
dev.off();

##################################################################################################################

# 파워값 수정 
powerBeta  = 8 #

##################################################################################################################

net = blockwiseModules(datExpr, power = powerBeta,
TOMType = "unsigned", minModuleSize = 30,
reassignThreshold = 0, mergeCutHeight = 0.25,
numericLabels = TRUE, pamRespectsDendro = FALSE,
saveTOMs = TRUE,
saveTOMFileBase = TOMFileBase, maxBlockSize = blockSize,
verbose = 3)

##################################################################################################################

sizeGrWindow(12, 9)
mergedColors = labels2colors(net$colors)
plotDendroAndColors(net$dendrograms[[1]], mergedColors[net$blockGenes[[1]]], "Module colors", dendroLabels = FALSE, hang = 0.03, addGuide = TRUE, guideHang = 0.05)
moduleLabels = net$colors
moduleColors = labels2colors(net$colors)
MEs = net$MEs;
geneTree = net$dendrograms[[1]];
save(MEs, moduleLabels, moduleColors, geneTree, datExpr, file = paste(TOMFileBase, "RData", sep = ""))

##################################################################################################################

pdf(file = "dendrograms.pdf", width = 12, height = 9);
# mergedColors = labels2colors(net$colors)
plotDendroAndColors(net$dendrograms[[1]], mergedColors[net$blockGenes[[1]]], "Module colors", dendroLabels = FALSE, hang = 0.03, addGuide = TRUE, guideHang = 0.05)
dev.off()

##################################################################################################################

MEs = moduleEigengenes(datExpr, moduleColors)$eigengenes
MET = orderMEs(MEs)

##################################################################################################################
pdf(file = "Eigengene_dendrograms.pdf", width = 6, height = 6);
sizeGrWindow(6, 6);
par(cex = 1.0)
plotEigengeneNetworks(MET, "Eigengene dendrogram", marDendro = c(0,4,1,2), plotHeatmaps = FALSE)
dev.off()

##################################################################################################################

pdf(file = "Eigengene_adjacency_heatmap.pdf", width = 6, height = 6);
par(cex = 1.0)
plotEigengeneNetworks(MET, "Eigengene adjacency heatmap", marHeatmap = c(3,4,2,2),
plotDendrograms = FALSE, xLabelsAngle = 90)
dev.off()

##################################################################################################################

# 실행 결과 저장
write.table(MEs, file = "MEs.txt", sep = '\t', quote = FALSE);
write.table(net$colors, file = "ID_colors.txt", sep = '\t', quote= FALSE, col.names = FALSE);
write.table(moduleColors, file = "moduleColors.txt", sep = "\t", quote= FALSE, col.names = FALSE);

##################################################################################################################

# 그래프를 위한 table 저장
TOM = TOMsimilarityFromExpr(datExpr, power = powerBeta);
probes = names(datExpr) 
dimnames(TOM) = list(probes, probes)
cyt = exportNetworkToCytoscape(TOM, edgeFile = "CytoscapeInput-edges.txt", nodeFile = "CytoscapeInput-nodes.txt", weighted = TRUE, threshold = 0.8, nodeNames = probes, nodeAttr = moduleColors);

#################################################################################################################

# 원하는 모듈의 node, edge data 저장
x = load(paste0(TOMFileBase, ".RData"))
TOM = TOMsimilarityFromExpr(datExpr, power = powerBeta); # Read in the annotation file 
modules = c("purple", "blue"); # array에 원하는 module 색깔을 선택 
probes = names(datExpr) 
inModule = is.finite(match(moduleColors, modules)); 
modProbes = probes[inModule]; 
modTOM = TOM[inModule, inModule];
dimnames(modTOM) = list(modProbes, modProbes) 
cyt = exportNetworkToCytoscape(modTOM, edgeFile = paste("CytoscapeInput-edges-", paste(modules, collapse="-"), ".txt", sep=""), nodeFile = paste("CytoscapeInput-nodes-", paste(modules, collapse="-"), ".txt", sep=""), weighted = TRUE, threshold = 0.02, nodeNames = modProbes, nodeAttr = moduleColors[inModule]);

