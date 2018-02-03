#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 08:18:15 2018

@author: jithin

HW1 for 585
"""
import numpy as np
import matplotlib.pyplot as plt
'''
'''
def rhomaker(x):
    y=np.array([])
    for i in range(1,len(x)):
        y=np.append(y, x[i]**3-x[i-1]**3)
    return y
def f(x):
    return 6*x**2-2*x+2  
def tridiag(a, b, c, k1=-1, k2=0, k3=1):
    return np.diag(a, k1) + np.diag(b, k2) + np.diag(c, k3)
N=5
x=np.linspace(0,1,N)  
xcube = x**3
xm = xcube[1:]-xcube[:-1]
xp1=xm[1:]
xm1 = xm[:-1] 
xi = xcube[2:]-xcube[:-2]

N = len(x)
h = 1/N
d1 = 2*h+(1/3)*xi
dm1 = -h-(1/3)*xm1[:-1]
dp1 = -h-(1/3)*xp1[:-1]
mat=tridiag(dm1,d1,dp1)

