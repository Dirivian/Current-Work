# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 12:46:19 2018

@author: amath
"""
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

g =9.81
h_l,h_r, X_l, X_r = 4500,480,-50,50
slope = (h_r-h_l)/(X_r-X_l)
t_r = 2*(np.sqrt(g*h_r)-np.sqrt(g*h_l))/(g*slope)

c_g = (h_l/h_r)**0.25
c_t = 2*np.sqrt(h_l)/(np.sqrt(h_l)+np.sqrt(h_r))

def pre_integral_sums(h,k):
    return (1/(16*h))*np.log(h/(np.sqrt(h)-k)**2)
    
def integral_sums(k):
    layer=(np.sqrt(h_l)+k)**2
    q = np.log(layer/h_l)**2
    second_trm = q/32
    first_term = quad(pre_integral_sums, layer, h_r, args=(k))[0]
    if k < np.sqrt(h_r)-np.sqrt(h_l):
        return 1-second_trm
    else:
        return 1-first_term -second_trm
 
    
kfinal = (np.sqrt(h_r)-np.sqrt(h_l))
dlag = 4*np.sqrt(h_r)*kfinal/slope
doffset = 100  # specify what starting distance here
kspace =np.linspace(0,kfinal)
dspace = doffset + kspace*4*np.sqrt(h_r)/slope
v= [integral_sums(k)*c_g for k in kspace]
alphe = 4*np.sqrt(h_r)/slope
plt.plot(dspace, v[::-1])
