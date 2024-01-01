import matplotlib.pyplot as plt

# Example data
categories = ['LR', 'DT', 'RF', 'MLP']
values = [0.45, 0.35, 0.1, 0.05]

# Create a bar plot
plt.bar(categories, values, color=['blue', 'green', 'red', 'purple'], hatch='/', edgecolor='black')

# Set the background of the axes to grey
plt.gca().set_facecolor('grey')

# Set the grid with white color, a specific linestyle, and linewidth
plt.grid(color='white', linestyle='-', linewidth=0.5)

# Set the y-axis limit to make the grid lines extend across the plot area
plt.ylim(0, 0.5)

# Show the plot
plt.show()
