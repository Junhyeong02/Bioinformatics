# KEGG enrichment 코드

library(clusterProfiler)
library(enrichplot)

args <- commandArgs(trailingOnly = TRUE)

term2genepath <- args[1]
deseq2result <- args[2]
term2namepath <- args[3]
prefix <- args[4]

term2gene<-read.table(term2genepath, sep = "\t")
term2name<-read.table(term2namepath, sep = "\t")
d <-read.table(deseq2result, sep = "\t", header = T)

unilist <- d[,1]
deg <- subset(d, padj <= 0.05 & (log2FoldChange >= 1 |  log2FoldChange <= -1) & baseMean > 10)
deglist <- deg[,1]

head(deglist)

geneList = deg[,3]
names(geneList) = as.character(deg[,1])
geneList = sort(geneList, decreasing = TRUE)	###	for GSEA function

x <- enricher(deglist, universe = unilist, TERM2GENE=term2gene, TERM2NAME=term2name)
y <- GSEA(geneList, TERM2GENE=term2gene, TERM2NAME=term2name)

save(x, file = paste0(prefix, ".enricherData.Rdata"))
save(y, file = paste0(prefix, ".GSEAData.Rdata"))

write(x$Description, file = paste0(prefix, ".enricherData.pathway.txt"), sep = "\t", quote = FALSE, col.names = FALSE, row.names = FALSE)
write(y$Description, file = paste0(prefix, ".GSEAData.pathway.txt"), sep = "\t", quote = FALSE, col.names = FALSE, row.names = FALSE)

pdf(file = paste0(prefix, ".enricherBar.pdf"), width = 12, height = 9);
barplot(x, showCategory=20);
dev.off();

Sys.sleep(1)

pdf(file = paste0(prefix, ".mutateBar.pdf"), width = 12, height = 9);
mutate(x, qscore = -log(p.adjust, base=10)) %>% 
    barplot(x="qscore");
dev.off();
Sys.sleep(1)

pdf(file = paste0(prefix, ".enricherDot.pdf"), width = 12, height = 9);
dotplot(x, showCategory=30) + ggtitle("dotplot for ORA");
dev.off();
Sys.sleep(1)

pdf(file = paste0(prefix, ".GSEAdot.pdf"), width = 12, height = 9);
dotplot(y, showCategory=30) + ggtitle("dotplot for GSEA");
dev.off();
Sys.sleep(1)

