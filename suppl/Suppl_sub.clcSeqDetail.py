import sys
import os
import subprocess
import time
from glob import glob


path = sys.argv[1]

filt_fastq_list = sorted(list(glob(os.path.join(path, "*.filter.fastq.gz"))))

process = []
out_fs = []

for fastq in filt_fastq_list:
    while len(process) >= 6:
        for i, proc in enumerate(process):
            if not proc.poll() is None:
                process.pop(i)
                break

    out = fastq.replace(".gz", ".log")
    out_fs.append(out)
    p = subprocess.Popen(f"/home/exeman/clc-assembly-cell-4.0.12-linux_64/clc_sequence_info -l {fastq} > {out}", shell = True)
    process.append(p)
    time.sleep(0.1)

while len(process) != 0:
    for i, proc in enumerate(process):
        if not proc.poll() is None:
            process.pop(i)
            break
