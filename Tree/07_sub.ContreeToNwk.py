import sys
import os
from glob import glob
from shutil import copyfile

filePath = sys.argv[1]

contrees = glob(os.path.join(filePath, "*.contree"))

for contree in contrees:
    copyfile(contree, contree.replace(os.path.splitext(contree)[-1], ".nwk"))







