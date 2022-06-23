import sys
import os
import re
import pandas as pd
from glob import glob
from Bio import SeqIO

TGFam_gff = sys.argv[1]
fasta = sys.argv[2]            # ../TGFam.re/*/*.geneIncludingMYB.fasta
original_gff = sys.argv[3]      

TGFam_gene_location = {}

df = pd.read_csv(TGFam_gff, sep = "\t", names = ["seqname", "source", "feature", "start", "end", "score", "strand", "frame", "attribute"], header = None)

df.dropna(inplace = True)
df = df[df["feature"] == "gene"]

pre_MYB = set("ID=" + gene.id for gene in SeqIO.parse(fasta, "fasta"))

overlap_count = 0
no_overlap_count = 0

gff_df = pd.read_csv(original_gff, sep = "\t", names = ["seqname", "source", "feature", "start", "end", "score", "strand", "frame", "attribute"], header = None)

gff_df.dropna(inplace = True)
gff_df = gff_df[gff_df["feature"] == "gene"]

for idx in df.index:
    seqname = df.loc[idx, "seqname"]
    start = df.loc[idx, "start"]
    end = df.loc[idx, "end"]

    # if seqname not in gff_df["seqname"]:
        
    #     no_overlap_count += 1
    #     continue

    temp = gff_df[gff_df["seqname"] == seqname]

    for idx2 in temp.index:
        if temp.loc[idx2, "attribute"] not in pre_MYB:
             continue

        g_start = temp.loc[idx2, "start"]
        g_end = temp.loc[idx2, "end"]

        if (g_start <= start and start <= g_end) or\
           (g_start <= end and end <= g_end) or\
           (g_start >= start and g_end <= end):
            overlap_count += 1
            break

    else:
        no_overlap_count += 1

print(fasta)
print("Total number of overlap count : {}".format(overlap_count)) 
print("Total number of no overlapped gene : {}".format(no_overlap_count))
        
