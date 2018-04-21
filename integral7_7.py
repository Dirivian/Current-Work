# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 19:37:15 2018

@author: amath
"""
import numpy as np
from scipy.integrate import quad, dblquad

def h(X):
    h_l,h_r, X_l, X_r = 4500,480,-50,50
    if X <= X_l:
        return h_l
    if X >+ X_r:
        return h_r
    else:
        return h_l + (h_r-h_l)*(X-X_l)/(X_r-X_l)
        
def X(t):
    g =9.81
    h_l,h_r, X_l, X_r = 4500,480,-50,50
    slope = (h_r-h_l)/(X_r-X_l)
    return X_l +np.sqrt(g*h_l)*t + 0.25*g*slope*t**2
    #np.sqrt(g*t*(h_l+slope*X_l))+ X_l + 0.25*g*slope*t**2
    #X_l - (h_l- (np.sqrt(g*h_l)-0.5*g*slope*t)**2/g)/slope
g =9.81
h_l,h_r, X_l, X_r = 4500,480,-50,50
slope = (h_r-h_l)/(X_r-X_l)
t_r = 2*(np.sqrt(g*h_r)-np.sqrt(g*h_l))/(g*slope)
def integrand(t_1,t_hat):
    return slope**2/(h(X(t_1))*h(X(t_1-t_hat/2)))**0.5
def sec_integrand(t_hat):
    return quad(integrand, 1, np.inf, args=(n, x))[0]
area = dblquad(lambda t_1, t_hat :slope**2/(h(X(t_1))*h(X(t_1-t_hat/2)))**0.5, 0, 2*t_r, lambda t_1: t_1/2, lambda t_1: t_r)
c_g = (h_l/h_r)**0.25
c_t = 2*np.sqrt(h_l)/(np.sqrt(h_l)+np.sqrt(h_r))
my_val = (np.log(h_l/h_r)**2)/32
print(c_g *(1-g*area[0]/32))
print(c_g *(1-my_val))