# -*- coding: utf-8 -*-
"""
Created on Sun May  7 16:07:26 2017

@author: user
"""
import numpy as np
from scipy import integrate
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def Laplacian(X,t):
    N=5
    w=[3,5,1,2,3]
    a = np.zeros(N)
    for i in range(N):
        b=0
        for j in range(N):
            b += -np.sin(X[i]-X[j])
        a[i]+= b
    
    return w + a

fig = plt.figure()
#ax = fig.gca(projection='3d')
#circa =np.linspace(0,2*np.pi,100)
N =5
a= np.random.randint(10,size=N)
dt =0.01
tspace = np.linspace(0,5,int(5/dt)) 
asol = integrate.odeint(Laplacian,a , tspace)
plt.plot(tspace,asol)
plt.ylabel('States')
plt.xlabel('Times')
plt.show