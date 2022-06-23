import sys
import json
import os
import subprocess
import time
from glob import glob

raw_path = sys.argv[1]
filter_path = sys.argv[2]
temp_path = sys.argv[3]

raw_files = sorted(glob(raw_path))
filter_files = sorted(glob(filter_path))

raw_proc = []

for raw in raw_files:
    while len(raw_proc) >= 6:

        for i, proc in enumerate(raw_proc):
            if not proc.poll() is None:
                raw_proc.pop(i)
                break
    
    name = os.path.basename(raw).replace(".fastq.gz", "").replace(".fq.gz", "")
    out  = os.path.join(temp_path, name + ".txt")
    print(raw)
    p = subprocess.Popen(f"/home/exeman/clc-assembly-cell-4.0.12-linux_64/clc_sequence_info {raw} > {out}", shell = True)
    raw_proc.append(p)
    time.sleep(0.1)

while len(raw_proc) != 0:
    for i, proc in enumerate(raw_proc):
        if not proc.poll() is None:
            raw_proc.pop(i)
            break

print(raw_proc)

filt_proc = []

for filt in filter_files:
    while len(filt_proc) >= 6:

        for i, proc in enumerate(filt_proc):
            if not proc.poll() is None:
                filt_proc.pop(i)
                break

    name = os.path.basename(filt).replace(".filter.fastq.gz", "").replace(".filter.fq.tz", "")
    out  = os.path.join(temp_path, name + ".txt")
    print(filt)
    p = subprocess.Popen(f"/home/exeman/clc-assembly-cell-4.0.12-linux_64/clc_sequence_info {filt} >> {out}", shell = True)
    filt_proc.append(p)
    time.sleep(0.1)

while len(filt_proc) != 0:
    for i, proc in enumerate(filt_proc):
        if not proc.poll() is None:
            filt_proc.pop(i)
            break

print(filt_proc)

print("Exit status 0")
