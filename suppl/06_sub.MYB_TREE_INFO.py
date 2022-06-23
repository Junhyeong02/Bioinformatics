import sys
import os
from glob import glob
import pickle

GROUP_INFO_PATH = sys.argv[1]
TSV_PATH = sys.argv[2:]

print("#", GROUP_INFO_PATH)
print("#", TSV_PATH)
print("#", len(TSV_PATH))

DOMAIN_COUNT = dict()

for tsv in TSV_PATH:
    print("#", tsv)

    with open(tsv) as f:
        for line in f.readlines():
            data = line.strip().split("\t")

            if data[4] != "PF00249":
                continue

            if data[0] not in DOMAIN_COUNT:
                DOMAIN_COUNT[data[0]] = 0

            DOMAIN_COUNT[data[0]] += 1

print("#", len(DOMAIN_COUNT))

with open(GROUP_INFO_PATH) as f:
    f.readline()
    f.readline()
    
    print("old_id\tnew_id\tgroup\tnumber_of_domain\n")
    
    for line in f.readlines():
        data = line.strip().split('\t')
        
        if data[0] in DOMAIN_COUNT:
            print("{}\t{}\t{}\t{}".format(data[0], data[1], data[2], DOMAIN_COUNT[data[0]]))

        else:
            print("{}\t{}\t{}\tNA".format(data[0], data[1], data[2]))
