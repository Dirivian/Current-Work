# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 18:14:15 2018

@author: amath
"""
import numpy as np
N = 100
a = -4*np.ones(N**2)
b = np.ones(N**2-1)
c = np.ones(N**2-N)
def multidiag(a, b, c, N, k1=-1, k2=0, k3=1):
    return np.diag(a, k2) + np.diag(b, k1) + np.diag(b, k3) + np.diag(c, N)+ np.diag(c,- N)
A = multidiag(a,b,c,N)