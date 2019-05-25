import numpy as np

x = np.arange(-6.2, 6.2, 0.1)

import matplotlib.pyplot as plt

plt.plot(x, np.sin(x))
# plt.savefig('sine.png')

print(plt.gcf().subplots().bbox)


plt.plot(x, np.sin(x))
sine_figure = plt.gcf()  # “gcf” = “get current figure”
sine_figure.savefig('sine.png')

print(sine_figure.__class__)