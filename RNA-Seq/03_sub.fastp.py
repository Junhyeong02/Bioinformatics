import sys
import os
import subprocess
from glob import glob

input_path = sys.argv[1]       ######## ../00.Raw_data/PE/PcPi/\*.fastq.gz
output_path = sys.argv[2]      ######## ../01.Preprocessed_data/PE/ECW.PL/
qcut = sys.argv[3]
CPU = sys.argv[4]
cut_ratio = float(sys.argv[5]) #######
pair_type = sys.argv[6]

print(input_path)
sample_list = sorted(list(glob(input_path)))
print(sample_list)

assert os.path.isdir(output_path)
assert pair_type == "SE" or pair_type == "PE"

process = list()
commonprefix = list()

for cnt, sample in enumerate(sample_list):
    while len(process) >= 6:
        for i, proc in enumerate(process):
            if not proc.poll() is None:
                process.pop(i)
                break

    assert os.path.isfile(sample)

    out_file = os.path.join(output_path, os.path.basename(sample).replace(".fastq.", ".filter.fastq."))
    html_file = out_file.replace(os.path.splitext(out_file)[1], ".html")
    json_file = out_file.replace(os.path.splitext(out_file)[1], ".json")

    # len_cut = cut_ratio 
    len_cut = int(int(subprocess.check_output("gunzip -c {} |head -n 2 |tail -n 1 | wc -L".format(sample), shell = True))*cut_ratio)
    readqual = str(subprocess.check_output("gunzip -c {} |head -n 1000 | sed -n '4~4p' |tr -d '\\n'".format(sample), shell = True), "utf-8")
    phred = "" if (max(ord(c) for c in readqual)-33) <= 41 else "-6"
    
    ### Single end
    if pair_type == "SE":
        assert os.path.abspath(out_file) != os.path.abspath(sample)
        
        commonprefix.append(sample)
        commend = "fastp -i {} -o {} -l {} -q {} -w {} -h {} -j {} {}".format(sample, out_file, len_cut, qcut, CPU, html_file, json_file, phred)

    ### Paired end
    elif pair_type == "PE":
        if cnt % 2 == 1:
            continue
      
        file1 = sample
        file2 = sample_list[cnt+1]
        out_file1 = out_file
        out_file2 = os.path.join(output_path, os.path.basename(file2).replace(".fastq.", ".filter.fastq."))
        assert os.path.abspath(out_file1) != os.path.abspath(file1)
        assert os.path.abspath(out_file2) != os.path.abspath(file2)
        
        commonprefix.append(os.path.commonprefix([file1, file2]))
        commend = "fastp -i {} -I {} -o {} -O {} -l {} -c --detect_adapter_for_pe -q {} -w {} -h {} -j {} {}".format(file1, file2, out_file1, out_file2, int(len_cut), qcut, CPU, html_file, json_file, phred)
    
    p = subprocess.Popen(commend, shell = True)
    # p = subprocess.Popen('echo "{}"'.format(commend), shell = True)
    process.append(p)

while len(process) != 0:
    for i, proc in enumerate(process):
        if not proc.poll() is None:
            process.pop(i)
            break

for s in commonprefix:
    print(s)
