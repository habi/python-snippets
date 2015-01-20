"""
Matplotlib Animation Example

Fully based on Jake Vanderplas animation tutorial, available at
http://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
points = 150
xs = np.random.randint(0, 100, size=points)
ys = np.random.randint(0, 100, size=points)
zs = np.random.randint(0, 100, size=points)
scatter = ax.scatter(xs, ys, zs)


def init():
    # Initialization function: Initialize plot, move the camera
    axis = fig.gca()
    axis.azim = 66
    axis.elev = 15
    axis.set_xlim([0, 100])
    axis.set_ylim([0, 100])
    axis.set_zlim([0, 100])
    return axis,


def animate(i):
    # Animation function.
    axis = fig.gca()
    axis.azim = 45 + 40 * np.sin(np.radians(i))
    axis.elev = 30 + 10 * np.sin(np.radians(i))
    print 'animating frame', i, 'of', numframes
    return axis,

# Call the animator. blit=True means only re-draw the parts that have changed.
numframes = 360
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=numframes, interval=10, blit=True)

# Save the animation as an mp4.
#~ anim.save('basic_animation.mp4', fps=24, extra_args=['-vcodec', 'libx264'])

plt.show()
