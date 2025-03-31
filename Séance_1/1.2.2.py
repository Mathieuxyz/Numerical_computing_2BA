import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi,np.pi,100)
y = np.sin(x)

plt.plot(x, y)
plt.title('sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.text(1,0, 'Mandarine')
plt.legend('sin(x)')
plt.show()