# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 19:37:15 2018

@author: amath
"""

def h(X):
    h_l,h_r, X_l, X_r = 4500,480,-50,50
    if X <= X_l:
        return h_l
    if X >+ X_r:
        return h_r
    else:
        return h_l + (h_r-h_l)*(X-X_l)/(X_r-X_l)