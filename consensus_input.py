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

N =3
def Laplacian(X,t):
    L = np.ones((5,5))
    for i in range(5):
        L[i,i]=-5
    #print(L.dot(X))
    N=3

    L1 = np.ones((N,N))
    for i in range(N):
        L1[i,i]=-(N-1)
    return L1.dot(X)+ [3,0,-3]

fig = plt.figure()
#ax = fig.gca(projection='3d')
#circa =np.linspace(0,2*np.pi,100)
L1 = np.ones((N,N))
for i in range(N):
    L1[i,i]=-(N-1)


a= np.random.randint(10,size=N)
#b = np.linalg.solve(L1,-a)
dt =0.01
x=a
alpha = 0.6
xvec = [a]
for i in range(200):
    x = x+alpha*Laplacian(x,20)
    xvec= xvec+[x]
    

tspace = np.linspace(0,13,int(13/dt)) 
asol = integrate.odeint(Laplacian,a , tspace)
plt.plot(tspace,asol)
plt.ylabel('States')
plt.xlabel('Times')
plt.show