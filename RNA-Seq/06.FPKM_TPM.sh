# usage : python3 06_sub.FPKM_TPM.py [GTF_PATH] [OUTPUT_PATH + PRIFIX]

GTF_PATH=""
OUTPUT_PATH=""

python3 06_sub.FPKM_TPM.py $GTF_PATH $OUTPUT_PATH
# python3 06_sub.FPKM_TPM.py ../04.Mapping/Zunla-1.tissue/ ../05.FPKM_TPM/Zunla-1.tissue/Zunla-1.tissue

### history ###

# time python3 06_sub.FPKM_TPM.py ../04.Mapping/Bac.tissue/ ../05.FPKM_TPM/ *.chromosome.gtf
# time python3 06_sub.FPKM_TPM.py ../04.Mapping/Chi.tissue/ ../05.FPKM_TPM/ *.chromosome.gtf
# time python3 06_sub.FPKM_TPM.py ../04.Mapping/CM334.Mock/ ../05.FPKM_TPM/ *.CM334_0817.chromosome.gtf
# time python3 06_sub.FPKM_TPM.py ../04.Mapping/CM334.Pc/ ../05.FPKM_TPM/ *.CM334_0817.chromosome.gtf
# time python3 06_sub.FPKM_TPM.py ../04.Mapping/CM334.PepMov/ ../05.FPKM_TPM/ *.CM334_0817.chromosome.gtf
# time python3 06_sub.FPKM_TPM.py ../04.Mapping/CM334.Pi/ ../05.FPKM_TPM/ *.CM334_0817.chromosome.gtf
# time python3 06_sub.FPKM_TPM.py ../04.Mapping/CM334.tissue/ ../05.FPKM_TPM/ *.CM334_0817.chromosome.gtf
# time python3 06_sub.FPKM_TPM.py ../04.Mapping/CM334.TMV_P0/ ../05.FPKM_TPM/ *.CM334_0817.chromosome.gtf
# time python3 06_sub.FPKM_TPM.py ../04.Mapping/CM334.TMV_P2/ ../05.FPKM_TPM/ *.CM334_0817.chromosome.gtf
# time python3 06_sub.FPKM_TPM.py ../04.Mapping/ECW.PL/ ../05.FPKM_TPM/ *.ECW_0806.gtf
# time python3 06_sub.FPKM_TPM.py ../04.Mapping/Zunla-1.tissue/ ../05.FPKM_TPM/ *.Zunla-1_0806.gtf
# time python3 06_sub.FPKM_TPM.py ../04.Mapping/Heinz/ ../05.FPKM_TPM/ *.Heinz_0810.gtf

### 2021.08.23 ECW.PL L1###
# time python3 06_sub.FPKM_TPM.py ../04.Mapping/ECW.PL/ ../05.FPKM_TPM/ \*.ECW_0820.gtf
# time python3 06_sub.FPKM_TPM.py ../04.Mapping/ECW.PL/ ../05.FPKM_TPM/ \*.ECW_0806.gtf

### AVERAGE ### 

# python3 06_sub.Average.py ../SupplData/sample_group.txt ../05.FPKM_TPM/\*.MYB.FPKM.txt ../05.FPKM_TPM/\*.MYB.TPM.txt
# python3 06_sub.Average.py ../SupplData/sample_group.txt ../05.FPKM_TPM/CM334.tissue.MYB.FPKM.txt ../05.FPKM_TPM/CM334.tissue.MYB.TPM.txt

#### 2021.09.23 ###

