import matplotlib.pyplot as plt
import numpy as np

# Define the equation parameters
a = 2
b = 3
c = 1

# Generate x values
x = np.linspace(-10, 10, 100)

# Compute y values
y = a * x**2 + b * x + c

# Plot the graph
plt.plot(x, y)

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of y = {}x^2 + {}x + {}'.format(a, b, c))

# Show the plot
plt.show()
