import numpy as np
import matplotlib.pyplot as plt
import sys

def temperatures(): #working
    
    years = 10

    days = 365
    
    Temperatures = np.zeros(shape=(years, days))

    for i in range(years):
        for n in range(30):
            Temperatures[i, n] = np.random.randint(1,7)
        for n in range(30,60):
            Temperatures[i, n] = np.random.randint(1,10)
        for n in range(60,90):
            Temperatures[i, n] = np.random.randint(3,13)
        for n in range(90,120):
            Temperatures[i, n] = np.random.randint(6,16)
        for n in range(120,150):
            Temperatures[i, n] = np.random.randint(8,18)
        for n in range(150,180):
            Temperatures[i, n] = np.random.randint(11,21)
        for n in range(180,210):
            Temperatures[i, n] = np.random.randint(14,24)
        for n in range(210,240):
            Temperatures[i, n] = np.random.randint(17, 27)
        for n in range(240,270):
            Temperatures[i, n] = np.random.randint(20,30)
        for n in range(270,300):
            Temperatures[i, n] = np.random.randint(23,33)
        for n in range(300,330):
            Temperatures[i, n] = np.random.randint(26,36)
        for n in range(330,360):
            Temperatures[i, n] = np.random.randint(29,39)
        for n in range(360,365):
            Temperatures[i, n] = np.random.randint(32,42)
    
    return Temperatures

def average_day_temperature(): #working

    matrix = temperatures()

    average_temperatures_array = np.zeros(shape = (1, 365))
    
    for i in range(len(matrix[0, :])):
    
        summ = 0
    
        for n in range(len(matrix[:, 0])):
    
            summ += matrix[n, i]

        average = summ/len(matrix[:, 0])

        average_temperatures_array[0, i] = average
    
    return average_temperatures_array

def cloud(op=None):

    y = average_day_temperature().flatten()
    x = []

    for i in range(len(y)):
        x.append(i+1)

    if op is None:
        plt.scatter(x,y)
        plt.show()

    else:
        return x, y

def regression_line(degree_of_precision = None):
    
    x, y = cloud(True)
    x = np.array(x)

    if degree_of_precision == 1:

        [a, b] = np.polyfit(x,y,degree_of_precision)
        ymodel = a * x + b
        plt.plot(x, ymodel, 'b')

    elif degree_of_precision == 2 :

        [a, b, c] = np.polyfit(x,y,degree_of_precision)
        ymodel = a*(x**2) + b*x + c
        plt.plot(x,ymodel, 'b')
    
    elif degree_of_precision == 3 :

        [a, b, c, d] = np.polyfit(x,y,degree_of_precision)
        ymodel = a*(x**3) + b*(x**2) + c*x + d
        plt.plot(x,ymodel, 'b')
    
    else :
        print(f'Indicate a degree of precision lower than 4.\nExiting the program...')
        sys.exit(1)

    plt.scatter(x,y)
    plt.show()

def interpolation():

    x,y = cloud(True)
    x = np.array(x)

    x_interp = np.linspace(x.min(), x.max(), 20)
    y_interp = np.interp(x_interp, x, y)

    plt.plot(x,y)
    plt.plot(x_interp,y_interp, 'r')
    plt.show()

interpolation()