# marker size (ms), marker edge color (mec) , marker face color(mfc)
import numpy as np 
import matplotlib.pyplot as plt

#marker size
x=np.array([2,5,8,10,12])
plt.plot(x,marker='o',ms=35)
plt.show()

#marker edge coor
y=np.array([8,4,16,9])
plt.plot(y,marker='o',ms=35,mec='r')
plt.show()

#marker face color
z=np.array([[12,8,18,14]])
plt.plot(z,marker='o',ms=35,mec='r',mfc='k')
plt.show()