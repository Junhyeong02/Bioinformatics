import sys
import os
import numpy as np
import pandas as pd
from glob import glob


path  = sys.argv[1] # ../06.CoExpNetwork/CM334/Module/

melist = glob(path + "*.txt")

result = {}

for me in melist:
    df = pd.read_csv(me, sep = "\t", index_col = "GeneID")
    df = df.div(df.max(axis=1), axis=0)
    sei = df.describe().loc["mean", :]
    result[os.path.splitext(os.path.basename(me))[0]] = sei

result = pd.DataFrame(result)

result.to_csv(os.path.join(path, "eigen.txt"), sep = "\t")
    

