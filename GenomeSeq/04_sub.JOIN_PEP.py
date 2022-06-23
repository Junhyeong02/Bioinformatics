import sys
import os
from Bio import SeqIO

assert len(sys.argv) == 5

path_gff = sys.argv[1]
path_original_fasta = sys.argv[2]
path_TGFam_fasta = sys.argv[3]
path_outfile_fasta = sys.argv[4]



MYB_ID = set()
gene_count = 0

with open(path_gff) as f:
    for line in f.readlines():
        line = line.strip()
        
        if line == '':
            continue

        data = line.split()

        if data[2] == "gene":
            MYB_ID.add(data[-1].replace("ID=", ""))
            gene_count += 1

if len(MYB_ID) != gene_count:
    print("gene count error")

fw = open(path_outfile_fasta, "w")

line_number = 0

for record in SeqIO.parse(path_TGFam_fasta, "fasta"):
    fw.write(">{}\n{}\n".format(record.id, record.seq))
    line_number += 1

print("TGFam_MYB : {}".format(line_number))
gene_count = 0

for record in SeqIO.parse(path_original_fasta, "fasta"):
    if record.id in MYB_ID:
        print(record.id)
        fw.write(">{}\n{}\n".format(record.id, record.seq))
        line_number += 1 
        gene_count += 1

print("Original_MYB : {}".format(gene_count))
print("Total_number : {}".format(line_number))

fw.close()
