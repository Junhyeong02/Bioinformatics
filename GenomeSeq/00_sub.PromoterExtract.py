# gff 형식 파일과 fasta 형식 파일에서 유전자의 promoter 지역만을 추출하는 코드
# start codon에서 상위 2000개의 염기 서열을 추출

import sys
import os
from Bio import SeqIO
import pandas as pd

class Gene():
    def __init__(self, ID, start, end, Str = "+"):
        self.ID = ID
        self.strand = Str

        if Str == "+":
            self.startCodonStart = start
            self.startCodonEnd = start + 2
            self.promoterStart = start - 2000
            self.promoterEnd = start - 1

        elif Str == "-":
            self.startCodonStart = end-2
            self.startCodonEnd = end
            self.promoterStart = end + 1
            self.promoterEnd = end + 2000

def gffReader(gff_path, gene_list):
    GeneData = {}

    with open(gff_path) as f:
        for line in f.readlines():
            line = line.strip()

            if len(line) == 0:
                continue

            LineData = line.split('\t')
    
            if LineData[2] == "gene":
                ID = LineData[-1].replace("ID=", "")

                if ID not in gene_list:
                    continue

                loc = LineData[0]
                Str = LineData[6]
                start = LineData[3]
                end = LineData[4]
                
                if loc not in GeneData:
                    GeneData[loc] = list()
                
                GeneData[loc].append(Gene(ID, int(start), int(end), Str))

    return GeneData

def fastaReader(gene_data:dict, fasta_path:str, out_path)->None:
    # fw = open(out_path, "w")

    for seq_record in SeqIO.parse(fasta_path, "fasta"):
        if seq_record.id not in gene_data:
            continue

        for gene in gene_data[seq_record.id]:
            promoter = seq_record.seq[gene.promoterStart-1:gene.promoterEnd]
            startCodon = seq_record.seq[gene.startCodonStart-1:gene.startCodonEnd]

            if gene.strand == "-":
                promoter = promoter.reverse_complement()
                startCodon = startCodon.reverse_complement()

            # print(startCodon)
            # assert str(startCodon) == "ATG"
            print(">" + gene.ID + "\t" + readable[gene.ID] + "\n" + str(promoter))
            # fw.write(">{}\n{}\n".format(gene.ID, str(promoter)))

    # fw.close()
    return

if __name__ == "__main__":
    gene_path = sys.argv[1]
    gff_path = sys.argv[2]
    fasta_path = sys.argv[3]
    # out_path = sys.argv[4]
    
    df = pd.read_csv(gene_path, sep = "\t")
    gene_list = list(df["v2.0"])
    readable = {key : val for key, val in zip(list(df["v2.0"]), list(df["short name"]))}
    geneData = gffReader(gff_path, gene_list)
    fastaReader(geneData, fasta_path, None)
