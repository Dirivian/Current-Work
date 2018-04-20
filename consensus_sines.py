# -*- coding: utf-8 -*-
"""
Created on Sun May  7 16:07:26 2017

@author: user
"""
import numpy as np
from scipy import integrate
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from copy import deepcopy
import itertools
N =50
def Laplacian(X,t):
    L1 = np.ones((N,N))
    L4 = np.zeros((5,5))
    def tridiag(a, b, c, k1=-1, k2=0, k3=1):
        return np.diag(a, k1) + np.diag(b, k2) + np.diag(c, k3)
    a = np.ones(4)
    b = np.ones(5)*(-2)
    L4 = tridiag(a,b,a)
    L4[0,0]=-1
    L4[4,4]=-1
    for i in range(N):
        L1[i,i]=-(N-1)
    return L1.dot(X)+ [3,0,-3]

fig = plt.figure()
#ax = fig.gca(projection='3d')
#circa =np.linspace(0,2*np.pi,100)
def add_edge(L, x):
    i = x[0]
    j = x[1]
    if i == j or L[i,j]==1:
        return L
    elif L[i,j]!=1:
        L[i,j]=1
        L[i,i]-=1
        L[j,j]-=1
        L[j,i]=1
        return L

pair= list(itertools.product(range(N), range(N)))        
L4 = np.zeros((N,N))
def tridiag(a, b, c, k1=-1, k2=0, k3=1):
    return np.diag(a, k1) + np.diag(b, k2) + np.diag(c, k3)
a = np.ones(N-1)
b = np.ones(N)*(-N+1)
L4 = tridiag(a,b,a)
L4[0,0]=-1
L4[N-1,N-1]=-1
#L2=deepcopy(L4)
t= abs(np.linalg.eig(L4)[0][1])
convlist = [abs(sorted(np.linalg.eig(L4)[0])[-2])] 
def argmax(pairs,L):
    L2= deepcopy(L)
    return max(pairs, key=lambda x = x: abs(sorted(np.linalg.eig(add_edge(L2, x))[0])[-2]))
for i in range(500):
    w = argmax(pair,L4)
    L4 = add_edge(L4,w)
    convlist += [abs(sorted(np.linalg.eig(L4)[0])[-2])]
c50 = convlist
plt.plot(c50, label = 'n = 50')
plt.plot(c30,  label = 'n = 30')
plt.plot(c10,  label = 'n = 10')
plt.ylabel('Algebraic Connectivity')
plt.xlabel('Edges added')
plt.show