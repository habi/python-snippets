"""
3D plots are bad!
Showing Philip that the data in https://flic.kr/p/fL5FsQ can easily be plotted
better than https://flic.kr/p/fL5Ft7
"""

import matplotlib.pyplot as plt
import numpy

y = (87.4, 73, 65.7, 68.3, 61.5, 54.7, 68, 65.5, 50.4, 43.6, 39.6, 32.4)
x = range(len(y))
plt.plot(x, y, 'green', linewidth=4)
plt.xlim(min(x), max(x))
plt.ylim(0, 100)
plt.savefig('ekston.png')
plt.show()
