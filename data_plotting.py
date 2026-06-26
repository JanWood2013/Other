import matplotlib.pyplot as plt #"aktivates" matplotlib

x_values = [Type in x values here] #x values
y_values = [Type in y values here] #y values

plt.plot(x_values, y_values, color = "red") #the value which is called first is x // plt.plot -> line // color -> sets the color //line will be red
plt.scatter(x_values, y_values, color = "blue") #the data points in the diagram will be marked with a blue point  // plt.scatter -> only points // points will be blue

new_x_values = [Type in other x values here] #the other x values
new_y_values = [Type in other y values here] #the other y values

plt.plot(new_x_values, new_y_values, color ="green") #shows the other x and y values with a green line  
plt.scatter(new_x_values, new_y_values, color = "brown") #shows the other x and y values with brown points 

plt.title("First diagram") #shows the title at the top
plt.xlabel("x values") #label at the x axis
plt.ylabel("y Values") #label at the y axis

plt.show() #shows the diagram