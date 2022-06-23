KONUMBER="/var2/Work/Myung-Shin/RNA_Seq/10.KOnumber"
GENE2TERM=".GENE2TERM.txt"
TERM2NAME=".TERM2NAME.txt"

# python 10_sub.bulidMAP2KOdb.py ../10.KOnumber/cann00001.json cann ../10.KOnumber/MAP/cann


# python 10_sub.bulidMAP2KOdb.py ../10.KOnumber/sly00001.json sly ../10.KOnumber/MAP/sly
# python 10_sub.bulidMAP2KOdb.py ../10.KOnumber/pif00001.json pif ../10.KOnumber/MAP/pif

# python 10_sub.MAPGENE.py cann00906 ../10.KOnumber/CaCM334.MYB.ReAnnot.chromosome.GENE2TERM.txt ../10.KOnumber/MAP/cann.MAP2TERM.txt ../10.KOnumber/CaCM334.MYB.ReAnnot.chromosome.TERM2NAME.txt ../10.KOnumber/CaCM334.MYB.ReAnnot.chromsoome.cann00906.txt

# python 10_sub.bulidMAP2KOdb.py ../10.KOnumber/MAP/ko00001.json ko ../10.KOnumber/MAP/ko

TARGET="ko00906"
PREFIX="SlHeinz.MYB.ReAnnot"

python 10_sub.MAPGENE.py $TARGET $KONUMBER/$PREFIX$GENE2TERM $KONUMBER/MAP/ko.MAP2TERM.txt $KONUMBER/$PREFIX$TERM2NAME $KONUMBER/${PREFIX}.${TARGET}.txt
