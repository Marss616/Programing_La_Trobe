import matplotlib.pyplot as plt
import numpy as np

# Define the equations
# x + y = 17 => y = 17 - x
def equation1(x):
    return 17 - x

# (4/3)x - 20 = -y => y = -((4/3)x - 20) => y = (4/3)x - 20
def equation2(x):
    return (4/3) * x - 20

# Create an array of x values
x_values = np.linspace(0, 25, 400)

# Plot the first equation
plt.plot(x_values, equation1(x_values), label='x + y = 17')

# Plot the second equation
plt.plot(x_values, equation2(x_values), label='(4/3)x - 20 = -y')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Equations Plot')
plt.legend()

# Set the limit for the axes
plt.xlim(0, 25)
plt.ylim(-5, 25)

# Save the plot to a file
plt.grid(True)
file_path = '/mnt/data/linear_equations_plot.png'
plt.savefig(file_path)
plt.close()

file_path
