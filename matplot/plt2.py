# ploting without line
import numpy as np
import matplotlib.pyplot as plt

#Draw two points in the diagram, one at position (1, 3) and one in position (8, 10):

a=np.array([1,8])
b=np.array([3,10])

plt.plot(a,b,'o')
plt.show()