import sys
import os
import pickle as pkl
import pandas as pd 
from glob import glob

expData = sorted(glob("source\CM334.NaCl.TPM.avg.txt"))
idf = dict()

for data in expData:
    df = pd.read_csv(data, index_col = 0, sep = "\t")
    print(f"bulid idf from {data}...")

    for idx in df.index:
        if idx not in idf:
            idf[idx] = list()

        idf[idx].append(data)

with open("source\CM334.NaCl.avg.pickle", "wb") as fw:
    pkl.dump(idf, fw)
