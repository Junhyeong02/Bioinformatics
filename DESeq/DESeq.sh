PREPROCESSED="/var2/Work/Myung-Shin/RNA_Seq/01.Preprocessed_data"
GENOMEDATA="/var2/Work/Myung-Shin/RNA_Seq/02.Genome_data"
MAPPING="/var2/Work/Myung-Shin/RNA_Seq/04.Mapping"
FPKMTPM="/var2/Work/Myung-Shin/RNA-Seq/05.FPKM_TPM"
DESEQ="/var2/Work/Myung-Shin/RNA_Seq/07.DESeq"

############################################################

TARGET="Infestans.T30-4"
GTF="GCF_000142945.1_ASM14294v1_genomic.MS.gtf"
RESULT="infesT30-4_CAPS_DEG.txt"

# python3 07_sub.SampleInfo.py $MAPPING/$TARGET/ $DESEQ/$TARGET/ $GENOMEDATA/$GTF $PREPROCESSED/PE/Infestans/

# VALUE=148

# DIR=`pwd`
# cd $DESEQ/$TARGET/
# prepDE.py3 -i sample_lst.txt -l $VALUE
# cd $DIR

# Rscript DESeq.R $DESEQ/$TARGET/ ACN CAPS $DESEQ/$TARGET/$RESUL

# python volcano.py $DESEQ/Infestans/infes_CAPS_DEG.txt $DESEQ/temp.png "TITLE"
# python heatmap.py $DESEQ/sample.txt $DESEQ/heatmap.png "TITLE.heatmap"
python heatmap.ortho.py $DESEQ/Capsici/capsici_CAPS_DEG.txt $DESEQ/Infestans/infes_CAPS_DEG.txt $DESEQ/Prof.HA_Lee/PinfPcaps.tsv Pcap Pinf $FPKMTPM/Capsici/Capsici.TPM.txt $FPKMTPM/Infestans/Infestans.TPM.txt "P-cap-CAPS" "P-infes-CAPS" heatmap.png "TITLE.heatmap"
