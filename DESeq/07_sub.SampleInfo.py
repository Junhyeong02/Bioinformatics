# DESeq 하기 전에 sample_lst.txt, Phenotype.txt 만드는 코드
# 07.DESeq.sh 참조

import sys
import os
import json
from glob import glob

gtf_path = sys.argv[1]
out_path = sys.argv[2]
origin_gtf = sys.argv[3]
json_path = sys.argv[4]

gtf_list = sorted(glob((gtf_path + "*.gtf")))

fwslst = open(os.path.join(out_path, "sample_lst.txt"), "w")
fwphen = open(os.path.join(out_path, "Phenotype.txt"), "w")

fwphen.write("SampleID\tType\n")

for gtf in gtf_list:
    sample = os.path.basename(gtf).replace("." + origin_gtf, "")

    abspath = os.path.abspath(gtf)
    fwslst.write(f"{sample}\t{abspath}\n")
    fwphen.write(f"{sample}\n")

fwslst.close()
fwphen.close()

base = 0
read = 0

for jfile in glob(json_path + "*.json"):
    with open(jfile) as f:
        json_object = json.load(f)

    base += json_object["summary"]["after_filtering"]["total_bases"]
    read += json_object["summary"]["after_filtering"]["total_reads"]

print(base/read)

