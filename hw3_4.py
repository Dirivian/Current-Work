#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 17:22:49 2018

@author: jithin
"""
import numpy as np
import matplotlib.pyplot as plt
def tridiag(a, b, c, k1=-1, k2=0, k3=1):
    return np.diag(a, k1) + np.diag(b, k2) + np.diag(c, k3)
def mat2(thetavec):
    N = len(thetavec)
    h =1/N
    e = 0.01 #update the other e too
    a1 = np.append([-1],thetavec[:-1])
    a2 = np.append(thetavec[1:],[1.5])
    b = e*(-2*thetavec+ a1+a2) + thetavec*(0.5*h*(a2-a1)-h**2)
    return b



def jacobian2(thetavec):
    N = len(thetavec)
    h =1/N
    e =0.01 #update the other e too
    a1 = np.append([-1],thetavec[:-1])
    a2 = np.append(thetavec[1:],[1.5])
    b = -2*e  + (0.5*h*(a2-a1)-h**2)
    return tridiag(e-0.5*h*thetavec[:-1],b,e+0.5*h*thetavec[:-1])   
N=60
thetavec = np.zeros(N)
for i in range(100):
    #print(thetavec)
    b = -mat2(thetavec)
    A = jacobian2(thetavec)
    delta = np.linalg.solve(A,b)
    thetavec += delta

plt.plot(np.linspace(0,1,N),thetavec)