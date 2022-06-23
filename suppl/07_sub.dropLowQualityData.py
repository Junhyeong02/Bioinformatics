import sys
import os
import numpy as np
import pandas as pd
from glob import glob

mappingRate = sys.argv[1]
pathExpData = sys.argv[2]

expData = glob(os.path.join(pathExpData, "*.txt"))

df = pd.read_csv(mappingRate, sep = "\t")

bad_sample = list(df[df["Align_rate"] < 70.0]["sample"])

print(bad_sample)

for exp in expData:
    exp_df = pd.read_csv(exp, sep = "\t", index_col = "GeneID")

    for bad in bad_sample:
        try:
            exp_df.drop(bad, inplace = True, axis = 1)
        except KeyError:
            pass

    exp_df.to_csv(exp.replace(".txt", ".qc.txt"), sep = "\t")
