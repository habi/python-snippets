'''
3D plots are bad!
https://secure.flickr.com/photos/ekston/9687833776/
https://secure.flickr.com/photos/ekston/9687833792/
'''
from pylab import *

y = (87.4, 73, 65.7, 68.3, 61.5, 54.7, 68, 65.5, 50.4, 43.6, 39.6, 32.4)
x = range(len(y))
plt.plot(x, y, 'green')
plt.fill_between(x, y, facecolor='green', alpha=0.5)
plt.xlim(min(x), max(x))
plt.savefig('ekston.png')
plt.show()

