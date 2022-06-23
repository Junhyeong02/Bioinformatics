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
# print(df.columns)

for gene_list in target:
    for i, gene in enumerate(gene_list.split(", ")):
        CM334 = gene.split(", ")[i]
        Heinz = df.loc[gene, 'Heinz.v.4.0_PEP'].split(", ")[i]
        ECW = df.loc[gene, 'ECW.v.1.0_PEP'].split(", ")[i]
        Zunla = df.loc[gene, 'Zunla-1_v2.0_PEP'].split(", ")[i]
        chinense = df.loc[gene, 'Chinense.v.1.2.PEP'].split(", ")[i]
        baccatum = df.loc[gene, 'C_baccatum.v.1.2_PEP'].split(", ")[i]
        chiltepin = df.loc[gene, 'Chiltepin_v2.0_PEP'].split(", ")[i]
        SF = df.loc[gene, 'SF.v.1.0_PEP'].split(", ")[i]
    
    print('\t'.join([CM334, Heinz, ECW, Zunla, chinense, baccatum, chiltepin, SF]))

        
