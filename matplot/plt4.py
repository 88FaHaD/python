'''
Markers
You can use the keyword argument marker to emphasize each point with a specified marker

'''

import numpy as np 
import matplotlib.pyplot as plt

x=np.array([2,3,6,9])
y=np.array([5,7,9,10])
plt.plot(x, marker='o')
plt.plot(y, marker='*')
plt.show()