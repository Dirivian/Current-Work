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
def rho(x):
    return 1+x**2
    
def tridiag(a, b, c, k1=-1, k2=0, k3=1):
    return np.diag(a, k1) + np.diag(b, k2) + np.diag(c, k3)
    
def mat(thetavec,L):
    N = len(thetavec)
    h =L/N
    a1 = np.append([0.7],thetavec[:-1])
    a2 = np.append(thetavec[1:],[0.7])
    b = -2*thetavec+ a1+a2 + (h**2)* np.sin(thetavec)
    return b


def jacobian(thetavec,L):
    N = len(thetavec)
    h =L/N
    a = np.ones(N-1)
    b = -2  + (h**2)* np.cos(thetavec)
    return tridiag(a,b,a)  


N=500
L = 70*np.pi
x = np.linspace(0,L,N)
thetavec = 0.7+np.sin(x/2)
for i in range(40):
    #print(thetavec)
    b = -mat(thetavec,L)
    A = jacobian(thetavec,L)
    delta = np.linalg.solve(A,b)
    thetavec += delta
plt.plot(x,thetavec)
plt.title("T = 70$\pi$" )

