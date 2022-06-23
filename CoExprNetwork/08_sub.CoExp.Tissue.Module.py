import sys
import os
import numpy as np
import pandas as pd

MYB_module_path = sys.argv[1] # ../06.CoExpNetWork/module_MYB.txt
module_tissue_path = sys.argv[2] # ../06.CoExpNetWork/module_tissue.txt
out = sys.argv[3]

df_MYB = pd.read_csv(MYB_module_path, sep = "\t")

for idx in df_MYB.index:
    ID = df_MYB.loc[idx, "ID"]
    df_MYB.loc[idx, "module"] = ID.split("_")[0] + df_MYB.loc[idx, "module"]

df_tissue = pd.read_csv(module_tissue_path, sep = "\t")

for idx in df_tissue.index:
    df_tissue.loc[idx, "module"] = df_tissue.loc[idx, "Base"] + df_tissue.loc[idx, "module"]

df = pd.merge(df_MYB, df_tissue, left_on = "module", right_on = "module", how = "inner")
df.drop(["module", "Base"], axis = 1, inplace = True)

df.to_csv(out, sep = "\t", index = None)
