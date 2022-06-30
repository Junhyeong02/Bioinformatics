# map number, ko number table 만드는 코드
# input이 기억 안남

import sys
import json
import re

JSONPATH = sys.argv[1]
PREFIX = sys.argv[2]
OUT = sys.argv[3]

with open(JSONPATH) as f:
    db = json.load(f)

# print(db)

fw1 = open(OUT + ".MAP2TERM.txt", "w")
fw2 = open(OUT + ".MAP2NAME.txt", "w")

for temp1 in db["children"]:
    for temp2 in temp1["children"]:
        for data in temp2["children"]:
            name = data["name"]
            # print(name)
            try:
                mapid = re.search(
                    "\[PATH:(" + PREFIX + "[0-9]{5})\]$", name).group(1)
                term = re.search("[0-9]{5} (.+) \[PATH:", name).group(1)
            except AttributeError:
                continue

            fw2.write(f"{mapid}\t{term}\n")

            koset = set()
            for data2 in data["children"]:
                try:
                    ko = re.search("(K[0-9]{5}) ", data2["name"]).group(1)
                except AttributeError:
                    continue
                koset.add(ko)

            for ko in koset:
                fw1.write(f"{mapid}\t{ko}\n")

fw1.close()
fw2.close()
