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
cw.writerow(['settlingTime', 'unsettled','overshoot','overshootTime', 'crossCount', 'riseTime',  'J', 'Kp', 'Kd',])
#Settling time<99
#unsettled 0 || 1
#overshoot time < settling time
#Rise time < overshoot time
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

# if i%100 ==0:
#     [o,s,c,u,r,oT] = sim.main(Kp=lKp, Kd = lKd, J = lJ, showGraph=True)
#     print(f"Overshoot = {o}, Settling Time = {s}, J = {lJ}, Cross Count = {c}, Unsettled = {u}, Rise Time = {r}, Overshoot Time = {oT}")
#     print("--- Executed %s in %s seconds ---" %(i,time.time() - start_time))
#     start_time = time.time()
# else:
# #Varying Kp
# #Generating best Kp
# minJ = 30000
# minKp = 0.08
# maxKp = 0.09

# minO = 50
# minS = 100
# out1Kp, out2Kp = 0,0
# for i in range(0,nRows+1):

#     lKp = minKp + ((maxKp-minKp)/nRows) * i
#     lKd = minKd
#     lJ = minJ
#     if False:#i%100 ==0:
#         o,s,c,u,r,oT = sim.main(Kp=lKp, Kd = lKd, J = lJ, showGraph=True)
#         print(f"Overshoot = {o}, Settling Time = {s}, J = {lJ}, Cross Count = {c}, Unsettled = {u}, Rise Time = {r}, Overshoot Time = {oT}")
#         print("--- Executed %s in %s seconds ---" %(i,time.time() - start_time))
#         start_time = time.time()
#     else:
#         o,s,c,u,r,oT = sim.main(Kp=lKp, Kd = lKd, J = lJ)

#     if s < minS and o>0:
#         minO = o
#         minS = s
#         out2Kp = lKp
# print(out2Kp, minS, minO)

# #Varying Kd
# #Generating best Kd
# minJ = 10000
# minKp =0.11125
# minKd = 0.3
# maxKd = 0.33

# minO = 50
# minS = 100
# out2Kd = 0
# for i in range(0,nRows+1):

#     lKd = minKd + ((maxKd-minKd)/nRows) * i
#     lKp = minKp
#     lJ = minJ
#     if False:#i%100 ==0:
#         o,s,c,u,r,oT = sim.main(Kp=lKp, Kd = lKd, J = lJ, showGraph=True)
#         print(f"Overshoot = {o}, Settling Time = {s}, J = {lJ}, Cross Count = {c}, Unsettled = {u}, Rise Time = {r}, Overshoot Time = {oT}")
#         print("--- Executed %s in %s seconds ---" %(i,time.time() - start_time))
#         start_time = time.time()
#     else:
#         o,s,c,u,r,oT = sim.main(Kp=lKp, Kd = lKd, J = lJ)

#     if s < minS and o>0:
#         minO = o
#         minS = s
#         out2Kd = lKd
# print(out2Kd, minS, minO)