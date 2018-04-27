# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 07:34:58 2018

@author: amath
"""

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
from scipy.optimize import nnls

a = np.array([1,4,6])
u = np.array([1,4,6,1,2,3])
D = np.array([[1,0],[-1,1],[0,-1]])
D_t = np.transpose(D)
#x, rnorm = nnls(np.transpose(D),z_ref)
R = np.random.rand(3,3)
def LTI(x,t):
    return -np.dot(R,x)
z_ref =np.array([-10,2])
v_ref=np.array([10,2,10,30])
L = np.array([[1,-1,0],[-1,2,-1],[0,-1,1]])
def single_integrator(x,t):
    k =1
    return -k*np.dot(L,x)+k*np.dot(D,z_ref)

def double_integrator(x,t):
   # print(i)
    k =1
    I = np.eye(3)
    Ze = np.zeros((3,3))
    Ze2 = np.zeros((3,2))
    
    Lap = np.bmat([[Ze,I],[-k*L,-k*L]])
    Dap = np.bmat([[Ze2,Ze2],[k*D,k*D]])
    were = np.array(np.dot(Lap,x)+np.dot(Dap,v_ref))[0] 

    return were   
tspace = np.linspace(0,30,int(13/dt)) 
asol = integrate.odeint(single_integrator,a , tspace)
usol = integrate.odeint(double_integrator,u , tspace)
vsol = integrate.odeint(LTI,a , tspace)
plt.plot(tspace,vsol[:,:3])
plt.ylabel('States')
plt.xlabel('Times')
plt.show