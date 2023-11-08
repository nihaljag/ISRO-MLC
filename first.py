import math
PI = math.pi #PI exact
L = 100 #Total time = 100seconds
dT = 1   #Time Interval = 1second

thetaRef = [0]*L
thetaFeedback = [0]*L
error = [0]*L
Tc = [0]*L
R = [0]*L
P = [0]*L
Vo = [0]*L
PlantIn = [0]*L
PlantOut = [0]*L
intgt1 = [0]*L
intgt2 = [0]*L


def diff(a, k):
    return(a[k] - a[k-dT])/dT


Kp = 0.1 * 180/PI
Kd = 0.4 * 180/PI
error[0]= 50
Km = 12.25
Tm = 0.128
Uon = 1.0
Uoff = -0.15
Um = 1.0
J = 18000
PlantK = 300/J
for i in range(5,100):
    thetaRef[i] = 50


for k in range (1, L):
    error[k] = thetaRef[k] - thetaFeedback[k]
    Tc[k] = Kp * error[k] + Kd * diff(error, k)
    R[k] = Tc[k] - Vo[k]
    #Transfer Fn 1
    P[k] = (Tm/(dT+Tm))*P[k-1] + (Km*dT/(dT+Tm))*R[k]
    #Hysterisis
    if P[k] > Uon:
        Vo[k] = Um
    elif P[k] < -1*Uon:
        Vo[k] = -1*Um
    elif -Uoff < P[k] < Uoff:
        Vo[k] = 0 
    elif P[k] < Uon and P[k] > Uoff:
        if Vo[k] == Um:
            Vo[k] = Um
        else:
            Vo[k] = 0
    else:
        if Vo[k] == -Um:
            Vo[k] = -Um
        else:
            Vo[k] = 0
    #End Hysterisis
    #Actuator
    PlantIn[k] = (0.04/(dT+0.04))*PlantIn[k-1] + (1*dT/(dT+0.04))*Vo[k]
    #Plant
    PlantOut[k] = PlantIn[k]*PlantK
    intgt1[k] = intgt1[k-1] + dT*PlantOut[k]
    intgt2[k] = intgt2[k-1] + dT*intgt1[k]
    #End Plant
    radianOut = intgt2
    print(radianOut[k])