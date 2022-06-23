###########################################

DATA="/var2/Work/MS_Work/Plant_NLR_evolution/SOL_NLR_evolution/PEP/OrthoFinder/Results_Sep20/Orthologues/Orthologues_C_annuum.v.2.0_PEP"

python3 10_sub.Orthogroup.db.py ../07.Ortho/CaCM334.MYB.ReAnnot.chromosome.ko00906.txt ../07.Ortho/ko00906.ortho.txt ${DATA}/C_annuum.v.2.0_PEP__v__C_baccatum.v.1.2_PEP.tsv ${DATA}/C_annuum.v.2.0_PEP__v__Chinense.v.1.2.PEP.tsv ${DATA}/C_annuum.v.2.0_PEP__v__Zunla-1_v2.0_PEP.tsv ${DATA}/C_annuum.v.2.0_PEP__v__Heinz.v.4.0_PEP.tsv







