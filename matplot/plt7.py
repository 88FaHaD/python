'''
Linestyle
You can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line

Line Color
You can use the keyword argument color or the shorter c to set the color of the line

Line width
You can use the keyword argument linewidth or the shorter lw to change the width of the line.
'''

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, linestyle = 'dotted')
plt.show()

ypoints=np.array([3,8,1,10])
plt.plot(ypoints,color='k')
plt.show()

zpoints=np.array([3,8,1,10])
plt.plot(zpoints,color='k',lw=30)
plt.show()

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()