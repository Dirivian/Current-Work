import numpy as np
fname = 'fort.q0012'
import matplotlib.pyplot as plt
A = np.loadtxt(fname,skiprows=6)
B = np.loadtxt('grid.data',skiprows=1)
Beff = 0.5*(B[:-1,]+B[1:])
plt.plot(Beff[:,0],A[:,-1])