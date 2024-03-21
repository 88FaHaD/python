# doted and colored line
'''

Line Syntax	   Description
'-'	           Solid line	
':'	           Dotted line	
'--'	       Dashed line	
'-.'	       Dashed/dotted line

'''
import numpy as np
import matplotlib.pyplot as plt


x=np.array([2,8,10,12])
plt.plot(x,'o:r')
plt.show()

y=np.array([3,5,9,15])
plt.plot(y,'*-.b')
plt.show()

z=np.array([2,4,6,8,10,12,14])
plt.plot(z,'X--g')
plt.show()

a=np.array([2,4,7,9,10,12,14])
plt.plot(a,'o-k')
plt.show()