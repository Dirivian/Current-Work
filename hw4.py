#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 08:18:15 2018

@author: jithin

HW1 for 585
"""
import numpy as np
import matplotlib.pyplot as plt
'''
'''
def rhomaker(x):
    y=np.array([])
    for i in range(1,len(x)):
        y=np.append(y, x[i]**3-x[i-1]**3)
    return y
def f(x):
    return 6*x**2-2*x+2  
def xf(x):
    return 6*x**3-2*x**2+2*x  
def intf(x):
    return 2*x**3-x**2+2*x  
def intxf(x):
    return (6/4)*x**4-(2/3)*x**3+x**2  
def fmaker(x,i):
    return (x[i+1]/(x[i+1]-x[i]))*(intf(x[i+1])-intf(x[i])) - (x[i-1]/(x[i]-x[i-1]))*(intf(x[i])-intf(x[i-1]))+(1/(x[i]-x[i-1]))*(intxf(x[i])-intxf(x[i-1])) -(1/(x[i+1]-x[i]))*(intxf(x[i+1])-intxf(x[i])) 
def aij(x,i):
    return 1/(x[i]-x[i-1]) +(x[i]**3-x[i-1]**3)/(3*(x[i]-x[i-1])**2)
def aii(x,i):
    return aij(x,i)+aij(x,i+1)
def tridiag(a, b, c, k1=-1, k2=0, k3=1):
    return np.diag(a, k1) + np.diag(b, k2) + np.diag(c, k3)
def fmaker1(x,i):
    return x[i+1]*(intf(x[i+1])-intf(x[i])) - x[i-1]*(intf(x[i])-intf(x[i-1]))+(intxf(x[i])-intxf(x[i-1])) -(intxf(x[i+1])-intxf(x[i])) 

N=1000
x=np.array([])
for i in range(N):
    x= np.append(x,(i/(N-1))**2)
#x=np.linspace(0,1,N)
fe = np.array([])
aiivec = np.array([])
aijvec = np.array([])
for i in range(1,len(x)-1):
    fe=np.append(fe,fmaker(x,i))  
    aiivec =np.append(aiivec,aii(x,i))
    aijvec =np.append(aijvec,-aij(x,i))
xcube = x**3
xm = xcube[1:]-xcube[:-1]
xp1=xm[1:]
xm1 = xm[:-1] 
xi = xcube[2:]-xcube[:-2]

N = len(x)-1
h = 1/N
d1 = 2+(N/3)*xi
dm1 = -1-(N/3)*xm1[:-1]
dp1 = -1-(N/3)*xp1[:-1]
mat=tridiag(dm1,d1,dp1)
mat2=tridiag(aijvec[1:],aiivec,aijvec[1:])
z=np.zeros(N-2)
k = np.linalg.solve(mat2,fe)
y=x[1:-1]
plt.plot(y,k, label = "Result")
exact=y*(1-y)
plt.plot(y,exact, label = "Exact solution")
plt.legend()
print(np.linalg.norm(k-exact, np.inf))
plt.title("N="+str(N))

