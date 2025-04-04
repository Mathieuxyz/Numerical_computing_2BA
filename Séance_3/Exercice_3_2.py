import numpy as np
import matplotlib.pyplot as plt 

Vini = float(input('Initial speed (m/s) ? : '))
alpha = float(input('Angle of shooting (°) ? : '))
alpha = np.radians(alpha)
dt = 0.13 #s/tic

g = 9.81

def initial_conditions(Vini: float, alpha: float): #working with (x, y, z=0)
    A0 = np.array([0, -g])
    B0 = np.array([Vini*np.cos(alpha), Vini*np.sin(alpha)])
    P0 = np.array([0,0])

    return A0, B0, P0

def position():

    A0, B0, P0 = initial_conditions(Vini, alpha)

    t = 0
    

    while True:
        t += dt
        P = (P0) + (B0 * t) + (0.5 * A0 * (t**2))
        if 99 <= P[1] <= 101 and 0 <= P[1] <= 200 :
            plt.plot(P[0], P[1], marker = '*', color = 'red', markersize = 15)
            break
        elif P[1] < 0 :
            plt.plot(P[0], P[1], marker = '*', color = 'red', markersize = 15)
            break
        else:
            plt.plot(P[0], P[1], marker = 'o', color = 'green')
            plt.pause(0.05) #indispensable si on souhaite que les points s'affichent harmonieusement l'un à la suite de l'autre
    
    plt.xlim(-10,130)
    plt.ylim(-10, 300)
    plt.xlabel('Position x')
    plt.ylabel('Postion y')
    plt.title('Simulation tir de bouboule')
    plt.legend()
    plt.show()

position()

