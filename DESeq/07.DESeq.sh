# python3 07_sub.SampleInfo.py ../04.Mapping/Infestans/ ../07.DESeq/Infestans/ /var2/Work/Myung-Shin/RNA_Seq/02.Genome_data/GCA_012552325.1_ASM1255232v1_genomic.MS.gtf ../01.Preprocessed_data/PE/Infestans/

# python3 07_sub.SampleInfo.py ../04.Mapping/Capsici/ ../07.DESeq/Capsici/ /var2/Work/Myung-Shin/RNA_Seq/02.Genome_data/GCA_016618375.1_Pcap_4.1_genomic.MS.gtf ../01.Preprocessed_data/PE/Capsici/

:<<end
DIR=`pwd`
cd ../07.DESeq/Infestans/
pwd
prepDE.py3 -i sample_lst.txt -l 148
cd $DIR
pwd
end

# Rscript DESeq.R ../07.DESeq/Infestans/ ACN CAPS infes_CAPS_DEG.txt

:<<end
DIR=`pwd`
cd ../07.DESeq/Capsici/
pwd
prepDE.py3 -i sample_lst.txt -l 146
cd $DIR
pwd
end

# Rscript DESeq.R ../07.DESeq/Capsici/ ACN CAPS capsici_CAPS_DEG.txt


# python 07_sub.DESeq.format.py ../07.DESeq/CM334.Pi/ 
# python 07_sub.KEGG.pathway.py ../02.Genome_data/KO_Assign/CaCM334.MYB.ReAnnot.chromosome.KO.tsv 1e-6 ../07.DESeq/CM334.Pc/CaCM334.MYB.ReAnnot.chromosome 
# python 07_sub.TogoWS.py /var2/Work/Myung-Shin/RNA_Seq/07.DESeq/CaCM334.MYB.ReAnnot.chromosome.TERM2GENE.txt ../07.DESeq/Capsicum.kegg /var2/Work/Myung-Shin/RNA_Seq/07.DESeq/capsicum_kegg_path.txt

# Rscript KEGG_enrichment.R ../07.DESeq/Capsicum.PATH2GENE.txt ../07.DESeq/CM334.Pc/P.capsici_12h_DEG.txt ../07.DESeq/Capsicum.kegg.MAPdiscription.txt ../07.DESeq/CM334.Pc/P.capsici.12h &
# Rscript KEGG_enrichment.R ../07.DESeq/Capsicum.PATH2GENE.txt ../07.DESeq/CM334.Pc/P.capsici_6h_DEG.txt ../07.DESeq/Capsicum.kegg.MAPdiscription.txt ../07.DESeq/CM334.Pc/P.capsici.6h &
# Rscript KEGG_enrichment.R ../07.DESeq/Capsicum.PATH2GENE.txt ../07.DESeq/CM334.Pc/P.capsici_1D_DEG.txt ../07.DESeq/Capsicum.kegg.MAPdiscription.txt ../07.DESeq/CM334.Pc/P.capsici.1D &
# Rscript KEGG_enrichment.R ../07.DESeq/Capsicum.PATH2GENE.txt ../07.DESeq/CM334.Pc/P.capsici_1h_DEG.txt ../07.DESeq/Capsicum.kegg.MAPdiscription.txt ../07.DESeq/CM334.Pc/P.capsici.1h &
# Rscript KEGG_enrichment.R ../07.DESeq/Capsicum.PATH2GENE.txt ../07.DESeq/CM334.Pc/P.capsici_2h_DEG.txt ../07.DESeq/Capsicum.kegg.MAPdiscription.txt ../07.DESeq/CM334.Pc/P.capsici.2h &
# Rscript KEGG_enrichment.R ../07.DESeq/Capsicum.PATH2GENE.txt ../07.DESeq/CM334.Pc/P.capsici_4h_DEG.txt ../07.DESeq/Capsicum.kegg.MAPdiscription.txt ../07.DESeq/CM334.Pc/P.capsici.4h 

# Rscript KEGG_enrichment.R ../07.DESeq/Capsicum.PATH2GENE.txt ../07.DESeq/CM334.Pi/P.infestans_12h_DEG.format.txt ../07.DESeq/Capsicum.kegg.MAPdiscription.txt ../07.DESeq/CM334.Pi/P.infestans.12h &
# Rscript KEGG_enrichment.R ../07.DESeq/Capsicum.PATH2GENE.txt ../07.DESeq/CM334.Pi/P.infestans_6h_DEG.format.txt ../07.DESeq/Capsicum.kegg.MAPdiscription.txt ../07.DESeq/CM334.Pi/P.infestans.6h &
# Rscript KEGG_enrichment.R ../07.DESeq/Capsicum.PATH2GENE.txt ../07.DESeq/CM334.Pi/P.infestans_1D_DEG.format.txt ../07.DESeq/Capsicum.kegg.MAPdiscription.txt ../07.DESeq/CM334.Pi/P.infestans.1D &
# Rscript KEGG_enrichment.R ../07.DESeq/Capsicum.PATH2GENE.txt ../07.DESeq/CM334.Pi/P.infestans_2D_DEG.format.txt ../07.DESeq/Capsicum.kegg.MAPdiscription.txt ../07.DESeq/CM334.Pi/P.infestans.2D &
# Rscript KEGG_enrichment.R ../07.DESeq/Capsicum.PATH2GENE.txt ../07.DESeq/CM334.Pi/P.infestans_3.5D_DEG.format.txt ../07.DESeq/Capsicum.kegg.MAPdiscription.txt ../07.DESeq/CM334.Pi/P.infestans.3.5D &
# Rscript KEGG_enrichment.R ../07.DESeq/Capsicum.PATH2GENE.txt ../07.DESeq/CM334.Pi/P.infestans_5D_DEG.format.txt ../07.DESeq/Capsicum.kegg.MAPdiscription.txt ../07.DESeq/CM334.Pi/P.infestans.5D 

# TARGET="Infestans.T30-4"

# python3 07_sub.SampleInfo.py ../04.Mapping/$TARGET/ ../07.DESeq/$TARGET/ /var2/Work/Myung-Shin/RNA_Seq/02.Genome_data/GCA_016618375.1_Pcap_4.1_genomic.MS.gtf ../01.Preprocessed_data/PE/Capsici/


python 07_sub.KOnumber.py ../02.Genome_data/KO_Assign/CaCM334.MYB.ReAnnot.chromosome.KO.tsv 1e-10 ../07.DESeq/CaCM334.
