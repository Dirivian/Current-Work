# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 19:37:15 2018

@author: amath
"""
import numpy as np
from scipy.integrate import quad, dblquad
import matplotlib.pyplot as plt


g =9.81
h_l,h_r, X_l, X_r = 4500,480,-50,50
slope = (h_r-h_l)/(X_r-X_l)
t_r = 2*(np.sqrt(g*h_r)-np.sqrt(g*h_l))/(g*slope)

c_g = (h_l/h_r)**0.25
c_t = 2*np.sqrt(h_l)/(np.sqrt(h_l)+np.sqrt(h_r))

def h(X):
    h_l,h_r, X_l, X_r = 4500,480,-50,50
    if X <= X_l:
        return h_l
    if X >+ X_r:
        return h_r
    else:
        return h_l + (h_r-h_l)*(X-X_l)/(X_r-X_l)
        
def X(t):
    slope = (h_r-h_l)/(X_r-X_l)
    return X_l +np.sqrt(g*h_l)*t + 0.25*g*slope*t**2

def integrand(t_1,t_hat):
    return slope**2/(h(X(t_1))*h(X(t_1-t_hat/2)))**0.5
def sec_integrand(t_hat):
    return quad(integrand, t_hat/2,t_r, args= (t_hat))[0]
area = dblquad(lambda t_1, t_hat :slope**2/(h(X(t_1))*h(X(t_1-t_hat/2)))**0.5, 0, 2*t_r, lambda t_1: t_1/2, lambda t_1: t_r)

my_val = (np.log(h_l/h_r)**2)/32
print(c_g *(1-g*area[0]/32))
print(c_g *(1-my_val))

dt = 0.001
tspace = np.linspace(0,2*t_r,2*t_r/dt)

g_vec =[sec_integrand(t)*dt for t in tspace]
T = c_g*(1-np.cumsum(g_vec)*g/32)