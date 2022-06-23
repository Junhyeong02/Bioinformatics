import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
from math import log10, log2
from matplotlib import rcParams, rc

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']

#####################################

p_cutoff = 0.01
ptype = "pvalue" # pval of padj

cUP = "#065D0C"
cDOWN = "#770B08"
cNOT_DEG = "#AAAAAA"

####################################

def colormap(x, ptype, pcutoff, c_up, c_down, c_none):
    if x["log2FoldChange"] >= 1 and x[ptype] <= pcutoff:
        return c_up
        
    elif x["log2FoldChange"] <= -1 and x[ptype] <= pcutoff:
        return c_down
        
    else:
        return c_none

if __name__ == "__main__":
    DEGOUTPUT = sys.argv[1] # DEseq2 output format, [Gene_id, baseMean, log2FoldChange, lfcSE, stat, pvalue, padj]
    OUT = sys.argv[2]
    TITLE = sys.argv[3]

    df = pd.read_csv(DEGOUTPUT, sep = "\t")

    print(df)
    totalgene = len(df.index)
    print(f"Total number of genes: {totalgene}")

    df.dropna(inplace = True)

    filteredgene = len(df.index)
    print(f"After filtering : {filteredgene}")

    df["color"] = df.apply(colormap, axis = 1, args = (ptype, p_cutoff, cUP, cDOWN, cNOT_DEG))
    df[ptype] = df[ptype].apply(lambda x : -log10(float(x)) if float(x) > 1e-10 else 10)

    ###############################################################################

    plt.figure(figsize=(25, 20))
    plt.scatter(df["log2FoldChange"], df[ptype], c = df["color"])
    
    plt.title(TITLE, fontsize = 40, pad = 50)
    plt.xlabel("log2FoldChange", fontsize = 40, labelpad = 40)
    plt.ylabel(f"-log10 {ptype}", fontsize = 40, labelpad = 40)

    plt.xticks([-10, -5, -1, 0, 1, 5, 10], fontsize = 25)
    plt.yticks(fontsize = 25)

    plt.axhline(-log10(p_cutoff), color = "#7E7E7E", ls = "--")
    plt.axvline(1, color = "#7E7E7E", ls = "--")
    plt.axvline(-1, color = "#7E7E7E", ls = "--")

    plt.margins(x = 0.01, y = 0.005)
    plt.xlim(-11, 11)
    plt.ylim(-0.5, 10.1)
    plt.savefig(OUT, bbox_inches = "tight")
    plt.show()

    ##############################################################################
