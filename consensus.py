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
    L = np.ones((5,5))
    for i in range(5):
        L[i,i]=-5
    #print(L.dot(X))
    L[2,1]=0
    L[1,2]=0
    L[3,4]=0
    L[4,3]=0
    return L.dot(X)
fig = plt.figure()
#ax = fig.gca(projection='3d')
#circa =np.linspace(0,2*np.pi,100)

dt =0.01
n = 1
t = np.linspace(0,10,int(10/dt))
#print(t)
a = [1,2,3,4,5]
asol = integrate.odeint(Laplacian,a , t)
plt.plot(t,asol)
plt.show