# -*- coding: utf-8 -*-
"""
Created on Wed May 23 10:49:37 2018

@author: amath
"""

import numpy as np
import matplotlib.pyplot as plt

N=5
def Laplacian(N):

    L4 = np.zeros((N,N))
    def tridiag(a, b, c, k1=-1, k2=0, k3=1):
        return np.diag(a, k1) + np.diag(b, k2) + np.diag(c, k3)
    a = np.ones(N-1)
    b = np.ones(N)*(-2)
    L4 = tridiag(a,b,a)
    L4[0,0]=-1
    L4[N-1,N-1]=-1

    return L4
    
sys = Laplacian(N)
Q = np.eye(N)
R = np.eye(N)
control.lqr(sys,Q,R)