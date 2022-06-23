import sys
import os
import numpy as np
import pandas as pd
import re
from glob import glob

path = sys.argv[1] ### ../04.mapping/CM334.Pc/
readtype = sys.argv[2] ## PE or SE
out = sys.argv[3] ###
log_data = sorted(glob(path+ '*.log'))

count = dict()
percent = dict()


columns = ["Total reads", "Aligned 0 times", "Aligned exactly 1 time", "Aligned > 1 times", "Mapping rate"]
for col in columns:
    count[col] = dict()

for log in log_data:
    with open(log) as f:
        data = f.readlines()

    print(log)

    if re.search(" were (\S+); of these:", data[1]).group(1) == "unpaired":
        temp = ""

    else:
        temp = "concordantly "
    sample = os.path.basename(log).replace(".log", "")
    total = re.search("^(\d+) reads; of these:\n", data[0]).group(1)
    exact, pexact = re.search(f"(\d+) \((\S+)\) aligned {temp}exactly 1 time", data[3]).groups()
    times0, ptimes0 = re.search(f"(\d+) \((\S+)\) aligned {temp}0 times", data[2]).groups()
    times2, ptimes2 = re.search(f"(\d+) \((\S+)\) aligned {temp}>1 times", data[4]).groups()
    # disco = re.search("(\d+) \(\S+\) aligned discordantly 1 time", data[7]).group(1)
    # pdisco = f"{float(disco)/float(total):.2f}%"

    mappingrate = re.search("^(\S+) overall alignment rate", data[-1]).group(1)

    count[columns[0]][sample] = f"{total}"
    count[columns[1]][sample] = f"{times0} ({ptimes0})"
    count[columns[2]][sample] = f"{exact} ({pexact})"
    count[columns[3]][sample] = f"{times2} ({ptimes2})"
    # count[columns[4]][sample] = f"{disco} ({pdisco})"
    
    count[columns[4]][sample] = mappingrate

df = pd.DataFrame(count)
df.to_csv(out, sep = "\t", index_label = "Sample ID")
