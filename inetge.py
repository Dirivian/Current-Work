# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 12:46:19 2018

@author: amath
"""
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
def integrand(h,k):
    return (1/(16*h))*np.log(h/(np.sqrt(h)-k)**2)
    
def vec(k):
    l = 480
    layer=(np.sqrt(l)+k)**2
    q = np.log(layer/l)**2
    second_trm = q/32
    r=4500
    first_term = quad(integrand, layer, r, args=(k))[0]
    if k > np.sqrt(r)-np.sqrt(l):
        return 1-second_trm
    else:
        return 1-first_term -second_trm

r=480
l = 4500
kfinal = -(np.sqrt(r)-np.sqrt(l))
kspace =np.linspace(0,kfinal)
v= [vec(k) for k in kspace]
w = 16333
slope = (l-r)/w
alphe = 4*np.sqrt(r)/slope
plt.plot(300+alphe*kspace,v)
