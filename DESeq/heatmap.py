import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']

DATAMATRIX = sys.argv[1] # input data matrix, columns = ["GeneID", "sample1", "sample2", ...]
OUT = sys.argv[2]
TITLE = sys.argv[3]

df = pd.read_csv(DATAMATRIX, sep = "\t")

df.dropna(inplace = True)
df = df.set_index("GeneID")
df = df[(df!=0).any(axis=1)] # drop all zero row
df = df.div(df.max(axis=1), axis=0) # normalize

###################################################

plt.figure(figsize = (20, 12))

heatmap = plt.pcolor(df, cmap = "viridis", edgecolors = 'face')

plt.xticks(np.arange(0, len(df.columns), 1) + 0.5, df.columns, fontsize = 20, rotation = 45)
plt.yticks(np.arange(len(df.index), 0, -1) - 0.5 , df.index, fontsize = 20)

plt.xlabel("Sample", fontsize = 30, labelpad = 15)
plt.ylabel("Gene", fontsize = 30, labelpad = 15)

plt.title(TITLE, fontsize = 40, pad = 50)

cbar = plt.colorbar()
cbar.ax.set_ylabel("Normalized TPM", fontsize = 20, labelpad = 35)

for t in cbar.ax.get_yticklabels():
     t.set_fontsize(20)

plt.savefig(OUT, bbox_inches = "tight")
plt.show()
