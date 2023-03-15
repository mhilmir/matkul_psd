import numpy as np
import matplotlib.pyplot as plt
import hilm_psd as hp

# define the equation parameters
x = lambda n: abs(n)  # x(n) = abs(n), -3 <= n <= 3

# soal_a ---> y(n) = x(n)
n = np.linspace(-3, 3, 1000)
y = x(n)
hp.visualize_graph(n, [y], ['y(n)'])

# soal_b ---> y(n) = x(n-1)
n = np.linspace(-2, 4, 1000)
y = x(n-1)
hp.visualize_graph(n, [y], ['y(n)'])

# soal_c ---> y(n) = x(n+1)
n = np.linspace(-4, 2, 1000)
y = x(n+1)
hp.visualize_graph(n, [y], ['y(n)'])

# # soal_d ---> y(n) = 1/3 (x(n+1) + x(n) + x(n-1))
# n = np.linspace(-4, 4, 1000)
# y = 1/3 * (x(n+1) + x(n) + x(n-1))
# hp.visualize_graph(n, [y], ['y(n)'])
