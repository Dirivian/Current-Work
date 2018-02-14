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
def mat2(thetavec,h,e=0.01):
    a1 = np.append([-1],thetavec[:-1])
    a2 = np.append(thetavec[1:],[1.5])
    b = e*(-2*thetavec+ a1+a2) + thetavec*(0.5*h*(a2-a1)-h**2)
    return b



def jacobian2(thetavec,h,e=0.01):
    a1 = np.append([-1],thetavec[:-1])
    a2 = np.append(thetavec[1:],[1.5])
    b = -2*e  + (0.5*h*(a2-a1)-h**2)
    return tridiag(e-0.5*h*thetavec[1:],b,e+0.5*h*thetavec[:-1])   
for N in [20,40,80,160]:
    h =1/N
    e=0.01
    w_0 =1.5
    x_0 = 0.25
    x= np.linspace(0,1,N)
    
    thetavec = x - x_0 +w_0*np.tanh(w_0*e*(x-x_0)/(2))
    for i in range(100):
        #print(thetavec)
        b = -mat2(thetavec,h,e)
        A = jacobian2(thetavec, h,e)
        delta = np.linalg.solve(A,b)
        thetavec += delta
    plt.plot(x,thetavec, label = N)
    plt.legend()
    