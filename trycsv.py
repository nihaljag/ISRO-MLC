import csv
import time
#Settling time<99
#unsettled 0 || 1
#overshoot time < settling time
#Rise time < overshoot time

csvfile = open("test.csv", "w")

cw = csv.writer(csvfile)
start_time = time.time()
for i in range(10000):
    cw.writerow([1,2,3,4,5,6,7,8,9])
print("--- Executed in %s seconds ---" %(time.time() - start_time))
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