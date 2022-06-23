# target gene과 연결된 gene 중에서 CUTOFF 이상의 연결을 가진 gene을 저장
# KEGG 분석에서 GENE2TERM, TERM2GENE 데이터로 gene 설명 추가

import sys
import pandas as pd

target = sys.argv[1]
EDGEPATH = sys.argv[2]
CUTOFF = sys.argv[3]
GENE2TERM = sys.argv[4]
TERM2NAME = sys.argv[5]
OUT = sys.argv[6]

CUTOFF = float(CUTOFF)

df = pd.read_csv(EDGEPATH, sep = "\t")

df.drop(["direction", "fromAltName", "toAltName"], axis = 1, inplace = True)
df = df[df["weight"] >= CUTOFF]

df1 = df[df["fromNode"] == target]
df2 = df[df["toNode"] == target]

df1.drop("fromNode", axis = 1, inplace = True)
df2.drop("toNode", axis = 1, inplace = True)

df1.columns = ["Node", "weight"]
df2.columns = ["Node", "weight"]

df3 = pd.concat([df1, df2])

print(df3)

term2name = pd.read_csv(TERM2NAME, sep = "\t", names = ["term", "name"])
temp = term2name.groupby("term", as_index= False).first()

gene2term = pd.read_csv(GENE2TERM, sep = "\t", names = ["gene", "term"])

out1 = pd.merge(df3, gene2term, left_on = "Node", right_on = "gene", how = "inner")
out = pd.merge(out1, temp, on = "term", how = "inner")

out = out[["Node", "weight", "term", "name"]]

out.sort_values(by = "weight", ascending = False, inplace = True)
out.to_csv(OUT, sep = "\t", index = False, na_rep = "")
