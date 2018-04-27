# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 07:34:58 2018

@author: amath
"""

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
from scipy.optimize import nnls

a = np.array([1,4,6,8,20])
u = np.array([1,4,6,1,2,3])
D = np.array([[1,0,0,0],[-1,1,0,0],[0,-1,1,0],[0,0,-1,1],[0,0,0,-1]])
D_t = np.transpose(D)
#x, rnorm = nnls(np.transpose(D),z_ref)
zdot_ref =np.array([1,2])
v_ref=np.array([1,2,0,1])
L = np.array([[1,-1,0,0,0],[-1,2,-1,0,0], [0,-1,2,-1,0],[0,0,-1,2,-1],[0,0,0,-1,1]])
def single_integrator(x,t):
    k =1
    z_ref = np.array([1*np.sin(t),2*np.sin(t), 0,0*t**2])
    zdot_ref = np.array([1*np.cos(t),2*np.cos(t),0,2*t*0])
    J,rnorm = nnls(np.transpose(D),zdot_ref)
    #print(J)
    return -k*np.dot(L,x)+k*np.dot(D,z_ref)+J

dt = 0.01
tspace = np.linspace(0,20,int(20/dt)) 
asol = integrate.odeint(single_integrator,a , tspace)
#usol = integrate.odeint(double_integrator,u , tspace)
plt.plot(tspace,asol[:,:5])
plt.ylabel('States')
plt.xlabel('Times')
plt.show