# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 18:14:15 2018

@author: amath
"""
import numpy as np
import matplotlib.pyplot as plt
N = 19
a = -4*np.ones(N)
b = np.ones(N-1)
c = np.ones(N)
I = np.eye(N)
def tridiag(a, b, c, k1=-1, k2=0, k3=1):
    return np.diag(a, k1) + np.diag(b, k2) + np.diag(c, k3)
T = tridiag(b,a,b)
S = np.diag(b, -1)+ np.diag(b, 1)
A = np.kron(I,T)+np.kron(S,I )
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
    fvec[i]= fvec[i]*(h**2)+ sum(row)
    i+=1
fv = 6*(h**2)*fvec
x = np.linalg.solve(A, fvec)
xn = np.reshape(x,(N,N))
plt.imshow(xn)
print(np.linalg.norm(xn-x100[::6,::6], 2))
