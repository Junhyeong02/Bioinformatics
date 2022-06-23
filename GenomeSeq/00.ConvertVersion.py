import sys
import os
from Bio import SeqIO
import pandas as pd

"""
target_gene_path = sys.argv[1]
from_fasta = sys.argv[2]
out = sys.argv[3]

df = pd.read_csv(target_gene_path, sep = "\t")
df.dropna(inplace= True)
target_list = list(df["v1.5"])

print(target_list)
fw = open(out, "w")

for record in SeqIO.parse(from_fasta, "fasta"):
    if record.id in target_list:
        print(record.id)
        fw.write(">{}\n{}\n".format(record.id, record.seq))

fw.close()
"""

target_gene_fa = sys.argv[1]
to_fasta = sys.argv[2]

for record1 in SeqIO.parse(target_gene_fa, "fasta"):
    for record2 in SeqIO.parse(to_fasta, "fasta"):
        if record1.seq == record2.seq:
            print("{}\t{}\t{}\n".format(record1.id, record2.id, record2.seq))

