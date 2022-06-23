import sys
import os
import re

INPUT_FILE = sys.argv[1]
OUTPUT_FILE = sys.argv[2]
VERSION = sys.argv[3]

fw = open(OUTPUT_FILE, "w")

print("\n" + INPUT_FILE)

with open(INPUT_FILE) as f:
    exon_number = 0
    count = 0
    for line in f.readlines():
        if line.strip() == "":
            continue
      
        count += 1
        data = line.strip().split("\t")
        Type = data[2]
        
        ID = data[-1].replace("ID=", "")
        
        if Type == "gene":
            information = 'gene_id "{}"; gene_version "{}"; gene_name "{}"; '.format(ID, VERSION, ID) + \
                          'gene_source "{}"; gene_biotype "protein_coding";'.format(data[1])
            exon_number = 1

        elif Type == "mRNA":
            data[2] = "transcript"
            information = 'gene_id "{}"; gene_version "{}"; transcript_id "{}"; '.format(ID, VERSION, ID) + \
                          'transicript_version "{}"; gene_name "{}"; gene_source "{}"; '.format(VERSION, ID, data[1]) + \
                          'gene_biotype "protein_coding"; transcript_name "{}"; '.format(ID) + \
                          'transcript_source "{}"; transcript_biotype "protein_coding";'.format(data[1])
        
        elif Type == "exon":    
            information = 'gene_id "{}"; gene_version "{}"; transcript_id "{}"; '.format(ID, VERSION, ID) + \
                          'transcript_version "{}"; exon_number "{}"; gene_name "{}"; '.format(VERSION, exon_number, ID) + \
                          'gene_source "{}"; gene_biotype "protein_coding"; '.format(data[1]) + \
                          'transcript_name "{}"; transcript_source "{}"; '.format(ID, data[1]) + \
                          'transcript_biotype "protein_coding"; exon_id "{}"; exon_version "{}";'.format(ID, VERSION)
            
            exon_number += 1

        else:
            information = 'gene_id "{}"; gene_version "{}"; transcript_id "{}"; '.format(ID, VERSION, ID) + \
                          'transcript_version "{}"; exon_number "{}"; gene_name "{}"; '.format(VERSION, exon_number, ID) + \
                          'gene_source "{}"; gene_biotype "protein_coding"; '.format(data[1]) + \
                          'transcript_name "{}"; transcript_source "{}"; '.format(ID, data[1]) + \
                          'transcript_biotype "protein_coding"; protein_id "{}"; protein_version "{}";'.format(ID, VERSION)
            
        data[-1] = information
        data = '\t'.join(data)

        fw.write(data + '\n')
        # print(data)
    
    print("number of line : {}".format(count))

print("GTF created")
fw.close()     
