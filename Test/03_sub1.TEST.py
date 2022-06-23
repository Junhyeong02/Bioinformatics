import sys
import os
from glob import glob
from TGFam_Resource_test import DoTest

dir_path = sys.argv[1]

gff_list = sorted(glob(dir_path + "*.gff3"))
genome_list = sorted(glob(dir_path + "*.fasta"))
cds_list = sorted(glob(dir_path + "*CDS.fa"))
pep_list = sorted(glob(dir_path + "*PEP.fa"))

for gff, genome, cds, pep in zip(gff_list, genome_list, cds_list, pep_list):
    if not os.path.exists("results"):
        os.mkdir("results")

    head = gff.replace(dir_path, "")[:4]
    print("\n"+ head)

    print(gff, genome, cds, pep, sep = "\n")
    DoTest(gff, genome, cds, pep, head, "results/")   
