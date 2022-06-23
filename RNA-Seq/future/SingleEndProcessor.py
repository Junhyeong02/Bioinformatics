import subprocess


class SingleEndProcessor():
    __QUALIFIED_QUALITY:int
    __LENGTH_LIMIT:int
    __CPU:int
    __DEFAULT_COMMAND:str = "fastp -i {} -o {} -l {} -q {} -w {} -h {} -j {} {}"

    def __init__(self, qualified_quality, length_limit, cpu):
        self.__QUALIFIED_QUALITY = qualified_quality
        self.__LENGTH_LIMIT = length_limit
        self.__CPU = cpu

    def get_command(self):
        return self.__DEFAULT_COMMAND.format(self.__QUALIFIED_QUALITY, self.__LENGTH_LIMIT, self.__CPU)

    def process(self, input_fastq, output_fastq):
        subprocess.Popen(self.get_command, shell=True)