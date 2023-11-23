import csv

mlcData = open("mlcPerfectestDataEachJ.csv", "r")
perfectDataEachJ = open("mlcPerfectestReduced.csv", "w",  newline='')
cw = csv.writer(perfectDataEachJ)
cw.writerow([ 'J', 'Kp', 'Kd'])


mlcdataIterator = csv.reader(mlcData)
column_names = next(mlcdataIterator)
count = 0

data = [_ for _ in mlcdataIterator]
prev = {'J':float(data[0][8]), 'Kp': float(data[0][6]), 'Kd': float(data[0][7])}
for row in data[1:]:
    curr = {'J':float(row[8]), 'Kp': float(row[6]), 'Kd': float(row[7])}
    if prev['J']==curr['J']:
        if prev['Kp']==curr['Kp'] or prev['Kd']==curr['Kd']:
            print("Deleted row")
            continue 
    dat = [row[8], row[6], row[7]]
    cw.writerow(dat)
    count+=1
    prev = curr


print(count)