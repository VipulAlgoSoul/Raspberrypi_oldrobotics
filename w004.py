import matplotlib.pyplot as plt

import plotly.plotly as py
# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

x = [1,2,3,4]
y = [3,4,8,6]

plt.plot(x, 'o')
plt.plot(y)
fig = plt.gcf()

plot_url = py.plot_mpl(fig,line)
