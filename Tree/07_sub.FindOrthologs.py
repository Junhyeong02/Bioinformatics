import sys
import os
import pandas as pd

ortho_tsv = sys.argv[1]
index = sys.argv[2]
target = sys.argv[3:]

if not os.path.exists(ortho_tsv):
    print("NotFound")
    exit()

ortho_dict = {}

df = pd.read_csv(ortho_tsv, sep = "\t", index_col = "C_annuum.v.2.0_PEP")

for gene in target:
    temp = df[df.index == gene]
    print(temp)

        
