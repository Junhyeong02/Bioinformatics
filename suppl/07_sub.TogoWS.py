import sys
import os
import pandas as pd
from Bio import TogoWS
import time
import json

term2gene = sys.argv[1]
out = sys.argv[2]
filterpath = sys.argv[3]

fw2 = open(out + ".KOtoMAP.txt", "w")

df = pd.read_csv(term2gene, sep = "\t", header = None, names = [0,2])
filt = set()

with open(filterpath) as f:
    for line in f.readlines():
        pathwayNum = line.split("\t")[0]
        filt.add(pathwayNum)

KOterm = set(k for k in df[0])
mapdict = {}

for k in KOterm:
   print(k)

print(len(KOterm))

for i, KO in enumerate(KOterm):
    term = TogoWS.entry("kegg-orthology", KO, field = "pathways", format = "json")
    time.sleep(0.05)
    terms = json.load(term)

    if len(terms) == 0:
        continue

    if i % 100 == 0:
        print(i)

    for key, val in terms[0].items():
        if key.strip("map") in filt and not key.startswith("map011") and not key.startswith("map012"):
            fw2.write(KO + "\t" + key + "\n")
            fw2.flush()
            mapdict[key] = val
            print(key)

fw2.close()
fw3 = open(out + ".MAPdiscription.txt", "w")

for key, val in mapdict.items():
    fw3.write(f"{key}\t{val}\n")

fw3.close()


