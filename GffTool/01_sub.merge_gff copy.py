import sys
import os
import re
from glob import glob
import pandas as pd

class Gene():
    def __init__(self, ID, start, end, data, strand, chk="TGFam"):
        self.ID = ID
        self.start = start
        self.end = end
        self.data = data
        self.strand = strand
        self.chk = chk

def is_sorted(X_list, function):
    return all(function(x) <= function(y) for x, y in zip(X_list[:-1], X_list[1:]))

def read_gff(gff_path: str) -> pd.DataFrame:
    columns = ["seqname", "source", "feature", "start", "end", "score", "strand", "frame", "attribute"]
    df = pd.read_csv(gff_path, sep = "\t", comment = "#", names = columns, header = None)

    return df

def main(base_gff :str, load_gff:str, fasta:str, output:str ) -> None:
    base_df = read_gff(base_gff)
    load_df = read_gff(load_gff)

    chrs = base_df["location"].unique()

    print("\nTotal number of base gene : {}".format(len(base_df)))
    print("Total number of base Chr/scaffold : {}".format(len(chrs)))   



TGFam_gene_location = {}
    
if all(is_sorted(val, function = lambda x : x.start) for val in TGFam_gene_location.values()):
    print("TGFam_gff : sorted")

else: 
    print("TGFam_gff : not sorted")

# fw_GFF = open(OUT_HEAD+".gff", "w")
# fw_TABLE = open(OUT_HEAD+".txt", "w")

# header = "TGFam_ID\tLocation\tTGFam_start\tTGFam_end\tTGFam_strand\tOriginal_ID\tOriginal_start\tOriginal_end\tOriginal_strand\n"
# fw_TABLE.write(header)

### reading Original_gff ###
print("\nreading Original_gff...")

overlap_count = 0
not_overlap_count = 0

with open(Original_gff) as f:
    gff_list = re.split("[\n]{2,}", f.read().strip())

    # print(gff_list)
    for gff_data in gff_list:
        gene_line = gff_data.split()

        try:
            loc = gene_line[0]
            start = int(gene_line[3])
            end = int(gene_line[4])
            ID = gene_line[8].replace("ID=", "")
            # print(ID)
            strand = gene_line[6]

        except IndexError:
            break

        if loc not in TGFam_gene_location:
            TGFam_gene_location[loc] = [Gene(ID, start, end, gff_data.strip(), strand, "Ori")]
            not_overlap_count += 1
            continue
        
        overlap = False
 
        for g in TGFam_gene_location[loc]:
            if g.chk == "Ori":
                continue

            if (g.start <= start and start <= g.end) or\
               (g.start <= end and end <= g.end) or\
               (g.start >= start and g.end <= end):
                # print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(g.ID, loc, g.start, g.end,\
                #                                                     g.strand, ID, start, end, strand))

                # fw_TABLE.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(g.ID, loc, g.start, g.end,\
                #                                                              g.strand, ID, start, end, strand))        
                overlap_count += 1
                overlap = True

        if not overlap:
            TGFam_gene_location[loc].append(Gene(ID, start, end, gff_data.strip(), strand, "Ori"))
            not_overlap_count += 1

    print("sorting...")
    contig_list = os.popen("grep -P '>[^\s]+' {}|cut -f1".format(FASTA)).read().strip().replace(">", "").split()

    for key in contig_list:
        if key not in TGFam_gene_location:
            continue
    
        for data in sorted(TGFam_gene_location[key], key = lambda x: x.start):
            # fw_GFF.write(data.data)
            # fw_GFF.write("\n\n")
            pass

    print("\nTotal number of Original gene : {}".format(len(gff_list)))
    print("Total number of overlap count : {}".format(overlap_count)) 
    print("Total number of no overlapped gene : {}".format(not_overlap_count))

# fw_GFF.close()
# fw_TABLE.close()      

if __name__ == "__main__":
    TGFAM_GFF = sys.argv[1]
    ORIGINAL_GFF = sys.argv[2]
    FASTA = sys.argv[3]
    OUT_HEAD = sys.argv[4]

    main(TGFAM_GFF, ORIGINAL_GFF, FASTA, OUT_HEAD)