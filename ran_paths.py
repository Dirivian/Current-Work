#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 09:44:52 2018

@author: jithin

To get the terms missed out by not considering alternate paths in laggin_transmissions
"""

import numpy as np
import matplotlib.pyplot as plt

def magnitude_2( l,r,m1,m2,n):
    '''
    Output: tranmission coefficient of wave through two middle layers
    Input: delta_h - Height difference in the original shock
           l       - sea bed height of left interface
           r       - sea bed height of right interface
           m1      - sea bed height of 1st middle interface
           m2      - sea bed height of 2nd middle interface 
           n       - internal reflections coefficients [x,y,z]
    '''
    x = n[0]
    y = n[1]
    z = n[2]
    t_1 = 2*np.sqrt(l)/(np.sqrt(l)+np.sqrt(m1))
    t_2 = 2*np.sqrt(m1)/(np.sqrt(m2)+np.sqrt(m1))
    t_2bar = 2*np.sqrt(m2)/(np.sqrt(m2)+np.sqrt(m1))
    t_3 = 2*np.sqrt(m2)/(np.sqrt(r)+np.sqrt(m2))
    r1 = (np.sqrt(l)-np.sqrt(m1))/(np.sqrt(l)+np.sqrt(m1))
    r2 = (np.sqrt(m2)-np.sqrt(m1))/(np.sqrt(m2)+np.sqrt(m1))
    r2bar = (np.sqrt(m1)-np.sqrt(m2))/(np.sqrt(m2)+np.sqrt(m1))
    r3 = (np.sqrt(r)-np.sqrt(m2))/(np.sqrt(m2)+np.sqrt(r))
    a  = (r2*r1)**x
    b  = (r3**y)*(r2bar**z)
    c  = (t_2bar*r1*t_2)**(y-z)
    return t_1*a*t_2*b*c*t_3

summ =0
l = 60
m1 = 45
m2 = 35
r = 30
mat =[]
i=0


def transformer(t):
    '''
    Transforms Randy's paths to mine
    '''
    x=(sum(t[::2])-len(t)+1)/2 #'Sum the odd terms and subtract the transmitted rays and divide by two to get internal reflections'
    y=(sum(t[1::2])-1)/2
    z=y-(len(t)-2)/2
    return [x,y,z]
#plt.plot(mat)  
print(2*np.sqrt(l)/(np.sqrt(l)+np.sqrt(r))) 

import itertools
o = []
e = []
o1 = []
e1 = []
for i in range(1,9):
    if i %2 != 0:
        o.append(i)
        if i<=10:
           o1.append(i) 
    else:
        e.append(i)
        if i<=10:
           e1.append(i)
oe=[1,3,5,7,9,11,13,15,17,19,21]
o2=[1,3,5,7,9,11,13,15]
e2=[2,4]
e =[2,4,6,8,10]
iterables1 = [ oe,oe ]
iterables2 = [ oe,e,e,oe]
iterables3 = [ o1,e1,e1,e1,e1,o1]
iterables4 = [ o1,e1,e1,e1,e1,e1,e1,o1]
iterables5 = [ o2,e2,e2,e2,e2,e2,e2,e2,e2,o2]
iterables6 = [ o2,e2,e2,e2,e2,e2,e2,e2,e2,e2,e2,o2]
iterables7 = [ o2,e2,e2,e2,e2,e2,e2,e2,e2,e2,e2,e2,e2,o2]
ransum=0
mat2=[]
mat3=[]
iterlist=[]
for j in [iterables1,iterables2,iterables3,iterables4,iterables5,iterables6]:
    iterlist+=itertools.product(*j)
for t in iterlist:
    n1 = transformer(t)
    n = [int(i) for i in n1]
    mat3.append(n)
mat3 = sorted(mat3, key=lambda x: -abs(magnitude_2(1,r,m1,m2,x)))
mat3100=mat3[:20]
def lag_calculator(n,l,r,m1,m2,w1,w2):
    return 2*(n[0]+n[1]-n[2])*w1*np.sqrt(r/m1)+2*n[1]*w2*np.sqrt(r/m2)
lag=[]
w1=0.1
w2=0.1
mag_array=[]
for n in mat3100:
    lag.append(lag_calculator(n,l,r,m1,m2,w1,w2))
    add = magnitude_2(l,r,m1,m2,n)
    mag_array.append(add)
def wave_maker(mag_array,lag,delta_h, time_lag,xspace):
    i = 0
    t = -1
    r = 0
    p = np.zeros(len(xspace))
    
    mag_array = [delta_h*x for x in mag_array]
    
    for x in xspace:
        if x < 1+time_lag+sum(lag[t:]):
            p[i]=sum(mag_array[:len(mag_array)-r])
        else:
            t-=1
            r+=1
            if r == len(mag_array) or sum(lag)==0:
                break
            p[i]=sum(mag_array[:len(mag_array)-r])

        i+=1
    return p
xspace = np.linspace(0,sum(lag)+10,100)
p=wave_maker(mag_array,lag,1, 5,xspace)
jum=wave_maker(mag_array,lag,-1, 0,xspace)
res=p+jum