import numpy as np

# we can shift elements of an array with np.roll() function

"""
    np.roll(a, shift, axis=None)

    a:      The input array to be rolled.

    shift:  The number of places by which elements are shifted.
            If shift is positive, the elements are shifted to the right. 
            If shift is negative, the elements are shifted to the left.

    axis:   The axis along which the elements are shifted. 
            Default is None, which means that the flattened array is used.
"""

arr = np.array([1,2,3,4,5])

print(arr)  # [1 2 3 4 5]
arr = np.roll(arr, 2)  # shifting
print(arr)  # [4 5 1 2 3]