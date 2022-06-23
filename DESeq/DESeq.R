args <- commandArgs(trailingOnly = TRUE)

workingdir = args[1]
reftarget = args[2]
target = args[3]
out = args[4]

setwd(workingdir)
getwd()

TargetCol = c(paste(reftarget, "_1", sep = ""), paste(reftarget, "_2", sep = ""), paste(reftarget, "_3", sep = ""), paste(target, "_1", sep = ""), paste(target, "_2", sep = ""), paste(target, "_3", sep = ""))

TargetCol

AllcountData = read.csv("gene_count_matrix.csv", row.names="gene_id", head= TRUE)
colnames(AllcountData)

SubcountData <- subset(AllcountData, select=TargetCol)
countData <- as.matrix(SubcountData)

AllcolData <- read.table("Phenotype.txt", sep="\t", head=TRUE, row.names=1)
colData <- subset(AllcolData, Type == reftarget | Type == target)

all(rownames(colData) %in% colnames(countData))

if(all(rownames(colData) != colnames(countData)))
{
	countData <- countData[, rownames(colData)]
}
library(DESeq2)

colnames(countData)
rownames(colData)

dds <- DESeqDataSetFromMatrix(countData = countData, colData = colData, design = ~ Type)
dds$Type <- relevel(dds$Type, ref = reftarget)
dds <- DESeq(dds)

DGE.results <- results(dds, alpha = 0.05)

summary(DGE.results)

# table(DGE.results$padj < 0.05)
# rownames(subset(DGE.results, padj < 0.05))

write.table(DGE.results, out, quote=FALSE, sep ="\t", row.names=TRUE, col.names=NA)

options(scipen = 100)
hist(DGE.results$padj, breaks = 20, col = "grey" , border = "white" , xlab = "Adjusted p-value" , ylab = "Count" , main = "frequencies of adjusted p-values")

library(NMF)

DGE.results.sorted <- DGE.results[order(DGE.results$padj), ]
DGEgenes <- rownames(subset(DGE.results.sorted, padj < 0.05))

counts.sf_normalized <- counts(dds, normalized = TRUE)
log.norm.counts <- log2(counts.sf_normalized + 1)
hm.mat_DGEgenes <- log.norm.counts[DGEgenes, ]
aheatmap(hm.mat_DGEgenes, Rowv=TRUE, Colv=TRUE , distfun="euclidean", hclustfun="average", scale="row")





