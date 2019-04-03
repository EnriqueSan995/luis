import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.1)
y = x*np.cos(x)

plt.plot(x,y)
plt.xlabel('x,2e')
plt.ylabel('y,w')
plt.title('Lab DLS "prueva"')
plt.show()
