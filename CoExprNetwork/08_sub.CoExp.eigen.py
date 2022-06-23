# 모듈별로 발현 패턴을 보여주기 위한 코드
# 먼저 row 별로 0~1 사이로 정규화
# 그 다음 column 별로 평균을 구함
# 구한 결과를 표로 만들어서 반환
# 08_sub.CoExp.Data.py 실행 결과로 만들어진 폴더를 arg로 받음

import sys
import os
import pandas as pd
from glob import glob

path  = sys.argv[1] # ../06.CoExpNetwork/CM334/Module/

melist = glob(path + "*.txt")

result = {}

for me in melist:
    df = pd.read_csv(me, sep = "\t", index_col = "GeneID")
    df = df.div(df.max(axis=1), axis=0) # 정규화
    sei = df.describe().loc["mean", :] # 평균 계산
    result[os.path.splitext(os.path.basename(me))[0]] = sei

result = pd.DataFrame(result)

result.to_csv(os.path.join(path, "eigen.txt"), sep = "\t")
    

