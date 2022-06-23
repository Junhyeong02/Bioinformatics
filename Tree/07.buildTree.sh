###	conda activate MS
#mafft --thread 40 --maxiterate 1000 --globalpair Annuum.Intact.NBARC.NoECW20R.fa > Annuum.Intact.NBARC.NoECW20R.align.fa

#trimal -in Annuum.Intact.NBARC.NoECW20R.align.fa -out Annuum.Intact.NBARC.NoECW20R.align.20.fa -gt 0.75
#iqtree -s Annuum.Intact.NBARC.NoECW20R.align.90.fa -alrt 1000 -bb 1000 -nt AUTO -safe & 

# trimal -in Annuum.Intact.NBARC.NoECW20R.align.fa -out Annuum.Intact.NBARC.NoECW20R.align.85.fa -gt 0.80
# iqtree -s Annuum.Intact.NBARC.NoECW20R.align.85.fa -alrt 1000 -bb 1000 -nt AUTO -safe &

# trimal -in Annuum.Intact.NBARC.NoECW20R.align.fa -out Annuum.Intact.NBARC.NoECW20R.align.87.fa -gt 0.85
# iqtree -s Annuum.Intact.NBARC.NoECW20R.align.87.fa -alrt 1000 -bb 1000 -nt AUTO -safe &

# trimal -in Annuum.Intact.NBARC.NoECW20R.align.fa -out Annuum.Intact.NBARC.NoECW20R.align.92.fa -gt 0.90
# iqtree -s Annuum.Intact.NBARC.NoECW20R.align.92.fa -alrt 1000 -bb 1000 -nt AUTO -safe &

###	conda activate MS    ###
# mafft --thread 30 --maxiterate 1000 --globalpair --anysymbol ../05.TREE/Total.R2R3_MYB.fa > ../05.TREE/phylo/R2R3_MYB.align.fa

# trimal -in /var2/Work/Kong_Junhyeong/05.TREE/phylo/R2R3_MYB.align.fa -out /var2/Work/Kong_Junhyeong/05.TREE/phylo/R2R3_MYB.align.50.fa -gt 0.50
# iqtree -s /var2/Work/Kong_Junhyeong/05.TREE/phylo/R2R3_MYB.align.50.fa -alrt 1000 -bb 1000 -nt AUTO -safe &

# trimal -in /var2/Work/Kong_Junhyeong/05.TREE/phylo/R2R3_MYB.align.fa -out /var2/Work/Kong_Junhyeong/05.TREE/phylo/R2R3_MYB.align.45.fa -gt 0.55
# iqtree -s /var2/Work/Kong_Junhyeong/05.TREE/phylo/R2R3_MYB.align.45.fa -alrt 1000 -bb 1000 -nt AUTO -safe &

# trimal -in /var2/Work/Kong_Junhyeong/05.TREE/phylo/R2R3_MYB.align.fa -out /var2/Work/Kong_Junhyeong/05.TREE/phylo/R2R3_MYB.align.40.fa -gt 0.60
# iqtree -s /var2/Work/Kong_Junhyeong/05.TREE/phylo/R2R3_MYB.align.40.fa -alrt 1000 -bb 1000 -nt AUTO -safe &

# trimal -in /var2/Work/Kong_Junhyeong/05.TREE/phylo/R2R3_MYB.align.fa -out /var2/Work/Kong_Junhyeong/05.TREE/phylo/R2R3_MYB.align.35.fa -gt 0.65
# iqtree -s /var2/Work/Kong_Junhyeong/05.TREE/phylo/R2R3_MYB.align.35.fa -alrt 1000 -bb 1000 -nt AUTO -safe &


#### 

# trimal -in /var2/Work/Kong_Junhyeong/05.TREE/phylo/R2R3_MYB.align.fa -out /var2/Work/Kong_Junhyeong/05.TREE/phylo/R2R3_MYB.align.30.fa -gt 0.70
# iqtree -s /var2/Work/Kong_Junhyeong/05.TREE/phylo/R2R3_MYB.align.30.fa -alrt 1000 -bb 1000 -nt AUTO -safe &

# trimal -in /var2/Work/Kong_Junhyeong/05.TREE/phylo/R2R3_MYB.align.fa -out /var2/Work/Kong_Junhyeong/05.TREE/phylo/R2R3_MYB.align.25.fa -gt 0.75
# iqtree -s /var2/Work/Kong_Junhyeong/05.TREE/phylo/R2R3_MYB.align.25.fa -alrt 1000 -bb 1000 -nt AUTO -safe &

# trimal -in /var2/Work/Kong_Junhyeong/05.TREE/phylo/R2R3_MYB.align.fa -out /var2/Work/Kong_Junhyeong/05.TREE/phylo/R2R3_MYB.align.20.fa -gt 0.80
# iqtree -s /var2/Work/Kong_Junhyeong/05.TREE/phylo/R2R3_MYB.align.20.fa -alrt 1000 -bb 1000 -nt AUTO -safe &

# trimal -in /var2/Work/Kong_Junhyeong/05.TREE/phylo/R2R3_MYB.align.fa -out /var2/Work/Kong_Junhyeong/05.TREE/phylo/R2R3_MYB.align.15.fa -gt 0.85
# iqtree -s /var2/Work/Kong_Junhyeong/05.TREE/phylo/R2R3_MYB.align.15.fa -alrt 1000 -bb 1000 -nt AUTO -safe &

# trimal -in /var2/Work/Kong_Junhyeong/05.TREE/phylo/R2R3_MYB.align.fa -out /var2/Work/Kong_Junhyeong/05.TREE/phylo/R2R3_MYB.align.10.fa -gt 0.90
# iqtree -s /var2/Work/Kong_Junhyeong/05.TREE/phylo/R2R3_MYB.align.10.fa -alrt 1000 -bb 1000 -nt AUTO -safe &

