import sys
import os
import pandas as pd
from glob import glob


datapath = sys.argv[1]
data = glob(datapath + "*DEG.txt")

for path in data:
    df = pd.read_csv(path, sep = "\t")

    print(df)
    df["ID"] = df["Unnamed: 0"].apply(lambda x: x.split("|")[0])
    df.drop("Unnamed: 0", axis = 1, inplace = True)

    df =df[[df.columns[-1]] + list(df.columns[:-1])]
    path = os.path.splitext(path)[0]+ ".format.txt"
    df.to_csv(path, sep = "\t", index = None, na_rep = "NA") 