# time python3 06_sub.FPKM_TPM.py ../04.Mapping/Bac.tissue/ ../05.FPKM_TPM/ \*.CB.MYB.ReAnnot.chromosome.sort.gtf
# time python3 06_sub.FPKM_TPM.py ../04.Mapping/Chi.tissue/ ../05.FPKM_TPM/ \*.CC.MYB.ReAnnot.chromosome.sort.gtf
# time python3 06_sub.FPKM_TPM.py ../04.Mapping/CM334.Mock/ ../05.FPKM_TPM/ \*.CaCM334.MYB.ReAnnot.chromosome.sort.gtf
# time python3 06_sub.FPKM_TPM.py ../04.Mapping/CM334.Pc/ ../05.FPKM_TPM/ \*.CaCM334.MYB.ReAnnot.chromosome.sort.gtf
# time python3 06_sub.FPKM_TPM.py ../04.Mapping/CM334.PepMov/ ../05.FPKM_TPM/ \*.CaCM334.MYB.ReAnnot.chromosome.sort.gtf
# time python3 06_sub.FPKM_TPM.py ../04.Mapping/CM334.Pi/ ../05.FPKM_TPM/ \*.CaCM334.MYB.ReAnnot.chromosome.sort.gtf
# time python3 06_sub.FPKM_TPM.py ../04.Mapping/CM334.tissue/ ../05.FPKM_TPM/ \*.CaCM334.MYB.ReAnnot.chromosome.sort.gtf
# time python3 06_sub.FPKM_TPM.py ../04.Mapping/CM334.TMV_P0/ ../05.FPKM_TPM/ \*.CaCM334.MYB.ReAnnot.chromosome.sort.gtf
# time python3 06_sub.FPKM_TPM.py ../04.Mapping/CM334.TMV_P2/ ../05.FPKM_TPM/ \*.CaCM334.MYB.ReAnnot.chromosome.sort.gtf
# time python3 06_sub.FPKM_TPM.py ../04.Mapping/ECW.PL/ ../05.FPKM_TPM/ \*.CaECW.MYB.ReAnnot.gtf
# time python3 06_sub.FPKM_TPM.py ../04.Mapping/ECW.PL.L1/ ../05.FPKM_TPM/ \*.CaECW.MYB.ReAnnot.gtf
# time python3 06_sub.FPKM_TPM.py ../04.Mapping/Heinz.tissue/ ../05.FPKM_TPM/ \*.SlHeinz.MYB.ReAnnot.gtf

# time python3 06_sub.FPKM_TPM.py ../04.Mapping/Zunla-1.tissue/ ../05.FPKM_TPM/ \*.CaZunla-1.MYB.ReAnnot.gtf
# time python3 06_sub.FPKM_TPM.py ../04.Mapping/Zunla-1.tissue/ ../05.FPKM_TPM/ \*.RefSeq_CaZunla-1.MYB.ReAnnot.gtf

# python3 06_sub.Average.py ../SupplData/sample_group.txt ../05.FPKM_TPM/\*.FPKM.txt ../05.FPKM_TPM/\*.TPM.txt

#### 2021.12.24 ####
# time python3 06_sub.FPKM_TPM.py ../04.Mapping/CM334.NaCl/ ../05.FPKM_TPM/ \*.CaCM334.MYB.ReAnnot.chromosome.sort.gtf


# time python3 06_sub.FPKM_TPM.py ../04.Mapping/CM334.NaCl/ ../05.FPKM_TPM/CM334.NaCl/CM334.NaCl.FPKM.txt ../05.FPKM_TPM/CM334.NaCl.TPM.txt
# python3 06_sub.FPKM_TPM.py ../04.Mapping/CM334.Pc/ ../05.FPKM_TPM/CM334.Pc/CM334.Pc.test
# python3 06_sub.FPKM_TPM.py ../04.Mapping/CM334.Pc/ ../05.FPKM_TPM/CM334.Pc/CM334.Pc
# python3 06_sub.FPKM_TPM.py ../04.Mapping/CM334.Pi/ ../05.FPKM_TPM/CM334.Pi/CM334.Pi
# python3 06_sub.FPKM_TPM.py ../04.Mapping/Zunla-1.tissue/ ../05.FPKM_TPM/Zunla-1.tissue/Zunla-1.tissue

