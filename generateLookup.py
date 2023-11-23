import csv
import sim, random
from collections import defaultdict
import json


mlcData = open("mlcPerfectestReduced.csv", "r")
# perfectDataEachJ = open("mlcPerfectestDataEachJ.csv", "w",  newline='')
# cw = csv.writer(perfectDataEachJ)
# cw.writerow(['settlingTime', 'unsettled','overshoot','overshootTime', 'crossCount', 'riseTime', 'Kp', 'Kd', 'J'])
mlcdataIterator = csv.reader(mlcData)
next(mlcdataIterator)
lookup = defaultdict(list)
for row in mlcdataIterator:
    lJ = float(row[0])
    lKp = float(row[1])
    lKd = float(row[2])
    lookup[lJ].append(tuple((lKp, lKd)))
mlcData.close()
# e.g. file = './data.json' 
with open("lookup.json", 'w') as f: 
    json.dump(lookup, f)