# mafft --thread 20 --maxiterate 1000 --globalpair --anysymbol ../05.TREE/Total.R2R3_MYB.fa > ../05.TREE/phylo.re/R2R3_MYB.align.fa
# trimal -in /var2/Work/Kong_Junhyeong/05.TREE/phylo.re/R2R3_MYB.align.fa -out /var2/Work/Kong_Junhyeong/05.TREE/phylo.re/R2R3_MYB.align.15.fa -gt 0.85
# iqtree -s /var2/Work/Kong_Junhyeong/05.TREE/phylo.re2/R2R3_MYB.align.15.fa -alrt 1000 -bb 1000 -nt AUTO -safe

# python3 07_sub.ContreeToNwk.py ../05.TREE/phylo.re/
# python3 07_sub.SubgroupAssign.py ../05.TREE/Subgroup_MYB.txt ../05.TREE/phylo.re/R2R3_MYB.align.15.fa.nwk ../05.TREE/phylo.re/R2R3_MYB.align.15.fa.assign.nwk

# mafft --thread 20 --maxiterate 1000 --globalpair --anysymbol ../05.TREE/PF13921/PF13921_PEP.fa > ../05.TREE/PF13921/phylo/PF13921.align.fa

# trimal -in /var2/Work/Kong_Junhyeong/05.TREE/PF13921/phylo/PF13921.align.fa -out /var2/Work/Kong_Junhyeong/05.TREE/PF13921/phylo/PF13921.align.15.fa -gt 0.85
# iqtree -s /var2/Work/Kong_Junhyeong/05.TREE/PF13921/phylo/PF13921.align.15.fa -alrt 1000 -bb 1000 -nt AUTO -safe -redo
# python3 07_sub.ContreeToNwk.py ../05.TREE/PF13921/phylo/


# python3 07_sub.TissueAssign.py ../05.TREE/MYB_tissue.txt ../05.TREE/phylo.re/R2R3_MYB.align.15.fa.nwk ../05.TREE/phylo.re/R2R3_MYB.align.15.fa.tissue.assign.nwk

# python3 07_sub.ContreeToNwk.py ../05.TREE/phylo.re2/
# python3 07_sub.SubgroupAssign.py ../05.TREE/Subgroup_MYB.txt ../05.TREE/phylo.re2/R2R3_MYB.align.15.fa.nwk ../05.TREE/phylo.re2/R2R3_MYB.align.15.fa.assign.nwk


# mafft --thread 20 --maxiterate 1000 --globalpair --anysymbol ../05.TREE/Total.MYB_related.fa > ../05.TREE/MYB_related/Total.MYB_related.align.fa
# trimal -in /var2/Work/Kong_Junhyeong/05.TREE/MYB_related/Total.MYB_related.align.fa -out /var2/Work/Kong_Junhyeong/05.TREE/MYB_related/Total.MYB_related.align.15.fa -gt 0.85
# iqtree -s /var2/Work/Kong_Junhyeong/05.TREE/MYB_related/Total.MYB_related.align.15.fa -alrt 1000 -bb 1000 -nt AUTO -safe

# python3 07_sub.ContreeToNwk.py ../05.TREE/MYB_related/

# trimal -in /var2/Work/Kong_Junhyeong/05.TREE/MYB_related/Total.MYB_related.align.fa -out /var2/Work/Kong_Junhyeong/05.TREE/MYB_related/Total.MYB_related.align.35.fa -gt 0.65
# iqtree -s /var2/Work/Kong_Junhyeong/05.TREE/MYB_related/Total.MYB_related.align.35.fa -alrt 1000 -bb 1000 -nt AUTO -safe &

# trimal -in /var2/Work/Kong_Junhyeong/05.TREE/MYB_related/Total.MYB_related.align.fa -out /var2/Work/Kong_Junhyeong/05.TREE/MYB_related/Total.MYB_related.align.30.fa -gt 0.70
# iqtree -s /var2/Work/Kong_Junhyeong/05.TREE/MYB_related/Total.MYB_related.align.30.fa -alrt 1000 -bb 1000 -nt AUTO -safe &

# trimal -in /var2/Work/Kong_Junhyeong/05.TREE/MYB_related/Total.MYB_related.align.fa -out /var2/Work/Kong_Junhyeong/05.TREE/MYB_related/Total.MYB_related.align.25.fa -gt 0.75
# iqtree -s /var2/Work/Kong_Junhyeong/05.TREE/MYB_related/Total.MYB_related.align.25.fa -alrt 1000 -bb 1000 -nt AUTO -safe &

# trimal -in /var2/Work/Kong_Junhyeong/05.TREE/MYB_related/Total.MYB_related.align.fa -out /var2/Work/Kong_Junhyeong/05.TREE/MYB_related/Total.MYB_related.align.20.fa -gt 0.80
# iqtree -s /var2/Work/Kong_Junhyeong/05.TREE/MYB_related/Total.MYB_related.align.20.fa -alrt 1000 -bb 1000 -nt AUTO -safe &


# python3 07_sub.ContreeToNwk.py ../05.TREE/MYB_related/



mafft --thread 20 --maxiterate 1000 --globalpair --anysymbol ../05.TREE/Reference/run.fasta > ../05.TREE/Reference/run.align.fa
trimal -in /var2/Work/Kong_Junhyeong/05.TREE/Reference/run.align.fa -out /var2/Work/Kong_Junhyeong/05.TREE/Reference/run.align.35.fa -gt 0.65
iqtree -s /var2/Work/Kong_Junhyeong/05.TREE/Reference/run.align.35.fa -alrt 1000 -bb 1000 -nt AUTO -safe






































