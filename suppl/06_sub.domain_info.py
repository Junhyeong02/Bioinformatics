import sys
import os
from glob import glob

csv_path = sys.argv[1]

csv_list = list(glob(csv_path + "*.csv"))


for csv in csv_list:
    count = [0, 0, 0, 0]
    with open(csv) as f:
        f.readline()
        for line in f.readlines():
            count[int(line.split("\t")[1]) - 1] += 1
    
    count = list(map(lambda x: str(x), count))
    print(csv)
    print("\t".join(count))



