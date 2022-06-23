import sys
import os
import numpy as np
import pandas as pd
import json
from glob import glob

path = sys.argv[1]
out = sys.argv[2]
end_type = sys.argv[3]

json_list = glob(path + "*.json")

df = {}

for col in ["Num. of reads", "Total length(bp)", "Avg. length(bp)", "Trimmed/Raw(%)"]:
    df[col] = dict()

for jsfile in json_list:
    with open(jsfile) as f:
        report = json.load(f)

    sample_names = os.path.basename(jsfile).replace(".filter.fastq.json", "")
 
    read1 = sample_names + "_read1"
    read2 = sample_names + "_read2"

    for i in range(1, 2 if end_type == "SE" else 3):
        read = f"{sample_names}_read{i}"
        # print(read)

        num_of_read = report[f"read{i}_after_filtering"]["total_reads"]
        total_length = report[f"read{i}_after_filtering"]["total_bases"]
        avg_length = total_length / num_of_read
        trimmed_raw = report[f"read{i}_after_filtering"]["total_bases"] / report[f"read{i}_before_filtering"]["total_bases"]

        df["Num. of reads"][read] = num_of_read
        df["Total length(bp)"][read] = total_length
        df["Avg. length(bp)"][read] = avg_length
        df["Trimmed/Raw(%)"][read] = trimmed_raw

df = pd.DataFrame(df)

df.to_csv(out, sep = "\t", index_label = "sample ID")
