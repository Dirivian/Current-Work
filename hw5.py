# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 18:14:15 2018

@author: amath
"""
import numpy as np
import matplotlib.pyplot as plt
N = 50
a = -4*np.ones(N**2)
b = np.ones(N**2-1)
c = np.ones(N**2-N)
def multidiag(a, b, c, N, k1=-1, k2=0, k3=1):
    return np.diag(a, k2) + np.diag(b, k1) + np.diag(b, k3) + np.diag(c, N)+ np.diag(c,- N)
A = multidiag(a,b,c,N)

def f(i,N):
    h = 1/(N+1) 
    x = (i%(N+1))*h
    g = int(i/N ) if i%N ==0 else int(i/N )+1
    y = g*h
    x = (i - (g-1)*N)*h
    return x**2 + y**2
fvec = np.array([])
for i in range(1,N**2+1):
    fvec = np.append(fvec,f(i,N**2))
h = 1/(N+1) 
i=0
for row in A:
    fvec[i]+= sum(row)
    i+=1
fv = (h**2)*fvec
x = np.linalg.solve(A, fv)
xn = np.reshape(x,(N,N))
plt.imshow(xn)