import matplotlib.pyplot as plt
x = [10,20,30]
y = [5,6,7]

plt.plot(x,y)
plt.show()

# x-axis values
x = [5, 2, 9, 4, 7]
# Y-axis values
y = [10, 5, 8, 4, 2]
# Function to plot
plt.plot(x, y)
# function to show the plot
plt.show()



# x-coordinates of left sides of bars
x = [1, 3, 5,7,9]
# heights of bars
y = [10, 24, 36, 40, 5]
# labels for bars
label = ['one', 'two', 'three', 'four', 'five']
# plotting a bar chart
plt.bar(x, y, tick_label=label,width=0.5, color=['green'],label="bar1")
# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('My bar chart!')
plt.legend()
# function to show the plot
plt.show()


# line 1 points
x1 = [1, 2, 3]
y1 = [2, 4, 1]
# plotting the line 1 points
plt.plot(x1, y1, label="line 1")
# line 2 points
x2 = [1, 2, 3]
y2 = [4, 1, 3]
# plotting the line 2 points
plt.plot(x2, y2, label="line 2")
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# giving a title to my graph
plt.title('Two lines on same graph!')
# show a legend on the plot
plt.legend()
# function to show the plot
plt.show()


activities = ['eat', 'sleep', 'work', 'play']
# portion covered by each label
slices = [3, 7, 8, 6]
# color for each label
colors = ['r', 'y', 'g', 'b']
# plotting the pie chart
plt.pie(slices, labels=activities, colors=colors,startangle=90, shadow=True, explode=(0, 0, 0, 0)
        ,radius=1.2, autopct='%1.1f%%')# plotting legend
plt.legend()
# showing the plot
plt.show()




