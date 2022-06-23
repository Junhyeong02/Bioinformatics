##### 2021.08.20 #####

#grep "overall alignment rate" ../04.Mapping/*.*/*.log ../04.Mapping/Heinz/*.log > ../SupplData/alignment_rate.txt
# alingment_rate.txt %s/Heinz/Heinz.tissue/g
# python3 07_sub.Mapping_rate.py ../SupplData/alignment_rate.txt ../SupplData/alignment_rate_total.txt
# python3 07_sub.READ_info.py ../01.Preprocessed_data/\*E/\*/\*.json ../01.Preprocessed_data/PE/ECW.PL/NoUse/\*.json > ../SupplData/READ_info.txt
# cp ../04.Mapping/*.*/*.log ../04.Mapping/Heinz/*.log ../TEST/04.Mapping/
# python3 07_sub.Mapping_info.py ../04.Mapping/\*/\*.log > ../SupplData/MAPPING_INFO.txt
# python3 07_sub.Table.py ../SupplData/READ_info.txt ../SupplData/MAPPING_INFO.txt > ../SupplData/TABLE.txt



##### use this #### 

# python3 07_sub.Mapping_info.py ../04.Mapping/\*/\*.log # > ../SupplData/MAPPING_INFO.txt


# python3 07_sub.READ_info.py ../01.Preprocessed_data/\*E/\*/\*.json  > ../SupplData/READ_INFO.txt

# python3 07_sub.Table.py ../SupplData/READ_INFO.txt ../SupplData/MAPPING_INFO.txt ../SupplData/Total.txt

# python 07_sub.dropLowQualityData.py ../SupplData/Total.txt ../05.FPKM_TPM/

# python3 07_sub.READ_info.py ../01.Preprocessed_data/PE/PcPi/\*.json > ../SupplData/PcPi_READ_INFO.txt
# python3 07_sub.READ_info.py ../01.Preprocessed_data/PE/CM334.NaCl/\*.json  # > ../SupplData/READ_INFO.txt


# python 07_sub.clcReadInfo.py ../00.Raw_data/PE/PcPi/\*.fastq.gz ../01.Preprocessed_data/PE/PcPi/\*.filter.fastq.gz ../SupplData/PcPi/
# python 07_sub.clcDataParsing.py ../SupplData/PcPi/


# python 07_sub.clcReadInfo.py ../00.Raw_data/PE/CM334.NaCl/\*.fastq.gz ../01.Preprocessed_data/PE/CM334.NaCl/\*.filter.fastq.gz ../SupplData/NaCl/
# python 07_sub.clcDataParsing.py ../SupplData/NaCl/



# python 07_sub.clcReadInfo.py ../00.Raw_data/PE/PcPi/\*.fastq.gz ../01.Preprocessed_data/PE/PcPi_51/\*.filter.fastq.gz ../SupplData/PcPi_51/
# python 07_sub.clcDataParsing.py ../SupplData/PcPi_51/


# python 07_sub.clcReadInfo.py ../00.Raw_data/PE/CM334.Pc/\*.fastq.gz ../01.Preprocessed_data/PE/CM334.Pc/\*.filter.fq.gz ../SupplData/CM334.Pc/
# python 07_sub.clcDataParsing.py ../SupplData/CM334.Pc/

# python 07_sub.clcReadInfo.py ../00.Raw_data/PE/PcPi/\*.fastq.gz ../01.Preprocessed_data/PE/PcPi_30_51/\*.filter.fastq.gz ../SupplData/PcPi_30_51/
# python 07_sub.clcDataParsing.py ../SupplData/PcPi_30_51/

# python 07_sub.clcReadInfo.py ../00.Raw_data/PE/PcPi/\*.fastq.gz ../01.Preprocessed_data/PE/PcPi_30_71/\*.filter.fastq.gz ../SupplData/PcPi_30_71/
# python 07_sub.clcDataParsing.py ../SupplData/PcPi_30_71/

# python 07_sub.clcSeqDistribution.py ../01.Preprocessed_data/PE/CM334.NaCl/SRR8692579_1.filter.fastq.log ../01.Preprocessed_data/PE/cCM334.NaCl/SRR8692579_2.filter.fastq.log

# python 07_sub.clcSeqDetail.py ../01.Preprocessed_data/PE/PcPi_30_71/
python 07_sub.clcSeqDistribution.py ../01.Preprocessed_data/PE/PcPi_30_71/








