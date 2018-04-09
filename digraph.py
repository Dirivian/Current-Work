#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 18:25:57 2018

@author: jithin
"""
import numpy as np
from scipy import integrate
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

L1 = np.array([[0,0,0],[1,-1,0],[1,0,-1]])
L = np.array([[-2,1,0],[1,-2,1],[0,1,-4]])
N=3
L = np.ones((N,N))
for i in range(N):
    L[i,i]=-4
def Lap(X,t,L=L):
    offset = [1,2,3]
    o = L.dot(offset) #-(20/t**2)*np.array([30000,40000,50000])
    return L.dot(X) +o*X

dt = 0.001
tspace = np.linspace(0.001,100,int(100/dt))

a=[1,2,3]

asol = integrate.odeint(Lap,a , tspace)

plt.plot(tspace,asol)