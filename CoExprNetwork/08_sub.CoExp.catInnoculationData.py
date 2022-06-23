import sys
import os
import numpy as np
import pandas as pd
from glob import glob

samples = ["CM334.Mock", "CM334.Pc", "CM334.PepMov", "CM334.Pi", "CM334.TMV_P0", "CM334.TMV_P2" ]


df = pd.read_csv(f"../05.FPKM_TPM/{samples[0]}/{samples[0]}.TPM.qc.txt", sep = "\t", index_col = "GeneID")

df.columns = list(map(lambda x: "_".join([samples[0], x]), df.columns))

for sample in samples[1:]:
    path = f"../05.FPKM_TPM/{sample}/{sample}.TPM.qc.txt"
    
    temp = pd.read_csv(path, sep = "\t", index_col = "GeneID")

    temp.columns = list(map(lambda x: "_".join([sample, x]), temp.columns))

    df = pd.merge(df, temp, how = "inner", left_index = True, right_index = True)

df.to_csv("../06.CoExpNetwork/CM334.immun/CM334.innoculation.TPM.txt", sep = "\t")
