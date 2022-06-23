import sys
import os
import subprocess
import time
from glob import glob

GTF_FILE = sys.argv[1]    # path of gtf file
PATH = sys.argv[2]        # path of bam file
CPU = sys.argv[3]
Prefix = sys.argv[4]

print(GTF_FILE, PATH)

Input_list = glob(os.path.join(PATH, "*.bam"))
Ref = os.path.basename(GTF_FILE)
print(Input_list)
process = []

for bam in Input_list:
    while len(process) >= 6:
        for i, proc in enumerate(process):
            if not proc.poll() is None:
               process.pop(i)
               break

    OUT_FILE = bam.replace("bam", Ref)
    print(OUT_FILE)
    # print("stringtie -p {} -e -G {} -o {} -l {} {}".format(CPU, GTF_FILE, OUT_FILE, Prefix, bam))
    p = subprocess.Popen("stringtie -p {} -e --rf -G {} -o {} -l {} {}".format(CPU, GTF_FILE, OUT_FILE, Prefix, bam), shell = True)
    process.append(p)
    time.sleep(0.1)

while len(process) != 0:
   for i, proc in enumerate(process):
       if not proc.poll is None:
           process.pop(i)
           break

time.sleep(5)

for p in process:
    p.wait()
