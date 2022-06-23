import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']

DEGOUTPUT1  = sys.argv[1] # DEseq2 output format, [Gene_id, baseMean, log2FoldChange, lfcSE, stat, pvalue, padj]
DEGOUTPUT2  = sys.argv[2] # DEseq2 output format, [Gene_id, baseMean, log2FoldChange, lfcSE, stat, pvalue, padj]
ORTHOGROUPS = sys.argv[3] # OrthoFinder output, [Orthogroup, sample, ...]
GROUP1      = sys.argv[4]
GROUP2      = sys.argv[5]
DATAMATRIX1 = sys.argv[6] # input data matrix, columns = ["GeneID", "sample1", "sample2", ...]
DATAMATRIX2 = sys.argv[7] # input data matrix, columns = ["GeneID", "sample1", "sample2", ...]
OUT         = sys.argv[7]
TITLE       = sys.argv[8]

degout = pd.read_csv(DEGOUTPUT1, sep = "\t")
deglist = degout[degout.apply(lambda x : (x["log2FoldChange"] >= 1 or x["log2FoldChange"] <= -1) and x["padj"] <= 0.05, axis=1)]

deg = set(deglist[deglist.columns[0]])

degout = pd.read_csv(DEGOUTPUT2, sep = "\t")
deglist = degout[degout.apply(lambda x : (x["log2FoldChange"] >= 1 or x["log2FoldChange"] <= -1) and x["padj"] <= 0.05, axis=1)]
deg.update(set(deglist[deglist.columns[0]]))

print(deg)

og = pd.read_csv(ORTHOGROUPS, sep = "\t", index_col = "Orthogroup")
og = og[[GROUP1, GROUP2]]

og.fillna('', inplace = True)
deog = og[og.apply(lambda x : any(gene in deg for gene in x[GROUP1].split(", ") + x[GROUP2].split(", ")), axis = 1)]

print(deog)

mapdeog = deog.applymap(lambda x : x.split(", "), na_action = "ignore")

print(mapdeog)

mapdeog.reset_index(inplace = True)

og1 = mapdeog.explode(GROUP1, ignore_index = True)[["Orthogroup", GROUP1]]
og2 = mapdeog.explode(GROUP2, ignore_index = True)[["Orthogroup", GROUP2]]

og1 = og1.set_index(GROUP1)
og2 = og2.set_index(GROUP2)

groupsog1 = og1.groupby("Orthogroup", as_index = False).groups
groupsog2 = og2.groupby("Orthogroup", as_index = False).groups

dfs = list()

assert len(groupsog1.keys()) == len(groupsog2.keys())

for key1, key2 in zip(sorted(groupsog1.keys()), sorted(groupsog2.keys())):
    assert key1 == key2

    data1 = list(map(lambda x : None if x == "" else x, groupsog1[key1]))
    data2 = list(map(lambda x : None if x == "" else x, groupsog2[key2]))

    df = pd.DataFrame([[GROUP1] + data1, [GROUP2] + data2]).set_index(0).transpose()
    df["Orthogroup"] = key1
    dfs.append(df)

df = pd.concat(dfs, ignore_index = True)

print(df)

data1 = pd.read_csv(DATAMATRIX1, sep = "\t")
data2 = pd.read_csv(DATAMATRIX2, sep = "\t")

data1.set_index("GeneID", inplace = True)
data2.set_index("GeneID", inplace = True)

data1.columns = list(map(lambda x :x.split(".")[0], data1.columns))
data2.columns = list(map(lambda x :x.split(".")[0], data2.columns))

data1 = data1[[col for col in data1.columns if col.startswith(COL1)]]
data2 = data2[[col for col in data2.columns if col.startswith(COL2)]]

data1 = data1.mean(axis = 1).reset_index()
data2 = data2.mean(axis = 1).reset_index()

data1.columns = [GROUP1, f"{GROUP1}_val"]
data2.columns = [GROUP2, f"{GROUP2}_val"]

df = pd.merge(df, data1, on = GROUP1, how = "left")
df = pd.merge(df, data2, on = GROUP2, how = "left")

val = df[[f"{GROUP1}_val", f"{GROUP2}_val"]]
val = val.div(val.max(axis=1), axis=0)

tck = list(df.groupby("Orthogroup", as_index = False).head(1).index)
tcklabel = list(df.groupby("Orthogroup", as_index = False).head(1)["Orthogroup"])

#########################################################################

fig = plt.figure(figsize = (10, 15))
ax = plt.subplot(1, 1, 1)

ax.pcolor(val, cmap = "viridis")

ax.axes.set_xticks([0.5, 1.5], ["P. capsici", "P. infestans"], fontsize = 20)
ax.axes.set_yticks(tck, tcklabel, fontsize = 10)

ax.axes.set_xlabel("Phythopthora", fontsize = 30, labelpad = 15)
ax.axes.set_ylabel("Gene", fontsize = 30, labalpad = 15)

ax.axes.set_title(TITLE, fontsize = 40, pad = 50)

plt.savefig(OUT, bbox_inches = "tight")
plt.show()


