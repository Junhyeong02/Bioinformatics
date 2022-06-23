import sys
import os
from Bio import SeqIO
import pandas as pd

fasta_path = sys.argv[1]
tsv_path = sys.argv[2:]

Domain = {}
other_domain = {}
order = []

for record in SeqIO.parse(fasta_path, "fasta"):
    Domain[record.id] = 0
    other_domain[record.id] = []
    order.append(record.id)

for tsv in tsv_path:
    with open(tsv) as f:
        for line in f.readlines():
            data = line.split("\t")
            ID, domain = data[0], data[4]
            if ID not in Domain:
                continue

            if domain == "PF00249":
                Domain[ID] += 1

            elif domain.startswith("PF"):
                other_domain[ID].append(domain)

print("ID\t#PF00249\tother domain")





# for ID in order:
#     print("{}\t{}\t{}".format(ID, Domain[ID], '\t'.join(other_domain[ID])))

