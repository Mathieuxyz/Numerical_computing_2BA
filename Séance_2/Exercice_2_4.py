import numpy as np
import matplotlib.pyplot as plt

def temperatures(): #working
    
    years = 10
    
    days = 365
    
    Temperatures = np.zeros(shape=(years, days))

    for i in range(years):
        for n in range(days):
            Temperatures[i, n] = np.random.randint(1,30)
    
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

def cloud():

    y = average_day_temperature()
    x = []

    for i in range(len(y[0, :])):
        x.append(i+1)

    plt.scatter(x,y)
    plt.show()

cloud()