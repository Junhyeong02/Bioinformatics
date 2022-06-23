import sys
import os
from Bio import SeqIO

path1 = sys.argv[1]
path2 = sys.argv[2]

DATA = {}

for record in SeqIO.parse(path1, "fasta"):
	DATA[record.id] = record.seq

for record in SeqIO.parse(path2, "fasta"):
	if record.id not in DATA:
		print(">{}\nNoDATA\n{}".format(record.id, record.seq))

	elif DATA[record.id] != record.seq:
		print(">{}\n{}\n{}".format(record.id, DATA[record.id], record.seq))

