'''
Snippe to show how to add noise to data
'''
from pylab import *
import numpy as np

data = np.random.rand(100)
sigma = 0.1
noisydata = data + sigma * np.random.randn(len(data))

plt.figure()
plt.plot(data, label='Rand')
plt.plot(noisydata, label='Rand+Noise')
plt.plot(data - noisydata, label='Difference and Sigma range')
plt.legend(loc='best')
plt.axhspan(0-sigma, 0+sigma, facecolor='r', alpha=0.125)

plt.show()
