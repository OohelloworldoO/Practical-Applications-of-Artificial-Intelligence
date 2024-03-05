from matplotlib import pyplot as plt


import numpy as np




x = np.linspace(1, 10, 20)


print(x)


y = 3 * x + 2


fig = plt.figure()


axes = fig.add_axes([0.1, 0.1, 0.9, 0.9])


axes.plot(x, y, 'r')




plt.show()