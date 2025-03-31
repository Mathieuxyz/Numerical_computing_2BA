import numpy as np

def temperatures():
    
    years = 10
    
    days = 365
    
    Temperatures = np.zeros(shape=(years, days))

    for i in range(years):
        for n in range(days):
            Temperatures[i, n] = np.random.randint(1,30)
    
    return Temperatures

print(temperatures())