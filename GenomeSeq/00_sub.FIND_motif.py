import sys
import os
import pandas as pd
from glob import glob
from Bio import SeqIO

FASTA_PATH = sys.argv[1]
TSV_PATH = sys.argv[2]

FASTA_LIST = sorted(glob(FASTA_PATH))
TSV_LIST = sorted(glob(TSV_PATH))

for fasta, tsv in zip(FASTA_LIST, TSV_LIST):
    out = fasta.replace("/Genome_data/", "/Protein_data/").replace(".fa", ".MYB.fa")
        
    print(fasta, tsv, out)

    df = pd.read_csv(tsv, sep = "\t", names = [str(i) for i in range(13)], header = None)
    df_pfam = df[df["4"] == "PF00249"]

    pf_MYB = set(df_pfam["0"].tolist())
    # print(pf_MYB)

    fw = open(out, "w")

    for record in SeqIO.parse(fasta, "fasta"):
        if record.id in pf_MYB:
            fw.write(">{}\n{}\n".format(record.id, record.seq))
    
    fw.close()
    # print(df_pfam.head())
