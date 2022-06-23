import sys
import os
import pandas as pd

target = sys.argv[1] # cann00906
GENE2TERM = sys.argv[2]
MAP2TERM = sys.argv[3]
TERM2NAME = sys.argv[4]
OUT = sys.argv[5]

gene2term = pd.read_csv(GENE2TERM, sep = "\t", names = ["gene", "ko"])
term2name = pd.read_csv(TERM2NAME, sep = "\t", names = ["ko", "name"])
map2term  = pd.read_csv(MAP2TERM, sep = "\t", names= ["map", "ko"])

term2name = term2name.groupby("ko", as_index = False).first()

map2term = map2term[map2term["map"] == target]

df = pd.merge(gene2term, map2term, on = "ko", how = "inner")
df = pd.merge(df, term2name, on = "ko", how = "inner")

df.drop("map", axis = 1, inplace = True)

df.to_csv(OUT, sep = "\t", index = False)
