#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 12:16:02 2018

@author: jithin
"""

import numpy as np
from tabulate import tabulate

def central_diff(f,x,h):
    return (f(x+h)+f(x-h)-2*f(x))/h**2
j=[]
hlist =[]
for i in range(1,17):
    hlist.append(10**-i)
for h in hlist:
    j.append([h,central_diff(np.sin,np.pi/6,h),central_diff(np.sin,np.pi/6,h)+np.sin(np.pi/6)])

print(tabulate(j,headers=['h', 'Computed Value', 'Error'],tablefmt="latex"))

r=[]
s=[]
def richardson(A,f,x,h,step):
    k=2
    if step ==1:
        return (2**k *A(f,x,h/2)-A(f,x,h))/(2**k -1)
    else:
        step-=1
        k+=2
        return (2**k *richardson(A,f,x,h/2,step)-richardson(A,f,x,h,step))/(2**k -1)
for h in [0.2,0.1]:
    r.append([h,richardson(central_diff,np.sin,np.pi/6,h,1),richardson(central_diff,np.sin,np.pi/6,h,1)+np.sin(np.pi/6)])

for h in [0.2,0.1]:
    s.append([h,richardson(central_diff,np.sin,np.pi/6,h,2),richardson(central_diff,np.sin,np.pi/6,h,2)+np.sin(np.pi/6)])
print(tabulate(r,headers=['h', 'Computed Value', 'Error'],tablefmt="latex"))
print(tabulate(s,headers=['h', 'Computed Value', 'Error'],tablefmt="latex"))

def rho(x):
    return 1+x**2
    
def tridiag(a, b, c, k1=-1, k2=0, k3=1):
    return np.diag(a, k1) + np.diag(b, k2) + np.diag(c, k3)

def u(x):
    return (1-x)**2

def f(x):
    return 6*x**2 - 4*x + 2

def u(x):
    return (1-x)**2
U=[]
def f(x):
    return 6*x**2 - 4*x + 2
wer=[]
error=[]
for N in [10,100,1000,10000]:
    a=[]
    b=[]
    c=[]
    B=[]
    h=1/N
    U=[]
    
    for i in range(N-1):
        a.append(rho((i+0.5)*h)/(h**2))
        b.append((-rho((i+0.5)*h)-rho((i+1.5)*h))/(h**2))
        c.append(rho((i+1.5)*h)/(h**2))
        B.append(f((i+1)*h))
        U.append(u((i+1)*h))
    #b=-a-c
    a=a+[1]
    c=[0]+c
    b=[1]+b+[-1]
    B=[1]+B+[0]
    U=[1]+U+[0]
    A = tridiag(a, b, c)
    
    A[-1,-1]=3
    A[-1,-2]=-4
    A[-1,-3]=1
    
    Y= np.linalg.solve(A, B)
    eee=U-Y
    wer.append([h,np.linalg.norm(eee)])
    error+=[np.linalg.norm(eee)]
print(tabulate(wer,headers=['h', 'Error'],tablefmt="latex"))