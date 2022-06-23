# python3 05_sub.FIND_MYB.py ../01.GFF/Bac_0805.txt ../TGFam/Bac.re/CB.geneIncludingMYB.fasta ../01.GFF/Bac_0819.txt
# python3 05_sub.FIND_MYB.py ../01.GFF/Chi_0805.txt ../TGFam/Chi.re/CC.geneIncludingMYB.fasta ../01.GFF/Chi_0819.txt
# python3 05_sub.FIND_MYB.py ../01.GFF/Chiltepin_0805.txt ../TGFam/Chiltepin.re/CaChil.geneIncludingMYB.fasta ../01.GFF/Chiletepin_0819.txt
# python3 05_sub.FIND_MYB.py ../01.GFF/CM334_0805.txt ../TGFam/CM334.re/CaCM334.geneIncludingMYB.fasta ../01.GFF/CM334_0819.txt
# python3 05_sub.FIND_MYB.py ../01.GFF/ECW_0805.txt ../TGFam/ECW.re/CaECW.geneIncludingMYB.fasta ../01.GFF/ECW_0819.txt
# python3 05_sub.FIND_MYB.py ../01.GFF/Heinz_0810.txt ../TGFam/Heinz.re/SlHeinz.geneIncludingMYB.fasta ../01.GFF/Heinz_0819.txt
# python3 05_sub.FIND_MYB.py ../01.GFF/SF_0805.txt ../TGFam/SF.re/CaSF.geneIncludingMYB.fasta ../01.GFF/SF_0819.txt
# python3 05_sub.FIND_MYB.py ../01.GFF/Zunla-1_0805.txt ../TGFam/Zunla-1.re/CaZunla-1.geneIncludingMYB.fasta ../01.GFF/Zunla-1_0819.txt

# mv ../01.GFF/*_0819.txt ../06.Suppl/
# grep -c "NA" ../06.Suppl/*_0819.txt

#grep -c ">" ../Combined_pep_fasta/*pep_0809.fa ../Combined_pep_fasta/Heinz_pep_0810.fa> ../06.Suppl/Reannotated_total_MYB_gene.txt
# grep -Pc ">*+MYB" ../Combined_pep_fasta/*pep_0809.fa ../Combined_pep_fasta/Heinz_pep_0810.fa> ../06.Suppl/Reannotated_MYB_gene.txt

# grep -c ">" ../TGFam/*.re/*.geneIncludingMYB.fasta > ../06.Suppl/Pre_annotated_MYB_genes.txt

# grep -c "gene" ../01.GFF/*.gff > ../06.Suppl/Reannotated_total_genes.txt

# grep -c "gene" ../TGFam/Resource/Genome_data/*.gff3 > ../06.Suppl/Pre_annotated_total_genes.txt

# python3 06_sub.OVERLAPCOUNT.py ../06.Suppl/ *_0819.txt ../06.Suppl/Overlap_info.txt

# python3 06_sub.MYB_TREE_INFO.py ../06.Suppl/FINAL_old_new_group.txt ../TGFam/Resource/Genome_data/*.tsv ../TGFam/*.re/Final/*.tsv > ../06.Suppl/ID_group_domain.txt


# python3 06_sub.DOMAIN_COUNT.py ../06.Suppl/ID_group_domain.txt > ../06.Suppl/DOMAIN_COUNT.txt


### 2021.09.28 ###
# python3 06_sub.MYB_domain_count.py ../04.PEP_FASTA/CB.MYB.total.fa ../TGFam.re/Bac/Final/*.tsv ../TGFam/Resource/Genome_data/C_baccatum.v.1.2_PEP.fa.tsv > ../06.Suppl/CB.MYB.Domain.info.csv

# python3 06_sub.MYB_domain_count.py ../04.PEP_FASTA/CaChil.MYB.total.fa ../TGFam.re/Chiltepin/Final/*.tsv ../TGFam/Resource/Genome_data/Chiltepin_v2.0_PEP.fa.tsv > ../06.Suppl/CaChil.MYB.Domain.info.csv

# python3 06_sub.MYB_domain_count.py ../04.PEP_FASTA/CaCM334.MYB.total.fa ../TGFam.re/CM334/Final/*.tsv ../TGFam/Resource/Genome_data/C_annuum.v.2.0_PEP.fa.tsv > ../06.Suppl/CaCM334.MYB.Domain.info.csv

# python3 06_sub.MYB_domain_count.py ../04.PEP_FASTA/CaECW.MYB.total.fa ../TGFam.re/ECW/Final/*.tsv ../TGFam/Resource/Genome_data/ECW.v.1.0_PEP.fa.tsv > ../06.Suppl/CaECW.MYB.Domain.info.csv

# python3 06_sub.MYB_domain_count.py ../04.PEP_FASTA/CaSF.MYB.total.fa ../TGFam.re/SF/Final/*.tsv ../TGFam/Resource/Genome_data/SF.v.1.0_PEP.fa.tsv > ../06.Suppl/CaSF.MYB.Domain.info.csv

# python3 06_sub.MYB_domain_count.py ../04.PEP_FASTA/CaZunla-1.MYB.total.fa ../TGFam.re/Zunla-1/Final/*.tsv ../TGFam/Resource/Genome_data/Zunla-1_v2.0_PEP.fa.tsv > ../06.Suppl/CaZunla-1.MYB.Domain.info.csv

# python3 06_sub.MYB_domain_count.py ../04.PEP_FASTA/CC.MYB.total.fa ../TGFam.re/Chi/Final/*.tsv ../TGFam/Resource/Genome_data/Chinense.v.1.2.PEP.fa.tsv > ../06.Suppl/CC.MYB.Domain.info.csv

# python3 06_sub.MYB_domain_count.py ../04.PEP_FASTA/RefSeq_CaZunla-1.MYB.total.fa ../TGFam.re/RefSeq.Zunla-1/Final/*.tsv ../TGFam/Resource/Genome_data/RefSeq.Zunla-1_v1.0_PEP.fa.tsv > ../06.Suppl/RefSeq_CaZunla-1.MYB.Domain.info.csv

# python3 06_sub.MYB_domain_count.py ../04.PEP_FASTA/SlHeinz.MYB.total.fa ../TGFam.re/Heinz/Final/*.tsv ../TGFam/Resource/Genome_data/Heinz.v.4.0_PEP.fa.tsv > ../06.Suppl/SlHeinz.MYB.Domain.info.csv



