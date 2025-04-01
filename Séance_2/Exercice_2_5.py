import numpy as np
import matplotlib.pyplot as plt

A = [21.4, 22.5, 24.9, 21.9, 22.1, 24.9, 25.0, 22.0, 25.1, 24.5, 23.6, 21.3, 21.5, 21.4, 24.8, 22.7, 24.2, 22.6, 22.5, 22.2, 21.8,
     24.7, 23.1, 38.0, 46.0, 49.0, 51.0, 34.0, 22.9, 22.2, 24.6, 24.0, 22.2, 23.4, 24.1, 22.0, 23.8, 23.3, 23.5, 23.0, 22.9, 21.1, 25.2,
     21.9, 24.6, 20.3, 31.0, 42.0, 41.0, 33.0, 21.1, 21.9, 22.4, 25.0, 23.4, 24.6, 24.1, 23.9, 23.7, 23.9, 23.5, 23.7, 24.8, 25.7, 24.2,
     21.9, 22.8, 24.2, 24.1, 24.9, 23.4, 23.4, 23.8, 25.4, 25.0, 24.6, 22.6, 21.6, 22.2, 23.0, 23.9, 23.9, 23.3, 24.5, 22.9, 21.9, 26.1,
     21.5, 26.6, 23.0, 24.3, 22.7, 21.4, 23.7, 23.8, 44.0, 49.0, 52.0, 31.0, 24.0, 23.3, 53.0, 52.0, 41.0, 39.0, 23.3, 21.6, 24.4, 25.5,
     23.0, 22.6, 22.0, 22.4, 20.9, 23.4, 20.9, 25.5, 24.7, 22.0, 25.9, 22.2, 22.7, 23.6, 23.4, 22.2, 22.9, 23.7, 23.3, 24.9, 22.0, 25.1,
     24.8, 25.4, 22.4, 21.0, 21.8, 24.9, 23.3, 24.9, 29.0, 45.0, 39.0, 36.0, 26.6, 22.4, 23.2, 25.0, 22.5, 25.6, 22.9, 21.5, 26.0, 24.4,
     25.0, 22.9, 24.0, 21.4, 22.9, 21.1, 21.5, 24.2, 24.4, 25.1, 24.2, 25.9, 26.6, 23.5, 23.6]



def plot_graph(Temperatures):

    x = np.arange(0,len(Temperatures),1)
    y = np.array(Temperatures)

    mean = np.mean(Temperatures)
    std = np.std(Temperatures)

    plt.plot(x,y, marker = 'o', linestyle='-', markerfacecolor='blue', markersize=2, color='blue')

    for i in range(len(Temperatures)):
        
        if Temperatures[i] > mean and (Temperatures[i]- mean) > 2 :
            plt.plot(i, Temperatures[i], markersize=8, marker="*", markerfacecolor="red", markeredgecolor="red")

    #utiliser numpy.where, mettre en évidence les points bizzares et nommer les graphiques
    plt.title('Mesure de température')
    plt.xlabel('Temps [h]')
    plt.ylabel('Température [°C]')
    plt.show()

plot_graph(A)