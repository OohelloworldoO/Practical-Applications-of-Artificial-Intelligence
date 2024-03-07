import numpy as np
from scipy.signal import convolve2d

image = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

filtr = np.array([[-1, -2, -1],
                  [0, 0, 0],
                  [1, 2, 1]])
