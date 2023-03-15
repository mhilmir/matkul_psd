import matplotlib.pyplot as plt
import numpy as np
from typing import List

def visualize_graph(n: np.ndarray, eq: List[np.ndarray], the_label: List[str]):
    """ n = the elements of array, eq = equation, label for each equation\n
        Please specify eq and label in list of string form """

    
    # checking stage
    if( (len(the_label) != len(eq)) or
        not(isinstance(n, np.ndarray)) or
        not(isinstance(eq, list)) or
        not(isinstance(the_label, list)) ):
            print("invalid argument")
            return None
    
    # Plot the graph
    for i in range(len(eq)):
        plt.plot(n, eq[i], label=the_label[i])
        # must use 'label=', because that label parameter actually is not the third order of parameter
    plt.legend()

    # Add labels and title
    plt.xlabel('n')
    # generate ylabel
    ylabel = ""
    for i in range(len(eq)):
        ylabel = the_label[i] + ", "
    plt.ylabel(ylabel)

    # Show the plot
    plt.show()
