import sys
import pandas as pd

tsv = sys.argv[1] 
cut = sys.argv[2]
out = sys.argv[3]

df = pd.read_csv(tsv, sep = "\t", comment = "#", names = ["asterisk", "gene", "KO", "thre", "score", "e", "dis"])

print(df["e"])
df.drop(["asterisk", "thre", "score", "dis"], axis = 1, inplace = True)
df = df[df["e"] < float(cut)]
df = df.sort_values("e").groupby("gene", as_index = False).first()

print(df)

fw1 = open(out + ".GENE2KO.txt", "w")
fw2 = open(out + ".KO.txt", "w")

KOterm = set()

for idx in df.index:
    fw1.write(df.loc[idx, "gene"] + "\t" + df.loc[idx, "KO"] + "\n")
    KOterm.add(df.loc[idx, "KO"])

fw1.close()

for s in KOterm:
    fw2.write(s + "\n")

fw2.close()
