import sys
import os
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle as pkl
import shutil
from glob import glob
from matplotlib import rcParams

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']

def drawBar(ID:str, columns:list, exp:list, path:str, name:str)->None:
    prefix = os.path.splitext(os.path.basename(path))[0]
    
    plt.figure(figsize=(30, 20))
    plt.bar(columns, exp, color = "black", edgecolor = 'black')
    plt.title(f"{ID} : {prefix}", fontsize = 40)
    plt.xticks(columns, rotation = 90, fontsize = 20,  horizontalalignment="center")
    plt.yticks(fontsize = 30)
    plt.ylabel('TPM', fontsize = 30)
    plt.savefig(f"..\{name}\{ID}_{prefix}.png", bbox_inches = "tight")
    plt.close('all')

if __name__ == "__main__":
    ortholog = glob("..\MYB_ortholog\*")
    # target_gene += sys.stdin.read().split()

    with open("source\idf.pickle", "rb") as f:
        idf = pkl.load(f)

    for file in ortholog:
        f = open(file)
        file_name = os.path.splitext(os.path.basename(file))[0]
        target_gene = f.read().strip().split()
        
        if not os.path.exists(f"../{file_name}"):
            os.mkdir(f"../{file_name}")

        
        f.close()
        shutil.move(file, f"..\{file_name}\{file_name}.txt")

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
                    drawBar(gene, col, expdf, path, file_name)

        

