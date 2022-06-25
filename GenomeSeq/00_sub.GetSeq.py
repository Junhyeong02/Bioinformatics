# gene의 서열을 얻는 코드
# 입력 id_list : 줄바꿈으로 구분된 gene id
# 입력 fasta_path : fasta 파일의 경로
# 출력 : gene의 서열

import sys
from glob import glob
from Bio import SeqIO

id_list = sys.argv[1]
fasta_path = sys.argv[2]

fasta_list = glob(fasta_path)

with open(id_list) as f:
    target_id = list(map(lambda x : x.strip(), f.readlines()))

for fasta in fasta_list:
    # print(fasta)
    for record in SeqIO.parse(fasta, "fasta"):
        if record.id in target_id:
            print(">{}\n{}".format(record.id, record.seq))

