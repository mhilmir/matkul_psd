import matplotlib.pyplot as plt
import numpy as np

# Define the equation parameters
n = np.linspace(-10, 10, 100)
x = np.sin(n)   # Example input signal

# Compute y values
y = (1/3) * (np.roll(x, -1) + x + np.roll(x, 1))

# Plot the graph
plt.plot(n, x, label='x(n)')
plt.plot(n, y, label='y(n)')
plt.legend()

# Add labels and title
plt.xlabel('n')
plt.ylabel('x(n), y(n)')
plt.title('Graph of y(n) = 1/3(x(n+1) + x(n) + x(n-1))')

# Show the plot
plt.show()
