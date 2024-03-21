'''
Add Grid Lines to a Plot
With Pyplot, you can use the grid() function to add grid lines to the plot.

'''
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.plot(x, y)

plt.grid()

plt.show()

'''
Specify Which Grid Lines to Display
You can use the axis parameter in the grid() function to specify which grid lines to display.

Legal values are: 'x', 'y', and 'both'. Default value is 'both'.

'''
# x-axis
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.title("graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.plot(x, y)

plt.grid(axis = 'x')

plt.show()

#y-axis
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.title('garph')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(axis='y')
plt.plot(x,y)
plt.show()

'''
Set Line Properties for the GridYou can also set the line properties of the grid, like this: 
grid(color = 'color', linestyle = 'linestyle', linewidth = number).

'''
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.title('garph')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(color='black',linestyle='dashed',linewidth=0.5)
plt.plot(x,y)
plt.show()
