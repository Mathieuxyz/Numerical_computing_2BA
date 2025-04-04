import numpy as np 
import matplotlib.pyplot as plt
#considérons que le radar se trouve à 50 m de la route et détecte à 100m en horizontal de lui

frequency = 1*(10**9) #Hz
car_speed = 120/3.6

def emmiting_signal():
    x = np.arange(-0.05, 0.05, np.pi/2000)
    y = np.sin(2*np.pi*frequency*x)

    return x, y

def lambda_():

    return 3*(10**8)/frequency

def alpha(x:int, y:int):
    distance_route_x = x
    distance_route_y = y
    alpha = np.atan(distance_route_y/distance_route_x)

    return alpha

def receiving_frequency():

    alpha_ = alpha(100, 50)
    wavelenght = lambda_()

    delta_f = 2*car_speed*np.cos(alpha_)/wavelenght
    return frequency + delta_f

def receiving_signal():

    x, y = emmiting_signal()
    f2 = receiving_frequency()
    y2 = np.sin(2*np.pi*f2*x)

    return x, y, y2

def show_speed():
    x,y,y2 = receiving_signal()

    plt.plot(x,y, color = 'blue')
    plt.plot(x,y2, color ='red')
    plt.show()

def frequency_addition():

    x,y,y2 = receiving_signal()

    summed_y = y + y2
    
    plt.plot(x,summed_y, color = 'green')
    plt.title('Summed signals')
    plt.show()


frequency_addition()

    
    




