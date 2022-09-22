# pip install biopython
import sys

class SeqRecord():
    def __init__(self, id, sequence):
        self.id = id
        self.sequence = sequence

class Gene():
    def __init__(self, id, location, start_pos, end_pos, forward = True):
        self.id = id
        self.location = location
        self.forward = forward
        self.start_pos = start_pos - 1
        self.end_pos = end_pos

    def get_seqeunce(self, seq_record):
        seq = seq_record.sequence[self.start_pos:self.end_pos]
        
        if not self.forward:
            seq = reverse_complement(seq)
        return seq

    def get_utr(self, seq_record, length = 1000):
        seq1 = seq_record.sequence[self.start_pos - length if self.start_pos > length else 0: self.start_pos]
        seq2 = seq_record.sequence[self.end_pos: self.end_pos + length]

        if self.forward:
            return seq1, seq2

        else:
            return reverse_complement(seq2), reverse_complement(seq1)

def reverse_complement(seq):
    seq = seq[::-1]
    atgc = {"A": "T", "T":"A", "G":"C" ,"C":"G"}
    seq = ''.join([atgc[s] if s in atgc else "N" for s in seq])

    return seq

def read_fasta(path, id):
    with open(path) as f:
        while True:
            line = f.readline()
            if line[0] == ">":
                record_id = line.split()[0].strip(">")
                print(record_id)
                if record_id == id:
                    seq_record = SeqRecord(id, "")
                    
                else:
                    continue

                seq_list = []
                while True:
                    seq = f.readline()
                    if len(seq) != 0 and not seq[0] == ">":
                         seq_list.append(seq.strip())

                         if len(seq_list) % 1000000 == 0:
                            print(len(seq_list))
                    else:
                        break
                
                seq_record.sequence = ''.join(seq_list)
                f.close()
                return seq_record

        """
        for line in f.readlines():
            if line.startswith(">"):
                record_id = line.split()[0].strip(">")
                if record_id == id:
                    pass

    for seq_record in SeqIO.parse(path, "fasta"):
        if seq_record.id == id:
            return seq_record.seq

    else:
        raise KeyError
        """


def print_seq(id, seq):
    print(">" + id)
    print(seq)
    return 

if __name__ == "__main__":
    gene_id  = sys.argv[1]
    location = sys.argv[2]
    start    = int(sys.argv[3])
    end      = int(sys.argv[4])
    strand   = sys.argv[5]
    fasta    = sys.argv[6]
    
    assert strand == "+" or strand == "-"

    if end < start:
        start, end = end, start

    seq_data = read_fasta(fasta, location)
    gene = Gene(gene_id, location, start, end, strand == "+")

    tgt_seq = gene.get_seqeunce(seq_data)
    before_seq, after_seq = gene.get_utr(seq_data)

    print_seq(gene.id, tgt_seq)
    print_seq("before_" + gene.id, before_seq)
    print_seq("after_" + gene.id, after_seq)

    # print(len(tgt_seq), len(before_seq), len(after_seq))