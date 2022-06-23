# 2022.1.11
# conda activate KJH3.9.5

######################################

RAWDATA=""
PREPROCESSING=""
GENOMEDATA=""
GENOMEINDEX=""
MAPPING=""
FPKM_TPM=""

Qvalue=20
LenCut="0.7"

######################################

RNASEQ () {
    
TARGET=$1
PAIRTYPE=$2
INDEX=$3
GTF=$4

### Fastp
python3 03_sub.fastp.py ${RAWDATA}/${PAIRTYPE}/${TARGET}/\*.fastq.gz ${PREPROCESSING}/${PAIRTYPE}/${TARGET}/ $Qvalue 3 $LenCut ${PAIRTYPE}
# echo python3 03_sub.fastp.py $RAWDATA/PE/$TARGET/\*.fastq.gz $PREPROCESSING/PE/$TARGET/ 20 3 0.7 PE

### Hisat2
python3 04_sub.Hisat2.py ${GENOMEINDEX}/${INDEX} ${PREPROCESSING}/${PAIRTYPE}/${TARGET}/\*.filter.fastq.gz ${MAPPING}/${TARGET}/ 20 ${PAIRTYPE}
# echo python3 04_sub.Hisat2.py $GENOMEINDEX/$INDEX $PREPROCESSING/PE/$TARGET/\*.filter.fastq.gz $MAPPING/$TARGET/ 20 PE

### Stringtie
# echo python3 05_sub.stringtie.py $GENOMEDATA/$GTF $MAPPING/$TARGET/ 3 $PREFIX
python3 05_sub.stringtie.py ${GENOMEDATA}/${GTF} ${MAPPING}/${TARGET}/ 3 "ERROR"

sleep 1m
### FPKM_TPM
# echo python3 06_sub.FPKM_TPM.py $MAPPING/$TARGET/ $FPKM_TPM/$TARGET/$TARGET

python3 06_sub.FPKM_TPM.py ${MAPPING}/${TARGET}/ ${FPKM_TPM}/${TARGET}/${TARGET}

echo $TARGET

}

RNASEQ "target" "pairtype" "index" "gtf"

# ex) RNASEQ "CM334.tissue" "SE" "Annuum.v1.6.Total" "CaCM334.MYB.ReAnnot.chromosome.sort.gtf"
