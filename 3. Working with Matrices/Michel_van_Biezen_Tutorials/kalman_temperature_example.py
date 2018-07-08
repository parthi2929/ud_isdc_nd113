"""
This script attempts to program and visualize the concept explained in
video tutorial from Michel van Biezen here: 
https://www.youtube.com/watch?v=PZrFFg5_Sd0&t=40s

This video is 5th part of the series

"""
import matplotlib.pyplot as plt
import numpy as np


Ttrue = 72      #True temperature = 72

#Assumptions
ESTinit = 68    #Initial Estimate = 68
Eestinit = 2    #Initial Error in Estimate = 2
MEAinit = 75    #Initial Measurement = 75
Emeainit = 4    #Error in Measurement = 4  (assumed as constant throughout)

#Measurements
MEA = [MEAinit , 71 , 70 , 74]

#Initialization
KG = []
EST = [ESTinit]
Eest = [Eestinit]

#Plotting results. You could ignore this and skip to main logic 
def plotThat():
    fig, ax1 = plt.subplots()
    t = np.arange(len(MEA)+1)
    s1 = Eest
    ax1.plot(t, s1, 'r')
    ax1.set_xlabel('measurement iteration')
    # Make the y-axis label, ticks and tick labels match the line color.
    ax1.set_xticks(t)
    ax1.set_ylim(ymin=0)
    ax1.set_ylabel('error', color='r')
    ax1.tick_params('y', colors='r')

    ax2 = ax1.twinx()
    s2 = EST
    ax2.plot(t, s2, 'b')
    ax2.set_ylim(ymax=Ttrue+1)
    ax2.set_ylabel('temperature estimate', color='b')
    ax2.axhline(y=Ttrue, color='g', linestyle='--')
    ax2.tick_params('y', colors='b')

    fig.tight_layout()
    plt.show()

"""
MAIN LOGIC FOR 1D TEMPERATURE ESTIMATION USING KALMAN FILTER
Calculations:
Kalman Gain             KG = Eest/(Eest + Emea)
Estimation              EST(t) = EST(t-1) + KG*(MEA - EST)
Error in Estimation     Eest(t) = (1 - KG)*Eest(t-1)
"""
for i in range(len(MEA)):
    KG.append(round(Eest[i]/(Eest[i] + Emeainit) , 3))
    EST.append(round(EST[-1] + KG[-1]*(MEA[i] - EST[-1]),3))
    Eest.append(round((1 - KG[-1])*Eest[-1],3))   

print('Kalman Gain over time: '+ str(KG))
print('Estimates over time: ' + str(EST))
print('Error in Estimates over time: ' + str(Eest))
plotThat()


