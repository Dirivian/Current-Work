# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 12:46:19 2018

@author: Jithin

Plots the first order (reflected once) reflected waves

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

h_i = np.linspace(h_l,h_r, 1000)
offset = -200
x_space = offset+4*np.sqrt(h_l)*(np.sqrt(h_i)-np.sqrt(h_l))/slope
y_reflected = (1+0.25*np.log(h_l/h_i))
plt.plot(x_space,y_reflected, 'r--')
 
    

