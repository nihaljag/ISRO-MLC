import time
import sim
import csv

minKp = 0.07
maxKp = 0.09
minKd = 0.38
maxKd = 0.5
minJ = 22000 
maxJ = 22000

nRowsJ = 1
nRowsKd = 100
nRowsKp = 100
start_time = time.time()

csvfile = open("bestPDs.csv", "w",  newline='')
cw = csv.writer(csvfile)
cw.writerow(['settlingTime', 'unsettled','overshoot','overshootTime', 'crossCount', 'riseTime', 'Kp', 'Kd', 'J'])

# Varying all
lKp=lKd=lJ =0
count = 0
minST = 120
for i in range(0,nRowsKp+1):
    lKp = minKp + ((maxKp-minKp)/nRowsKp) * i
    for j in range(0,nRowsKd+1):
        lKd = minKd + ((maxKd-minKd)/nRowsKd) * j
        for k in range(0,nRowsJ+1):
            lJ = minJ + ((maxJ-minJ)/nRowsJ) * k
            row = sim.main(Kp=lKp, Kd = lKd, J = lJ) #= [s, u, o, oT, c, r]
            if float(row[0])<minST:
                minST = float(row[0])
                print(minST, "is settling time, Kp=", lKp, "Kd=", lKd)
            #print("Kp=",lKp, "Kd=", lKd, "ST=",float(row[0]))
            if float(row[0])<12 and int(row[1])==0 and float(row[2])<4.0 and float(row[8])==22000.0:
                cw.writerow(row) #WRITING TO CSV
                count+=1
    print(str(i*100/nRowsKp)+"% completed")
print(count, "rows shortlisted")
print(minST, "is least settling time")
csvfile.close()
