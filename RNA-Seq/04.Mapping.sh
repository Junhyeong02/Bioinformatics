# usage : python3 04_sub.Hisat2.py [ht prefix] [list of fastq] [output dir] [cpu] [pair_type]

PREFIX=""
INPUT_FASTQ=""
OUTPUTPATH =""
CPU=10
PAIRTYPE="PE"

python3 04_sub.Hisat2.py $PREFIX $INPUT_FASTQ $OUTPUTPATH $CPU $PAIRTYPE
# python3 04_sub.Hisat2.py ../03.Genome_Index/Annuum.v1.6.Total ../01.Preprocessed_data/PE/CM334.NaCl/\*.fastq.gz ../04.Mapping/CM334.NaCl/ 10 PE

