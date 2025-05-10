import numpy as np
import matplotlib.pyplot as plt

def three_month_avg(temperatures):

    interval = np.arange(0,13,3)

    three_month_mean = []

    for i in range(len(interval)-1):
        mean = np.mean(temperatures[interval[i]:interval[i+1]])
        for n in range(3):
            three_month_mean.append(mean)            
            
    return np.array(three_month_mean)

temperatures_2019 = np.array([5.9,7.0,7.1,12.6,14.2,17.5,17.9,20.9,16.4,11.5,9.2,5.7])
months_2019 = np.linspace(1,12,12)

mean_temperature = np.mean(temperatures_2019)
mean_temperature_x_array = np.ones(len(months_2019))*mean_temperature

three_month_mean = three_month_avg(temperatures_2019)

#creating graph
plt.scatter(months_2019, temperatures_2019, marker='*')
plt.plot(months_2019, mean_temperature_x_array, linestyle = '--', color = 'orange')
plt.plot(months_2019, three_month_mean, color = 'yellow')
plt.title('Temperatures 2019')
plt.ylabel('Temp [°C]')
plt.xlabel('Month')
plt.legend('Temp') #to modify later
plt.tight_layout()
plt.show()

