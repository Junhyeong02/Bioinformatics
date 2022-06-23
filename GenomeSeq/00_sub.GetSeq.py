import sys
import os
from glob import glob
from Bio import SeqIO

id_list = sys.argv[1]
fasta_path = sys.argv[2]

fasta_list = glob(fasta_path)

with open(id_list) as f:
    target_id = list(map(lambda x : x.strip(), f.readlines()))

for fasta in fasta_list:
    # print(fasta)
    for record in SeqIO.parse(fasta, "fasta"):
        if record.id in target_id:
            print(">{}\n{}".format(record.id, record.seq))

