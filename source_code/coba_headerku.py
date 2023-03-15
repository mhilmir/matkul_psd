import matplotlib.pyplot as plt
import numpy as np
import hilm_psd as hm

# Define the equation parameters
n = np.linspace(-10, 10, 100)
x = np.sin(n)   # Example input signal

# Compute y values
y = (1/3) * (np.roll(x, -1) + x + np.roll(x, 1))

hm.visualize_graph(n, [x,y], ["x(n)", "y(n)"])