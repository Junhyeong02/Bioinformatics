import sys
import os
import pandas as pd
import numpy as np
from glob import glob

temp_path = sys.argv[1]
temp_files = sorted(glob(os.path.join(temp_path, "*.txt")))

df = pd.DataFrame({"Sample ID" : [os.path.basename(tf).replace(".txt", "") for tf in temp_files]})

df.set_index("Sample ID", inplace = True)

for tf in temp_files:
    with open(tf) as f:
        idx = os.path.basename(tf).replace(".txt", "")
        data  = list(map(lambda x: x.strip(), f.readlines()))
        raw_total = int(data[6].split()[-1])
        filt_total = int(data[19].split()[-1])

        num_of_read = int(data[16].split()[-1])
        avg_length = float(data[24].split()[-1])

        trimmed_raw_percentage = filt_total/raw_total

        df.loc[idx, "Num.of reads"] = num_of_read
        df.loc[idx, "Total length(bp)"] = filt_total
        df.loc[idx, "Avg. length(bp)"] = avg_length
        df.loc[idx, "Trimmed/Raw(%)"] = trimmed_raw_percentage


df.to_csv(os.path.join(temp_path, "Result.tsv"), sep = "\t")
