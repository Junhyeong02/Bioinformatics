### 2021.09.06 ###

# python3 00_sub.FIND_motif.py ../TGFam/Resource/Genome_data/\*PEP.fa ../TGFam/Resource/Genome_data/\*PEP.fa.tsv

# Interproscan

# /var2/Work/MS_Work/InterProScan/interproscan-5.48-83.0/interproscan.sh -i GCF_000710875.1_Pepper_Zunla_1_Ref_v1.0_protein.faa -appl Pfam -cpu 20


# python3 00_sub.FIND_motif.py ../TGFam/Resource/Genome_data/GCF_000710875.1_Pepper_Zunla_1_Ref_v1.0_protein.faa ../TGFam/Resource/Genome_data/GCF_000710875.1_Pepper_Zunla_1_Ref_v1.0_protein.faa.tsv

# cat *.fa > MYB.TGFam.fa

python3 00_sub.GetSeq.py ../05.TREE/PF13921/PF13921_list.txt ../TGFam/Resource/Genome_data/\*PEP.fa > ../05.TREE/PF13921/PF13921_PEP.fa
# python3 00_sub.GetSeq.py ../05.TREE/MYB_ba_list.txt ../TGFam/Resource/Genome_data/\*PEP.fa > ../05.TREE/MYB_ba_PEP.fa
