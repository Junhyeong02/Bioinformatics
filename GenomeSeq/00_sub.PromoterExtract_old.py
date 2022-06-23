import sys
import os
from Bio import SeqIO, Seq

class Gene():
    def __init__(self, ID, start, end, Str = "+"):
        self.ID = ID


        if Str == "+":
            self.promoterStart = start - 2000
            self.promoterEnd = start - 1

        elif Str == "-":
            self.promoterStart = end
            self.promoterEnd = end + 2000

        self.__start = start
        self.__end = end
        

def GffReader(gff_path):
    GeneData = {}

    with open(gff_path) as f:
        for line in f.readlines():
            line = line.strip()

            if len(line) == 0:
                continue

            LineData = line.split('\t')
    
            if LineData[2] == "gene":
                ID = LineData[-1].replace("ID=", "")
                loc = LineData[0]
                Str = LineData[6]
                start = LineData[3]
                end = LineData[4]
                
                if loc not in GeneData:
                    GeneData[loc] = list()
                
                GeneData[loc].append(Gene(ID, start, end, Str))

    return GeneData

def FastaReader(gene_data:dict, fasta_path:str)->None:
    for seq_record in SeqIO.parse(fasta_path, "fasta"):
        if seq_record.id not in gene_data:
            continue

        for gene in gene_data[seq_record.id]:
            CDS = Seq("")

            for start, end in gene.getCDS():
                CDS += seq_record.seq[start-1:end]
                    
            if gene.getStr() == "-":
                CDS = CDS.reverse_complement()

            print(">" + gene.getID() + "\n" + str(CDS))

    return



