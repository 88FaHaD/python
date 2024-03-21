'''
Create Labels for a Plot
With Pyplot, you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis.

'''

import numpy as np
import matplotlib.pyplot as plt

a=np.array([3,8,1,10])
plt.plot(a)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()

'''
Create a Title for a Plot
With Pyplot, you can use the title() function to set a title for the plot.

'''

b=np.array([3,8,1,10])
plt.plot(b)
plt.title('graphplot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()

'''
Set Font Properties for Title and Labels
You can use the fontdict parameter in xlabel(), ylabel(), and title() to set font properties for the title and labels.  

'''
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1={'family':'serif','color':'black','size':30}
font2={'family':'serif','color':'blue','size':10}

plt.plot(x,y)
plt.title('GRAPH',fontdict=font1)
plt.xlabel('x-axis',fontdict=font2)
plt.ylabel('y-axis',fontdict=font2)
plt.show()

'''
Position the Title
You can use the loc parameter in title() to position the title.

Legal values are: 'left', 'right', and 'center'. Default value is 'center'.

'''
plt.plot(x,y)
plt.title('GRAPH',fontdict=font1,loc='left')
plt.xlabel('x-axis',fontdict=font2)
plt.ylabel('y-axis',fontdict=font2)
plt.show()