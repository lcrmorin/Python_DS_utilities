import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def percentogram(series, num_bins=10):
    
    s, bins = pd.qcut(series,q=10,retbins=True)
    widths = bins[1:] - bins[:-1]
    heights = 1/widths
    center = (bins[:-1] + bins[1:]) / 2

    plt.bar(center, heights, align='center', width=widths)
    plt.title('Percentogram')
    plt.xlabel('Bins')
    plt.ylabel('Percentage')
    plt.show()

# Generate a Series of 1000 normally distributed random numbers
s = pd.Series(np.random.normal(loc=0, scale=1, size=1000))
s[0] = -10

# Plot a percentogram of the Series
percentogram(s, num_bins=10)
