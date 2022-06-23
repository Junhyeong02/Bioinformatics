import sys
import os
import numpy as np
import pandas as pd

subgroup_path = sys.argv[1] # ../05.TREE/Subgroup_MYB.txt
nwk_path = sys.argv[2]      # ../05.TREE/R2R3_MYB.align.15.fa.nwk
out_path = sys.argv[3]      # ../05.TREE/R2R

f = open(nwk_path)
data = f.read()

df = pd.read_csv(subgroup_path, sep = "\t")

for idx in df.index:
    subgroup = df.loc[idx, "Subgroup"]
    myb_name = df.loc[idx, "MYBs"]

    print(myb_name)
    data = data.replace(myb_name + ":", myb_name + "_" + subgroup + ":")

fw = open(out_path, "w")
fw.write(data)
fw.close()

