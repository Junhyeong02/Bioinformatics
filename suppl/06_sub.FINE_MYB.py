import sys
from Bio import SeqIO

PATH = sys.argv[1]
GeneIncludingMYB = sys.argv[2]
OUT = sys.argv[3]

MYB_set = set()

for record in SeqIO.parse(GeneIncludingMYB, "fasta"):
    MYB_set.add(record.id)
    print(record.id)

fw = open(OUT, "w")

with open(PATH) as f:
    fw.write(f.readline().strip() + "\ttag\n")
    
    for line in f.readlines():
        geneid = line.strip().split("\t")[5]

        if geneid in MYB_set:
            tag = "MYB"
        
        else:
            tag = "NA"

        data = line.strip() + "\t" + tag + "\n"

        fw.write(data)

fw.close()

