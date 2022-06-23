import sys
import json
import os
from glob import glob

path = sys.argv[1]

files = sorted(glob(path))
# print(files)

print("name\tsample\tRead_type\tRead_length1\tRead_length2\t#Raw_reads\t#Filtered_reads")

for file_path in files:
    # print(file_path)    
    temp = file_path.split("/")
    
    sample = temp[-1].replace(".filter.fastq", "").strip(".json")
    name = temp[-2].strip()
    Read_type = temp[-3]

    with open(file_path) as f:
        try:
             json_object = json.load(f)
        except ValueError:
             print(file_path)

        Raw_reads = str(json_object["summary"]["before_filtering"]["total_reads"])
        Read_length = str(json_object["summary"]["before_filtering"]["read1_mean_length"])
        Filtered_read = str(json_object["summary"]["after_filtering"]["total_reads"])

        if Read_type == "PE":        
            Read_length2 = str(json_object["summary"]["before_filtering"]["read2_mean_length"])
            print('\t'.join([name,  sample, Read_type, Read_length, Read_length2, Raw_reads, Filtered_read]))   

        # Filtered_read = str(json_object["summary"]["after_filtering"]["total_reads"])

        # print('\t'.join([name,  sample, Read_type, Read_length, Raw_reads, Filtered_read]))   
