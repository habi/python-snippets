"""
Snippet to show how to add noise to data
"""

import matplotlib.pyplot as plt
import numpy

data = numpy.random.rand(100)
sigma = 0.1
noisydata = data + sigma * numpy.random.randn(len(data))

plt.figure()
plt.plot(data, label='Rand')
plt.plot(noisydata, label='Rand+Noise')
plt.plot(data - noisydata, label='Difference and Sigma range')
plt.legend(loc='best')
plt.axhspan(0 - sigma, 0 + sigma, facecolor='r', alpha=0.125)

plt.show()
