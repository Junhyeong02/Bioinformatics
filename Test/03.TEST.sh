# time python3 TGFam_Resource_test.py Bac_0805.chromosome.sort.gff3 


### 2021.09.13 ###
# time python3 03_sub2.TEST.py ../TGFam.re/Bac/Final/CB_MYB.TGFam.gff3 ../TGFam/Resource/Genome_data/C_baccatum.v.1.2_genomic.fasta ../TGFam.re/Bac/Final/CB_MYB.TGFam.CDS.fa ../TGFam.re/Bac/Final/CB_MYB.TGFam.PEP.fa C_ba.re

# time python3 03_sub2.TEST.py ../TGFam.re/Chi/Final/CC_MYB.TGFam.gff3 ../TGFam/Resource/Genome_data/Chinense.v.1.2_genomic.fasta ../TGFam.re/Chi/Final/CC_MYB.TGFam.CDS.fa ../TGFam.re/Chi/Final/CC_MYB.TGFam.PEP.fa C_chi.re

# time python3 03_sub2.TEST.py ../TGFam.re/Chiltepin/Final/CaChil_MYB.TGFam.gff3 ../TGFam/Resource/Genome_data/Chiltepin_v2.0_genomic.fasta ../TGFam.re/Chiltepin/Final/CaChil_MYB.TGFam.CDS.fa ../TGFam.re/Chiltepin/Final/CaChil_MYB.TGFam.PEP.fa CaChil.re

# time python3 03_sub2.TEST.py ../TGFam.re/CM334/Final/CaCM334_MYB.TGFam.gff3 ../TGFam/Resource/Genome_data/C_annuum.v.2.0_genomic.fasta ../TGFam.re/CM334/Final/CaCM334_MYB.TGFam.CDS.fa ../TGFam.re/CM334/Final/CaCM334_MYB.TGFam.PEP.fa CaCM334.re

# time python3 03_sub2.TEST.py ../TGFam.re/ECW/Final/CaECW_MYB.TGFam.gff3 ../TGFam/Resource/Genome_data/ECW.v.1.0_genomic.fasta ../TGFam.re/ECW/Final/CaECW_MYB.TGFam.CDS.fa ../TGFam.re/ECW/Final/CaECW_MYB.TGFam.PEP.fa CaECW.re

# time python3 03_sub2.TEST.py ../TGFam.re/Heinz/Final/SlHeinz_MYB.TGFam.gff3 ../TGFam/Resource/Genome_data/Heinz.v.4.0_genomic.fasta ../TGFam.re/Heinz/Final/SlHeinz_MYB.TGFam.CDS.fa ../TGFam.re/Heinz/Final/SlHeinz_MYB.TGFam.PEP.fa SlHeinz.re

# time python3 03_sub2.TEST.py ../TGFam.re/RefSeq.Zunla-1/Final/RefSeq_CaZunla-1_MYB.TGFam.gff3 ../TGFam/Resource/Genome_data/RefSeq.Zunla-1_v1.0_genomic.fa ../TGFam.re/RefSeq.Zunla-1/Final/RefSeq_CaZunla-1_MYB.TGFam.CDS.fa ../TGFam.re/RefSeq.Zunla-1/Final/RefSeq.CaZunla-1_MYB.TGFam.PEP.fa RefSeq.CaZunla-1.re

# time python3 03_sub2.TEST.py ../TGFam.re/SF/Final/CaSF_MYB.TGFam.gff3 ../TGFam/Resource/Genome_data/SF.v.1.0_genomic.fasta ../TGFam.re/SF/Final/CaSF_MYB.TGFam.CDS.fa ../TGFam.re/SF/Final/CaSF_MYB.TGFam.PEP.fa CaSF.re

# time python3 03_sub2.TEST.py ../TGFam.re/Zunla-1/Final/CaZunla-1_MYB.TGFam.gff3 ../TGFam/Resource/Genome_data/Zunla-1_v2.0_genomic.fasta ../TGFam.re/Zunla-1/Final/CaZunla-1_MYB.TGFam.CDS.fa ../TGFam.re/Zunla-1/Final/CaZunla-1_MYB.TGFam.PEP.fa CaZunla-1.re

### 2021.09.14 ###

# time python3 03_sub2.TEST.py ../01.GFF/CaCM334.MYB.ReAnnot.chromosome.sort.gff3 ../TGFam/Resource/Genome_data/C_annuum.v.2.0_genomic.fasta ../01.GFF/CaCM334.MYB.ReAnnot.chromosome.CDS.fa ../TGFam.re/CM334/Final/CaCM334_MYB.TGFam.PEP.fa CaCM334.chr.re

# python3 03_sub3.CDS.match.py ../01.GFF/CaCM334.MYB.ReAnnot.chromosome.CDS.fa ../TGFam/Resource/Genome_data/C_annuum.v.2.0_CDS.fa > result/CaCM334.CDS.test.result.fa 

python3 03_sub3.CDS.match.py ../TGFam/Resource/Genome_data/C_annuum.v.2.0_CDS.fa ../01.GFF/CaCM334.MYB.ReAnnot.chromosome.CDS.fa  > result/CaCM334.CDS.test.result2.fa 
