import sys

DATA_PATH = sys.argv[1]

print("#", DATA_PATH)
print("# Group\t1\t2\t3\t4\t0\tNA\tothers") 

GROUP_COUNT_INFO = dict()

with open(DATA_PATH) as f:
	for line in f.readlines():
		if line[0] =="#":
			continue

		data = line.strip().split("\t")

		group, domain = data[2], data[3]

		if group not in GROUP_COUNT_INFO:
			GROUP_COUNT_INFO[group] = [0,0,0,0,0,0,0]

		if domain == "1":
			GROUP_COUNT_INFO[group][0] += 1

		elif domain == "2":
			GROUP_COUNT_INFO[group][1] += 1

		elif domain == "3":
			GROUP_COUNT_INFO[group][2] += 1

		elif domain == "4":
			GROUP_COUNT_INFO[group][3] += 1

		elif domain == "0":
			GROUP_COUNT_INFO[group][4] += 1

		elif domain == "NA":
			GROUP_COUNT_INFO[group][5] += 1

		else:
			GROUP_COUNT_INFO[group][6] += 1


order = sorted([key for key in GROUP_COUNT_INFO.keys() if key[0] == "C"], key = lambda x: int(x[1:]))\
		 + sorted([key for key in GROUP_COUNT_INFO.keys() if key[0] == "G"], key = lambda x:int(x[1:])) \
		 + sorted([key for key in GROUP_COUNT_INFO.keys() if key[0] != "C" and key[0] != "G"])

for key in order:
	print(str(key) + "\t" + '\t'.join(map(str, GROUP_COUNT_INFO[key])))
