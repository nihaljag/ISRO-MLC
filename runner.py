import time
import sim
import csv

minKp = 0.05
maxKp = 0.18
minKd = 0.2
maxKd = 0.6
minJ = 10000 
maxJ = 30000

nRowsJ = 100
nRowsKd = 20
nRowsKp = 50
start_time = time.time()

csvfile = open("mlcData100k.csv", "w",  newline='')
cw = csv.writer(csvfile)
cw.writerow(['settlingTime', 'unsettled','overshoot','overshootTime', 'crossCount', 'riseTime', 'Kp', 'Kd', 'J'])

# Varying all
lKp=lKd=lJ =0
for i in range(0,nRowsKp+1):
    lKp = minKp + ((maxKp-minKp)/nRowsKp) * i
    for j in range(0,nRowsKd+1):
        lKd = minKd + ((maxKd-minKd)/nRowsKd) * j
        for k in range(0,nRowsJ+1):
            lJ = minJ + ((maxJ-minJ)/nRowsJ) * k
            dat = sim.main(Kp=lKp, Kd = lKd, J = lJ) #= [s, u, o, oT, c, r]
            cw.writerow(dat) #WRITING TO CSV
    print(str(i*100/nRowsKp)+"% completed")

csvfile.close()
