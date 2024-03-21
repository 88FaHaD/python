# Matplotlib is a low level graph plotting library in python that serves as a visualization utility.
import numpy as np
import matplotlib.pyplot as plt

# Draw a line in a diagram from position (0,0) to position (6,250):
x=np.array([0,6])
y=np.array([0,250])

plt.plot(x,y)
plt.show()

# Draw a line in a diagram from position (1, 3) to position (8, 10):
a=np.array([1,8])
b=np.array([3,10])
plt.plot(a,b)
plt.show()