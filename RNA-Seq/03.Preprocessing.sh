###	Note: you must run this script after "conda activate MS3.4" to use fastp

# usage : python3 03_sub.fastp.py [glob files] [out file dir] [qcut] [total cpu] [length cutoff] [pair type]
INPUTPATH=""
OUTPUTPATH=""
QCUT=0
CPU=1
CUTRATIO=0.7
PAIRTYPE="PE"

python3 03_sub.fastp.py $INPUT_PATH $OUTPUTPATH $QCUT $CPU $CUTRATIO $PAIRTYPE
# python3 03_sub.fastp.py ../00.Raw_data/PE/PcPi/\*.fastq.gz ../01.Preprocessed_data/PE/PcPi_30_71/ 30 3 71 PE