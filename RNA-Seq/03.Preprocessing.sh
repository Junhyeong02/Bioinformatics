###	Note: you must run this script after "conda activate MS3.4" to use fastp
# perl 03_sub.Pre.pl ../00.Raw_data/SE/CM334.tissue/ ../01.Preprocessed_data/CM334.tissue/ 18 51 20 SE

# usage python3 03_sub.fastp.py [glob files] [out file dir] [qcut] [total cpu] [length cutoff] [pair type]

# python3 03_sub.fastp.py ../00.Raw_data/PE/Bac.tissue/ ../01.Preprocessed_data/PE/Bac.tissue/ 20 2 0.7 PE

# python3 03_sub.fastp.py /var2/Work/Kong_Junhyeong/00.Raw_data/\*.fastq.gz ../01.Preprocessing/SE/CM334.pericarp/ 20 2 0.7 SE

# python3 03_sub.fastp.py ../00.Raw_data/PE/PcPi/\*.fastq.gz ../01.Preprocessed_data/PE/PcPi/ 20 2 71 PE

# python3 03_sub.fastp.py ../00.Raw_data/PE/PcPi/\*.fastq.gz ../01.Preprocessed_data/PE/PcPi_51/ 20 3 51 PE

python3 03_sub.fastp.py ../00.Raw_data/PE/PcPi/\*.fastq.gz ../01.Preprocessed_data/PE/PcPi_30_71/ 30 3 71 PE
python3 03_sub.fastp.py ../00.Raw_data/PE/PcPi/\*.fastq.gz ../01.Preprocessed_data/PE/PcPi_30_51/ 30 3 51 PE

# python3 03_sub.fastp.py ../00.Raw_data/PE/CM334.NaCl/\*.fastq.gz ../01.Preprocessed_data/PE/CM334.NaCl/ 20 2 0.7 PE
