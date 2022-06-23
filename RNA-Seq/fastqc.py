import json
import os
import subprocess
from abc import abstractmethod

class ReadQC():
    def __init__(self, result_path:str, *, cpu:int = 1, json_log:bool, html_log:bool)->None:
        self.result_path = result_path
        self.cpu = cpu
        self.json_log = json_log
        self.html_log = html_log
        self.command = []
        self.length_cut = 0.7

    def out_file_path(self, file:str)->str:
        out_file_name = os.path.basename(file).replace(".fastq.", ".filter.fastq.")
        return os.path.join(self.result_path, out_file_name)

    def execute(self):
        pass

    @abstractmethod
    def get_command(self):
        pass

    @abstractmethod
    def forward(self):
        pass


    
class SingleEndReadQC(ReadQC):
    command     = ["fastp"]
    __input_file  = None
    __output_file = None
    
    # "fastp -i {} -o {} -l {} -q {} -w {} -h {} -j {} {}"
    
    # .format(sample, out_file, len_cut, qcut, CPU, html_file, json_file, phred)
    
    def __init__(self, result_path:str, cpu:int, json_log:bool = True, html_log:bool = True)->None:
        super().__init__(result_path, cpu = cpu, json_log = json_log, html_log = html_log)

    def set_input(self, file):
        self.__input_file = file

    def set_output(self, file):
        self.__output_file = self.out_file_path(file)

    def get_command(self):
        
        self.command.append("-i")
        self.command.append(self.__input_file)

        self.command.append("-o")
        self.command.append(self.__out_file)

        self.command.append("-l")
        self.command.append(self.length_cut)

        self.command.append("-q")
        self.command.append(self.qcut)

        self.command.append("-w")
        self.command.append(self.cpu)

        if self.html_log:

            html_log = out_file.replace(os.path.splitext(out_file)[1], ".html")
            self.command.append("-h")
            self.command.append()
        return None

    def forward(self, file:str):
        
        command = self.get_command(file, out_file)
        proc = subprocess.Popen(command, shell = True)
        return out_file  


class PairedEndReadQC(ReadQC):
    pass