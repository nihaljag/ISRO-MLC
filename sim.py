import math
import matplotlib.pyplot as plt

def main(Kp = 0.103, Kd = 0.40, J = 18000):
    PI = math.pi #PI exact
    # L = 100 #Total time = 100seconds
    dT = 0.001   #Time Interval = 0.1second
    totalTime = 100 #in seconds
    stepInputStartTime = 1 # in seconds. 
    stepInputSignalDegrees = 50 # in degrees, the input step.
    errorPercent = 2


    L = int(totalTime/dT)
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
        return(a[k] - a[k-1])/dT

    Kp = Kp * 180/PI
    Kd = Kd* 180/PI

    error[0]= 0 # 50 * PI/180
    Km = 12.25
    Tm = 0.128
    Uon = 1.0
    Uoff = -0.15
    Um = 1.0

    #J = 22000 # 10k-30k
    PlantK = 300/J

    stepInputStart = int(stepInputStartTime /dT)
    for i in range(stepInputStart,L):
        thetaRef[i] = stepInputSignalDegrees * PI/180


    for k in range (1, L):
        error[k] = thetaRef[k] - thetaFeedback[k-1]
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
        thetaFeedback[k] = intgt2[k]
        #End Plant

        #print(intgt2[k]*180/PI)

    degreeOut = [0]*L
    thetaDeg = [0]*L

    sTimeSample = 0
    sBand = errorPercent * 0.01 * stepInputSignalDegrees
    sBandNegative = stepInputSignalDegrees - sBand
    sBandPositive = stepInputSignalDegrees + sBand
    overshoot = 0

    for i in range(0,L):
        degreeOut[i] = intgt2[i]*180/PI
        overshoot = max(overshoot, degreeOut[i])
        
        thetaDeg[i] = thetaRef[i]*180/PI
        if sBandNegative< degreeOut[i] < sBandPositive:
            continue
        sTimeSample = i+1

    sT = (sTimeSample) * dT - stepInputStartTime
    
    plt.plot([i for i in range(1,L)], degreeOut[1:])
    plt.plot([i for i in range(1,L)], thetaDeg[1:])

    plt.xlabel("Time (sampling)")
    plt.ylabel("Output")
    plt.legend(['degreeOut', 'InputDeg', 'd'], loc='upper right')
    plt.text(L*0.60,0,f"J = {J}\nKp = {Kp*PI/180}*180/PI\nKd = {Kd*PI/180}*180/PI\nOvershoot = {overshoot}\nSettling time = {sT}s")
    plt.show()
    return overshoot, sT


# # Parameters
# Kp
# Kd
# J
# overshoot
# sT