#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 08:54:49 2017

@author: jithin
"""

import numpy as np
import matplotlib.pyplot as plt

def magnitude( delta_h, l,r,m,n):
    '''
    Output: tranmission coefficient of wave through a single middle layer
    Input: delta_h - Height difference in the original shock
           l       - sea bed height of left interface
           r       - sea bed height of right interface
           m       - sea bed height of middle interface
           n       - number of internal reflections
    '''
    t_1 = 2*np.sqrt(l)/(np.sqrt(l)+np.sqrt(m))
    t_2 = 2*np.sqrt(m)/(np.sqrt(r)+np.sqrt(m))
    ref = (np.sqrt(r)-np.sqrt(m))*(np.sqrt(l)-np.sqrt(m))/((np.sqrt(r)+np.sqrt(m))*(np.sqrt(l)+np.sqrt(m)))
    return t_1*t_2*(ref**n)

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
#'''
## Trials
summ =0
l = 70
m = 40
r = 20
2*np.sqrt(l)/(np.sqrt(l)+np.sqrt(r))
mat =[]
for i in range(10):
    add = magnitude(10,l,r,m,i)
    mat.append(add)
    summ +=add
    #print(add)
    #print(2*np.sqrt(l)/(np.sqrt(l)+np.sqrt(r)))
wet =summ-2*np.sqrt(l)/(np.sqrt(l)+np.sqrt(r))
'''
## Trials 2
summ =0
l = 60
m1 = 50
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
            mat.append(add)
            summ +=add
    #print(add)
    #print(2*np.sqrt(l)/(np.sqrt(l)+np.sqrt(r)))

#plt.plot(mat) 
print(summ)  
print(2*np.sqrt(l)/(np.sqrt(l)+np.sqrt(r))) 
'''
##

def plotter(w, delta_h, l,r,m,max_ref =20):
    '''
    Output: Magnitude(height difference) of wave transmitted through the middle layer
    Input: w       - width of the middle layer
           delta_h - Height difference in the original shock
           l       - sea bed height of left interface
           r       - sea bed height of right interface
           m       - sea bed height of middle interface
           max_ref - maximum number of internal reflections
    '''
    q = 2*w*(np.sqrt(r)/np.sqrt(m))
    mag_array = []
    for i in range(max_ref):
        add = magnitude(delta_h,l,r,m,i)
        if abs(add) < 1e-5:
            break
        mag_array.append(add)
    print(mag_array)
    lag = list(range(len(mag_array)))
    lag =[q*x for x in lag]
    lag.append(0)
    #print(lag)
    pulse_width = 50
    time_lag = pulse_width*np.sqrt(r/l)
    xspace = np.linspace(0,sum(lag)+time_lag+5,100)
    #print(lag)
    
    p =wave_maker(mag_array,lag,1, time_lag,xspace)
    #print(mag_array)
    #lag = lag*q
    jum = wave_maker(mag_array,lag,-1, 0,xspace)
    res = p+jum
    #print(q)
    return xspace, p,jum
def wave_maker(mag_array,lag,delta_h, time_lag,xspace):
    i = 0
    t = -1
    r = 0
    p = np.zeros(100)
    
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
    
#summ =0
l = 60
m = 40
r = 20
w=1
delta_h =1
xspace, p,jum= plotter(1, delta_h, l,r,m)  
res = jum +p
plt.plot(xspace,p)  
#plt.plot(xspace,res)      
    