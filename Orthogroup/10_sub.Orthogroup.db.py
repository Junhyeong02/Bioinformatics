import sys
import pandas as pd

PATH = sys.argv[1]
OUT = sys.argv[2]
target = sys.argv[3:]

ref = pd.read_csv(PATH, sep = "\t")
print(ref)

for path in target:
    df = pd.read_csv(path, sep = "\t", names = [1,2,3])
    df.drop(1, inplace = True, axis = 1)
    df = df.set_index(3).apply(lambda x :x.str.split(", ").explode()).reset_index()

    ref = pd.merge(ref, df, how = "left", left_on = "gene", right_on = 2)
    ref.drop(2, inplace = True, axis = 1)
    print(df)

print(ref)
ref.to_csv(OUT, sep = "\t", index = False, na_rep = "NaN")


