from matplotlib import pyplot as plt

x=[1,2,3]
y= [1,2,3]

x2=[1,2,3]
y2=[2,3,4]

#plt.hold('on')
# Set x-axis range
plt.xlim((1,9))
# Set y-axis range
plt.ylim((1,9))
# Draw lines to split quadrants
plt.plot([5,5],[1,9], linewidth=4, color='red' )
plt.plot([1,9],[5,5], linewidth=4, color='red' )
plt.title('Quadrant plot')
# Draw some sub-regions in upper left quadrant
plt.plot([3,3],[5,9], linewidth=2, color='blue')
plt.plot([1,5],[7,7], linewidth=2, color='blue')

plt.plot(x,y, label='First Line')
plt.plot(x2, y2, label='second line')
plt.xlabel('Plot Number')
plt.ylabel('impirtan line')
plt.title('intresting graph')
plt.show()
