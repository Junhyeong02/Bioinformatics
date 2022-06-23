# 바이오파이썬을 사용해서 chromosome을 그림
# Gene의 chromosome 상의 위치를 확인할 수 있다
# 그렇게 예쁜 그림이 나오지는 않는다
# 연습삼아 만들어본 코드

import sys
import os
import pandas as pd
from reportlab.lib.units import cm
from Bio.Graphics import BasicChromosome

target_gene = sys.argv[1]
gff = sys.argv[2]
genome = sys.argv[3]
out = sys.argv[4]

df = pd.read_csv(target_gene, sep = "\t")
df = df[["Orthogroup", genome, "color"]]
df = df[df[genome] != "None"]

for idx in df.index:
    if ", " in df.loc[idx, genome]:
        temp = df.loc[idx, genome].split(", ")
        df.loc[idx, genome] = temp[0]

        for t in temp[1:]:
            df.append({"Orthogroup" : df.loc[idx, "Orthogroup"], genome : t, "color" : df.loc[idx, "color"]}, ignore_index = True)

chromo_dict = {}

gff_df = pd.read_csv(gff, sep = "\t", names = ["seqname", "source", "feature", "start", "end", "score", "strand", "frame", "attribute"], header = None)
gff_df.dropna(inplace = True)
gff_df = gff_df[gff_df["feature"] == "gene"]
gff_df["attribute"] = gff_df["attribute"].apply(lambda x: x.replace("ID=", ""))

target_df = pd.merge(df, gff_df, left_on = genome, right_on = "attribute", how = "inner")
target_df = target_df[["Orthogroup", genome, "seqname", "color", "start", "end", "strand"]]

for idx in target_df.index:
    if target_df.loc[idx, "seqname"] not in chromo_dict:
        chromo_dict[target_df.loc[idx, "seqname"]] = []

    chromo_dict[target_df.loc[idx, "seqname"]].append((target_df.loc[idx, "start"], target_df.loc[idx, "end"], 1 if target_df.loc[idx, "strand"] == "+" else -1, target_df.loc[idx, "Orthogroup"], target_df.loc[idx, "color"]))

print(chromo_dict)

entries = {
"CM334" : [
    ("chr01", 309102287),
    ("chr02", 169555599),
    ("chr03", 282780301),
    ("chr04", 240120734),
    ("chr05", 238597879),
    ("chr06", 242241289),
    ("chr07", 251293532),
    ("chr08", 142366738),
    ("chr09", 271082670),
    ("chr10", 233321800),
    ("chr11", 266870110),
    ("chr12", 250929874)
],
"CB" : [
    ("Chr01", 259277713),
    ("Chr02", 169143200),
    ("Chr03", 297848814),
    ("Chr04", 219314553),
    ("Chr05", 227523855),
    ("Chr06", 253157891),
    ("Chr07", 254917563),
    ("Chr08", 210184557),
    ("Chr09", 196862403),
    ("Chr10", 229738584),
    ("Chr11", 263656806),
    ("Chr12", 236504799)
],
"CC" : [
    ("Chr01", 241225625),
    ("Chr02", 169927767),
    ("Chr03", 275189702),
    ("Chr04", 232151442),
    ("Chr05", 237150106),
    ("Chr06", 251477985),
    ("Chr07", 234238532),
    ("Chr08", 195914817),
    ("Chr09", 258863286),
    ("Chr10", 233440839),
    ("Chr11", 250851717),
    ("Chr12", 226401502)
]
}

max_len = max(e[1] for e in entries[genome])
telomere_length = 10000000

chr_diagram = BasicChromosome.Organism()
chr_diagram.page_size = (40 * cm, 20 * cm)

for i, (name, length) in enumerate(entries[genome]):
    cur_chromosome = BasicChromosome.Chromosome(name)
    cur_chromosome.scale_num = max_len + 2 * telomere_length

    start = BasicChromosome.TelomereSegment()
    start.scale = telomere_length
    cur_chromosome.add(start)
    
    body = BasicChromosome.AnnotatedChromosomeSegment(length, chromo_dict[name])
    body.scale = length
    cur_chromosome.add(body)

    end = BasicChromosome.TelomereSegment(inverted=True)
    end.scale = telomere_length
    cur_chromosome.add(end)

    chr_diagram.add(cur_chromosome)

chr_diagram.draw(out, "Capsicum annuum")



