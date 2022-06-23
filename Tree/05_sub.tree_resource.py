import sys
import os
from glob import glob
from Bio import SeqIO
import pandas as pd

info_path = sys.argv[1]
fasta_path = sys.argv[2]
out_path = sys.argv[3]

info_list = sorted(glob(info_path  + "*.csv"), key = lambda x :x.split("/")[-1].split(".")[0])
fasta_list = sorted(glob(fasta_path  + "*.fa"), key = lambda x :x.split("/")[-1].split(".")[0])

print(info_list)
print(fasta_list)

MYB_related = open(out_path + "MYB_related.fa", "w")
R2R3_MYB = open(out_path + "R2R3_MYB.fa", "w")
MYB_3R = open(out_path + "3R_MYB.fa", "w")
Atypical_MYB = open(out_path + "Atypical_MYB.fa", "w")

for info, fasta in zip(info_list ,fasta_list):
    MYB_domain = {}
    with open(info) as f:
        f.readline()
        for line in f.readlines():
            ID, num = line.split("\t")[:2]
            MYB_domain[ID] = int(num)

    for record in SeqIO.parse(fasta, "fasta"):
        if MYB_domain[record.id] == 1:
            MYB_related.write(">{}\n{}\n".format(record.id, record.seq))
        elif MYB_domain[record.id] == 2:
            R2R3_MYB.write(">{}\n{}\n".format(record.id, record.seq))
        elif MYB_domain[record.id] == 3:
            MYB_3R.write(">{}\n{}\n".format(record.id, record.seq))
        elif MYB_domain[record.id] == 4:
            Atypical_MYB.write(">{}\n{}\n".format(record.id, record.seq))
        else:
            print("no record")


MYB_related.close()
R2R3_MYB.close()
MYB_3R.close()
Atypical_MYB.close()




