# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 10:46:40 2018

@author: amath
Block matrices for 2-d 3-d laplcians
"""
import numpy as np
import matplotlib.pyplot as plt
N = 2 #don't use N=2


def tridiag(a, b, c, k1=-1, k2=0, k3=1):
    return np.diag(a, k1) + np.diag(b, k2) + np.diag(c, k3)

def laplacian_1d(N):
    d_0 = -2*np.ones(N) 
    d_1 = np.ones(N-1)
    A = tridiag(d_1,d_0,d_1)
    A[0,-1]=1
    A[-1,0]=1
    return A
def laplacian_2d(N):
    d_0 = -4*np.ones(N) 
    d_1 = np.ones(N-1)
    imp = tridiag(d_1,0*d_0,d_1)
    imp[0,-1]=1
    imp[-1,0]=1
    A = laplacian_1d(N)
    A_second = np.kron(np.eye(N,dtype='int'),A)+np.kron(imp,np.diag(np.ones(N)))
    return A_second-2*np.diag(np.ones(N**2))


def laplacian_3d(N):
    d_0 = -6*np.ones(N) 
    d_1 = np.ones(N-1)
    imp = tridiag(d_1,0*d_0,d_1)
    imp[0,-1]=1
    imp[-1,0]=1 
    A_second = laplacian_2d(N)
    A_third = np.kron(np.eye(N,dtype='int'),A_second)+np.kron(imp,np.diag(np.ones(N**2)))
    return A_third-2*np.diag(np.ones(N**3))
w =[3,4,5,6,7,8,9,10,11]
wout=[] 
wors=[]  
for N in range(3,13):
    A = laplacian_2d(N)
    alist = np.linalg.eig(A)[0]
    M = max(alist)
    wout = np.append(wout,[max(n for n in alist if n!=M)])
    wors = np.append(wors,[-2+2*np.cos(2*np.pi/(N))])


plt.plot(wout)
plt.plot(wors)