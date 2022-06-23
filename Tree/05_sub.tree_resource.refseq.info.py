import sys
import os
from Bio import SeqIO

ID_list = sys.argv[1]
gff_path = sys.argv[2]
fasta_path = sys.argv[3]
out = sys.argv[4] #../05.Tree/ref

ID_rename = dict()
ID_count = dict()

with open(ID_list) as f:
    for line in f.readlines():
        Ref_ID, name = line.split()
        ID_rename[Ref_ID] = name
        ID_count[Ref_ID] = 0

with open(gff_path) as f:
    for line in f.readlines():
        if line.startswith("#"):
            continue
        
        data = line.split("\t")

        if data[0] not in ID_count:
            continue

        if "Name=PF00249" in data[-1]:
            try:
                ID_count[data[0]] += 1

            except KeyError:
                print("unknown")


R1 = open(out + ".MYB_related.fa", "w")
R2 = open(out + ".R2R3_MYB.fa", "w")
R3 = open(out + ".R3_MYB.fa", "w")
R4 = open(out + ".Atypical_MYB.fa", "w")

for record in SeqIO.parse(fasta_path, "fasta"):
    if record.id in ID_count:
        if ID_count[record.id] == 1: 
            R1.write(">{}\n{}\n".format(ID_rename[record.id], record.seq))

        if ID_count[record.id] == 2: 
            R2.write(">{}\n{}\n".format(ID_rename[record.id], record.seq))


        if ID_count[record.id] == 3: 
            R3.write(">{}\n{}\n".format(ID_rename[record.id], record.seq))


        if ID_count[record.id] == 4: 
            R4.write(">{}\n{}\n".format(ID_rename[record.id], record.seq))


        if ID_count[record.id] == 1: 
            print(record.id)

R1.close()
R2.close()
R3.close()
R4.close()





















