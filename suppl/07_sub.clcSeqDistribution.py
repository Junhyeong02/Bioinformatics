import sys
import os
import json
from glob import glob
from multiprocessing import Process, Queue

def work(pid, read1, read2, result):
    read_dict = {}
    dis_dict = {}
   
    with open(read1) as f:
        for _ in range(13):
            print(f.readline().strip())
 
        for data in f.readlines()[:-1]:
            key = data.strip().split()[0]
            val = int(data.strip().split()[-1])
            read_dict[key] = val

    with open(read2) as f:
        for _ in range(13):
            print(f.readline().strip())

        for data in f.readlines()[:-1]:
            key = data.split()[0]
            val = int(data.split()[-1])
       
            diff = read_dict[key] - val

            if diff not in dis_dict:
                dis_dict[diff] = 0

            dis_dict[diff] += 1

    result.put((os.path.basename(os.path.commonprefix([read1, read2])), dis_dict))
    return


if __name__ == "__main__":
    path = sys.argv[1]
    
    info_dict = {}
    pair_log = []
    logs = sorted(list(glob(os.path.join(path, "*.log"))))

    for i, log in enumerate(logs):
        if i%2 == 1:
            continue

        pair_log.append((log, logs[i+1]))


    process = []
    result = Queue()
     
    for i, (r1, r2) in enumerate(pair_log):
        th = Process(target = work, args = (i, r1, r2, result))
        process.append(th)

    current_proc = []

    for p in process:
        while len(current_proc) >= 12:
            for i, cp in enumerate(current_proc):
                if not cp.is_alive():
                    current_proc.pop(i)
                    break

        p.start()
        current_proc.append(p)

    while len(current_proc) != 0:
        for i, cp in enumerate(current_proc):
            if not cp.is_alive():
                current_proc.pop(i)
                break
 
    assert all(not p.is_alive() for p in process)
    result.put("stop")

    while True:
        tmp = result.get()
        if tmp == "stop":
            break
        else:
            info_dict[tmp[0]] = tmp[1]

    with open(os.path.join(path, "SeqInfo.json"), 'w') as json_file:
        json.dump(info_dict, json_file, indent= 4, sort_keys = True)

