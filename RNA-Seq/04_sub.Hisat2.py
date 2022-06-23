import sys
import os
import subprocess
from glob import glob

path_index = sys.argv[1]   
path_input = sys.argv[2]
path_output = sys.argv[3]
CPU = sys.argv[4]
pairType = sys.argv[5]

# assert os.path.isdir(path_index)
assert os.path.isdir(path_output)
assert pairType == "PE" or pairType == "SE"

input_file_list = sorted(glob(path_input))
print(input_file_list)

for i, input_file in enumerate(input_file_list):
    print(input_file)
    assert os.path.isfile(input_file)
    out_file_name = os.path.basename(input_file).replace(".filter.fastq.gz", "").split("_")[0]
    out_file_name = os.path.join(path_output, out_file_name)

    assert os.path.abspath(out_file_name) != os.path.abspath(input_file)

    if pairType == "SE":
        
        commend = "hisat2 -p {} --dta -x {} --rna-strandness R --summary-file {}.log -U {} -S {}.sam".format(CPU, path_index, out_file_name, input_file, out_file_name)
        
    elif pairType == "PE":
        if i % 2 == 0:
            try:
                input_file1 = input_file
                input_file2 = input_file_list[i+1]
            except IndexError:
                print("No paired file exist")
                break
        else:
            continue    
        
        commend = "hisat2 -p {} --dta -x {} --rna-strandness RF --summary-file {}.log -1 {} -2 {} -S {}.sam".format(CPU, path_index, out_file_name, input_file1, input_file2, out_file_name)

    p = subprocess.Popen(commend, shell = True)
    # p = subprocess.Popen('echo "{}"'.format(commend), shell = True)
    p.wait()


    p2 = subprocess.Popen("samtools sort -@ {} -o {}.bam {}.sam".format(CPU, out_file_name, out_file_name), shell = True)
    # p2 = subprocess.Popen('echo "samtools sort -@ {} -o {}.bam {}.sam"'.format(CPU, out_file_name, out_file_name), shell = True)
    p2.wait()

    if os.path.exists(out_file_name + ".sam"):
        os.remove(out_file_name + ".sam")
