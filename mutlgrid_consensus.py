# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 14:52:24 2018

@author: amath

A_3 A_2 A_1
"""
from IPython import get_ipython
get_ipython().magic('reset -sf')
import numpy as np
import matplotlib.pyplot as plt


def altseries(N,v1=1,v2=0):
    k = np.zeros(N)
    k[::4]=v1
    k[3::4]=v2
    return k
w =np.linspace(4,40,17)
wout =[]
for N in w:
    N = int(N)
    a1 = np.ones(N-1)
    a2 = np.empty((N,))
    a2[::2]=2
    a2[1::2]=0
    a3 = 0.5*a2
    a4 = np.empty((N,))
    a4[::2]=0
    a4[1::2]=1
    
    def tridiag(a, b, c, k1=-1, k2=0, k3=1):
        return np.diag(a, k1) + np.diag(b, k2) + np.diag(c, k3)
    A_1= tridiag(0.5*a1,np.zeros(N),0.5*a1)  
    A_1[0,-1]=0.5
    A_1[-1,0]=0.5
    A_3= tridiag(a3[:-1],a2,a3[1:]) 
    if N%2 ==0:
        A_3[-1,0]=1
    A_3 = 0.5*A_3
    
    A_2= tridiag(0.5*a3[:-2],np.zeros(N),0.5*a3[:-2],-2,0,2) 
    A_2[0,-2]=0.5 
    if N%2 !=0:
        A_2[-1,1]=0.5
    else:
        A_2[-2,0]=0.5
    a34 =np.empty((N,))
    a34[::4]=1
    a34[1::4]=0
    A_4= tridiag(0.5*a34[:-4],np.zeros(N),0.5*a34[:-4],-4,0,4) 
    #print(A_4)
    altseries4_1 = altseries(4,0.5)
    altseries4_2 = altseries(4,0,0.5)
    if N%2 == 0:
        A_4[0,-4] += 0.5
    else:
        A_4[0,-3] += 0.5
    if N%4 ==0:
        diub = np.array([.5,0,0,0])
        A_4 += np.diag(diub,4-N)
    elif N%4 ==1:
        diub = np.array([0,0,.5])
        A_4 += np.diag(diub,3-N)
    elif  N%4 ==2:
        diub = np.array([0,0,.5,0])
        A_4 += np.diag(diub,4-N)
    elif  N%4 ==3:
        diub = np.array([.5,0,0])
        A_4 += np.diag(diub,3-N)
        

    print(A_4)
    alt5_1 = np.zeros(N)
    alt5_1[::4]=1
    alt5_2 = 0.5*alt5_1[:-2]
    alt5_3 = 0.5*alt5_1[2:]
    A_5 = tridiag(alt5_2,alt5_1,alt5_3,-2,0,2)
    if N%4==3:
        A_5[-1,0]=0.5
    elif N%4==0:
        A_5[-2,0]=0.5
    
    kyubi = np.dot(A_3,np.dot(A_2,A_1))
    kyubi = np.dot(A_3,A_2)
    kurama = np.dot(A_3,np.dot(A_5, np.dot(A_4,np.dot(A_2,A_1))))
    #kurama = np.dot(A_3,np.dot(A_5, np.dot(A_4,A_2)))
    A = -np.eye(N) + kyubi#kurama#np.dot(A_3,np.dot(A_5,np.dot(A_4,np.dot(A_2,A_1))))
    C  =-np.eye(N) +A_1
    C1  =-np.eye(N) +np.dot(A_1,A_1)
    ##print(np.dot(-np.eye(N)+kurama, np.ones(N)))
    def complete_matrix(N):
        return np.ones((N,N))-N*np.eye(N)
    B=complete_matrix(N)
    alist = np.linalg.eig(A)[0]
    M = max(alist)
    wout = np.append(wout,[max(n for n in alist if n!=M)])
plt.plot(w,wout)