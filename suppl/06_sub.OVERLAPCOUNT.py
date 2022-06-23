import sys
from glob import glob

PATH = sys.argv[1]
extension = sys.argv[2]
out_file = sys.argv[3]

log_list = glob(PATH+extension)

fw = open(out_file, "w")
fw.write("name\ta1\ta2\tb1\tb2\n")

for log in log_list:

    TGFam_a = set()
    TGFam_b = set()
    Original_a = set()
    Original_b = set()

    with open(log) as f:
        f.readline()
        
        for line in f.readlines():
            line = line.strip().split("\t")

            TGFamid = line[0]
            Originalid = line[5]

            tag = line[-1]
            print(tag)
            if tag == "MYB":
                TGFam_a.add(TGFamid)
                Original_a.add(Originalid)

            elif tag == "NA":
                TGFam_b.add(TGFamid)
                Original_b.add(Originalid)

    fw.write("{}\t{}\t{}\t{}\t{}\n".format(log, len(Original_a), len(TGFam_a), len(Original_b), len(TGFam_b)))


fw.close()
