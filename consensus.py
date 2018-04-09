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


def Laplacian(X,t):
    L = np.ones((5,5))
    for i in range(5):
        L[i,i]=-5
    #print(L.dot(X))
    N=5
    L3 = np.zeros((N,N))
    for i in range(1,N):
        L3[i,0]=1
        L3[i,i]=-1
    L3[3,:]=np.zeros(N) 
    L3[1,:]=np.zeros(N)
    L4 = np.zeros((5,5))
    def tridiag(a, b, c, k1=-1, k2=0, k3=1):
        return np.diag(a, k1) + np.diag(b, k2) + np.diag(c, k3)
    a = np.ones(4)
    b = np.ones(5)*(-2)
    L4 = tridiag(a,b,a)
    L4[0,0]=-1
    L4[4,4]=-1
    return L3.dot(X)

fig = plt.figure()
#ax = fig.gca(projection='3d')
#circa =np.linspace(0,2*np.pi,100)
N =5
a= np.random.randint(10,size=N)
dt =0.01
'''
n = 1
L1 = np.ones((5,5))
for i in range(5):
    L1[i,i]=-4
L2 = np.zeros((5,5))
for i in range(1,5):
    L2[i,0]=1
    L2[i,1]=1
    L2[i,i]=-2
L2[0,:]=[-4,1,1,1,1]   
L2[1,:]=[1,-4,1,1,1] 

L3 = np.zeros((5,5))
for i in range(1,5):
    L3[i,0]=1
    L3[i,i]=-1
L3[0,:]=[-4,1,1,1,1] 

L4 = np.zeros((5,5))
def tridiag(a, b, c, k1=-1, k2=0, k3=1):
    return np.diag(a, k1) + np.diag(b, k2) + np.diag(c, k3)
a = np.ones(4)
b = np.ones(5)*(-2)
L4 = tridiag(a,b,a)
L4[0,0]=-1
L4[4,4]=-1

def check_consensus(x):
    centre = (sum(x)/5)*np.ones(5)
    if np.linalg.norm(x-centre) <0.01:
        return 1
    else:
        return 0
tspace = np.linspace(0,13,int(13/dt))
tlist =[]
#print(t)
a = [1,2,3,4,5]
Llist =[L1,L2, L3,L4]
edges =[10,8,4,4]
eiglist=[]
for L in Llist:
    t =0
    x = a
    while check_consensus(x) != 1:
        v = L.dot(x)
        x = x+v*dt
        t = t+ dt
    tlist = tlist +[t]
    eiglist =eiglist +[sorted(np.real(np.linalg.eig(L)[0]))[-2]]
 '''  
tspace = np.linspace(0,13,int(13/dt)) 
asol = integrate.odeint(Laplacian,a , tspace)
plt.plot(tspace,asol)
plt.ylabel('States')
plt.xlabel('Times')
plt.show