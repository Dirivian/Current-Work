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
m1 = 60
m2 = 40
r = 30
mat =[]
i=0
for x in range(40):
    for y in range(40):
        for z in range(y+1):
            
            n = [x,y,z]
            if i ==0:
                print(n)
                i+=1
            add = magnitude_2(l,r,m1,m2,n)
            mat.append(n)
            summ +=add
    #print(add)
    #print(2*np.sqrt(l)/(np.sqrt(l)+np.sqrt(r)))
    '''
def transformer(t):
    '''
   # Transforms Randy's paths to mine
    '''
    if len(t) ==2:
        return [(t[0]-1)/2,(t[1]-1)/2,(t[1]-1)/2]
    if len(t) ==4:
        y = (t[1]+t[3]-1)/2
        return [(t[0]+t[2]-3)/2,y,y-1]
    if len(t) ==6:
        y = (t[1]+t[3]+t[5]-1)/2
        return [(t[0]+t[2]+t[4]-5)/2,y,y-2]
    if len(t) == 8:
        y = (t[1]+t[3]+t[5]+t[7]-1)/2
        return [(t[0]+t[2]+t[4]+t[6]-7)/2,y,y-3]
    if len(t) == 10:
        y = (t[1]+t[3]+t[5]+t[7]+t[9]-1)/2
        return [(t[0]+t[2]+t[4]+t[6]+t[8]-9)/2,y,y-4]
    print('error')
    '''
def transformer(t):
    '''
    Transforms Randy's paths to mine
    '''
    x=(sum(t[::2])-len(t)+1)/2 #'Sum the odd terms and subtract the transmitted rays and divide by two to get internal reflections'
    y=(sum(t[1::2])-1)/2
    z=y-(len(t)-2)/2
    return [x,y,z]
#plt.plot(mat) 
print(summ)  
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
iterables1 = [ o,o ]
iterables2 = [ o,e,e,o]
iterables3 = [ o1,e1,e1,e1,e1,o1]
iterables4 = [ o1,e1,e1,e1,e1,e1,e1,o1]
iterables5 = [ o1,e1,e1,e1,e1,e1,e1,e1,e1,o1]
ransum=0
mat2=[]
mat3=[]
for t in itertools.product(*iterables1):
    n1 = transformer(t)
    n = [int(i) for i in n1]
    add = magnitude_2(l,r,m1,m2,n)
    mat2.append(add)
    mat3.append(n)
    ransum +=add

for t in itertools.product(*iterables2):
    n1 = transformer(t)
    n = [int(i) for i in n1]
    add = magnitude_2(l,r,m1,m2,n)
    mat2.append(add)
    mat3.append(n)
    ransum +=add
#print(1)
for t in itertools.product(*iterables3):
    n1 = transformer(t)
    n = [int(i) for i in n1]
    add = magnitude_2(l,r,m1,m2,n)
    mat2.append(add)
    mat3.append(n)
    ransum +=add
#print(2)
for t in itertools.product(*iterables4):
    n1 = transformer(t)
    #print(n1)
    n = [int(i) for i in n1]
    add = magnitude_2(l,r,m1,m2,n)
    mat2.append(add)
    mat3.append(n)
    ransum +=add
#print(3)
    '''
for t in itertools.product(*iterables5):
    n1 = transformer(t)
    #print(n1)
    n = [int(i) for i in n1]
    add = magnitude_2(l,r,m1,m2,n)
    mat2.append(add)
    mat3.append(n)
    ransum +=add
    '''
print(ransum)
new_sum=0
for u in mat3:
    new_sum+=magnitude_2(l,r,m1,m2,u)
print(new_sum)


        