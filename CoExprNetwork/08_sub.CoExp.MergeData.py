# 샘플별로 FPKM, TPM 값이 계산된 table을 합치는 코드
# python3 08_sub.CoExpMergeData.py [OUTPUT] [file1] [file2] [file3] ...
# 각 파일은 GeneID 칼럼을 반드시 포함해야 한다.
# GeneID에 맞게 합쳐준다.

import sys
import pandas as pd

samples = sys.argv[2:]
OUTPUT = sys.argv[1]
# samples = ["CM334.Mock", "CM334.Pc", "CM334.PepMov", "CM334.Pi", "CM334.TMV_P0", "CM334.TMV_P2" ]

df = pd.read_csv(f"{samples[0]}", sep = "\t", index_col = "GeneID")
df.columns = list(map(lambda x: "_".join([samples[0], x]), df.columns))

for sample in samples[1:]:
    path = f"{sample}"
    temp = pd.read_csv(path, sep = "\t", index_col = "GeneID")
    temp.columns = list(map(lambda x: "_".join([sample, x]), temp.columns))
    df = pd.merge(df, temp, how = "inner", left_index = True, right_index = True)

df.to_csv(OUTPUT, sep = "\t")
