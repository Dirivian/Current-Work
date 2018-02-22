
"""
Matplotlib Animation Example

author: Jake Vanderplas
email: vanderplas@astro.washington.edu
website: http://jakevdp.github.com
license: BSD
Please feel free to use and modify this, but keep the above information. Thanks!
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)
line1, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

def plot_steps(v,xspace,r,dt=0.005, limy = [-1,1]):
    for x_0 in xspace:
        t=zeros(r)
        x=np.zeros(r+1)
        x[0]= x_0
        for i in range(r):
            t[i]=i*dt
            x[i+1]=x[i]+dt*v(x[i])
        plot(t,x[:-1])
        ylim(limy)
    xlabel('t')
    ylabel('x(t)')
    

def bif_2(x):
    return -0.1*x+x**3-x**5    
# animation function.  This is called sequentially
def animate(i):
    x = np.linspace(0, i*0.01, 1000)
    y = np.sin(2 * np.pi *x)
    line.set_data(x, y)
    return line,
def animate1(i):
    x = np.linspace(0, i, 200)
    dt =6/200
    t = np.zeros(i)
    y =np.zeros(i+1)
    z =np.zeros(i+1)
    y[0]=1
    z[0]=1
    for a in range(i):
            print(y[a])
            t[a]=a*dt
            y[a+1]=y[a]+dt*np.cos(y[a])
            z[a+1]=z[a]+dt*bif_2(z[a])
    #y = np.sin(2 * np.pi *x)
    line.set_data(t,y[:-1])
    line1.set_data(t,z[:-1])
   # print(len(t),len(y))
    return line
# animation function.  This is called sequentially
def animate2(i):
    x = np.linspace(0, i, 200)
    dt =2/200
    t = np.zeros(i)
    y =np.zeros(i+1)
    z =np.zeros(i+1)
    y[0]=2
    z[0]=1
    for a in range(i):
            print(y[a])
            t[a]=a*dt
            y[a+1]=y[a]+dt*bif_2(y[a])
            z[a+1]=z[a]+dt*bif_2(z[a])
    #y = np.sin(2 * np.pi *x)
    line.set_data(t,y[:-1])
    line1.set_data(t,z[:-1])
   # print(len(t),len(y))
    return [line, line1]
# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate2, init_func=init,
                               frames=200, interval=10)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()