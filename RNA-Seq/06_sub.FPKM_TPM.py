import sys
import os
import numpy as np
import pandas as pd
import time
from multiprocessing import Process, Manager, Pool
from glob import glob 

head = ["sequence", "source", "feature", "start", "end", "score", "strand", "phase", "attri"]

def work(pid, gtf, result1, result2):
    print(gtf) 

    df = pd.read_csv(gtf, sep = "\t", comment = "#", names = head)
    df = df[df["feature"] == "transcript"]

    FPKM = dict()
    TPM = dict()
   
    for i, attri in enumerate(df["attri"]):
        if i %1000 == 0:
            print(f"{gtf}	{i}")

        attri = attri.strip(";").split("; ")
        gene = attri[0].split()[1].strip('"')
        F = attri[-2].split()[1].strip('"')
        T = attri[-1].split()[1].strip('"')
        
        FPKM[gene] = float(F)
        TPM[gene] = float(T)
    
    result1.put((gtf, FPKM))
    result2.put((gtf, TPM))
    print("put...")

    return

def work2(pid, data, out, order):
    tempdict = dict()

    while True:
        tmp = data.get()
        if tmp == "stop":
            df = pd.DataFrame(tempdict)
            df = df[[os.path.basename(gtf) for gtf in gtf_list]]
            df.to_csv(out, sep = "\t", index_label = "GeneID")
            return

        else:
            tempdict[os.path.basename(tmp[0])] = tmp[1]

if __name__ == "__main__":
    GTF_PATH = sys.argv[1]
    PATH_OUT = sys.argv[2]

    gtf_list = sorted(glob(GTF_PATH + "*.gtf"))
    FPKM = Manager().Queue()
    TPM = Manager().Queue()

    with Pool(6) as pl:
        ret = pl.starmap(work, [[i, gtf, FPKM, TPM] for i, gtf in enumerate(gtf_list)])
        print(ret)
        

    print("merging...")
    FPKM.put("stop")
    TPM.put("stop")

    p1 = Process(target = work2, args = (1, FPKM, PATH_OUT + ".FPKM.txt", gtf_list))
    p2 = Process(target = work2, args = (1, TPM, PATH_OUT + ".TPM.txt", gtf_list))
    
    p1.start()
    p2.start()

    p1.join()
    p2.join()

