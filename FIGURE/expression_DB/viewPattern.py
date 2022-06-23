import sys
import os
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle as pkl
from glob import glob
from matplotlib import rcParams

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']

def drawBar(ID:str, columns:list, exp:list, path:str)->None:
    prefix = os.path.splitext(os.path.basename(path))[0]
    print(prefix)
    
    plt.figure(figsize=(50, 20))
    plt.bar(columns, exp, color = "black", edgecolor = 'black')
    plt.title(f"{ID} : {prefix}", fontsize = 50)
    plt.xticks(columns, rotation = 50, fontsize = 40,  horizontalalignment="center")
    plt.yticks(fontsize = 30)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    # plt.ylabel('TPM', fontsize = 30)
    plt.savefig(f"result\{ID}_{prefix}.png", bbox_inches = "tight")
    plt.clf()

if __name__ == "__main__":
    target_gene = sys.argv[1:]
    # target_gene += sys.stdin.read().split()

    if len(target_gene) == 0:
        exit()

    with open("source\idf.pickle", "rb") as f:
        idf = pkl.load(f)
    
    for file in glob("result\*"):
        os.remove(file)

    for gene in target_gene:
        if gene not in idf:
            print(f"gene {gene} not found in database")
            continue    

        for path in idf[gene]:
            try:
                df = pd.read_csv(path, sep = '\t', index_col=0)
            except FileNotFoundError:
                continue

            col = df.columns
            expdf = df.loc[gene, :]
            if any(e>0 for e in expdf):
                drawBar(gene, col, expdf, path)

