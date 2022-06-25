# gff, genome -> fasta

import sys
import pandas as pd
from Bio import SeqIO
from Bio.Seq import Seq

gff = sys.argv[1]
genome = sys.argv[2]
out = sys.argv[3]

print(gff, genome, out)

df = pd.read_csv(gff, comment = "#", sep = "\t", names = ["seqname", "source", "feature", "start", "end", "score", "strand", "frame", "attribute"], header = None)
# read gff

df.dropna(inplace = True)
df["ID"] = df["attribute"].apply(lambda x: x.replace("ID=", "")) # ID 추출 "ID=" 이후 문자열

genome_data = {record.id : record.seq for record in SeqIO.parse(genome, "fasta")}

fw = open(out, "w")
chk = True

for idx in df.index:
    seqname = df.loc[idx, "seqname"]
    
    if not seqname in genome_data:
        print(seqname)
        continue

    if df.loc[idx, "feature"] == "gene":
        try:
            if strand == "-":
                PEP = PEP.reverse_complement()

            PEP = PEP.translate()
            fw.write(f">{ID}\n{PEP}\n")
        except NameError:
            if chk:
                chk = False
                pass
            else:
                raise NameError
            

        ID = df.loc[idx, "ID"]
        strand = df.loc[idx, "strand"]
        PEP = Seq("")

    if df.loc[idx, "feature"] == "CDS":
        assert ID == df.loc[idx, "ID"]
        PEP += genome_data[seqname][df.loc[idx, "start"]-1:df.loc[idx, "end"]]
       
if strand == "-":
    PEP = PEP.reverse_complement()

PEP = PEP.translate()
fw.write(f">{ID}\n{PEP}\n")

fw.close()
