# pip install biopython

import sys
from Bio import SeqIO

class Gene():
    def __init__(self, id:str, location:str, start_pos:int, end_pos:int, forward:bool = True):
        self.id = id
        self.location = location
        self.forward = forward
        self.start_pos = start_pos - 1
        self.end_pos = end_pos

    def get_seqeunce(self, seq_record):
        seq = seq_record[self.start_pos:self.end_pos]
        
        if not self.forward:
            seq = seq.reverse_complement()
        return seq

    def get_utr(self, seq_record, length = 1000):
        seq1 = seq_record[self.start_pos - length if self.start_pos > length else 0: self.start_pos]
        seq2 = seq_record[self.end_pos: self.end_pos + length]

        if self.forward:
            return seq1, seq2

        else:
            return seq2.reverse_complement(), seq1.reverse_complement()

def read_fasta(path, id):
    for seq_record in SeqIO.parse(path, "fasta"):
        if seq_record.id == id:
            return seq_record.seq

    else:
        raise KeyError

def print_seq(id, seq):
    print(">" + id)
    print(seq)
    return 

if __name__ == "__main__":
    gene_id:str  = sys.argv[1]
    location:str = sys.argv[2]
    start:int    = int(sys.argv[3])
    end:int      = int(sys.argv[4])
    strand:str   = sys.argv[5]
    fasta:str    = sys.argv[6]
    
    assert strand == "+" or strand == "-"

    seq_data = read_fasta(fasta, location)
    gene = Gene(gene_id, location, start, end, strand == "+")

    tgt_seq = gene.get_seqeunce(seq_data)
    before_seq, after_seq = gene.get_utr(seq_data)

    print_seq(gene.id, tgt_seq)
    print_seq("before_" + gene.id, before_seq)
    print_seq("after_" + gene.id, after_seq)

    # print(len(tgt_seq), len(before_seq), len(after_seq))