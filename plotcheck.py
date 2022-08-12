import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py

plt.figure()
plt.axis([0,10,0,3])
for i in range(10):
    y = np.random.random()
    plt.plot(i, y,'*')
    plt.pause(0.5)

plt.show()
