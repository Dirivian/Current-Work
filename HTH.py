# -*- coding: utf-8 -*-
"""
Created on Wed May  2 18:38:37 2018

@author: amath
"""
import  numpy as np
p = np.array([12,1,1])
W = np.array([[1,-1,0],[-1,2,-1],[0,-1,1]])
D= 1
plist  = [p]
for i in range(10):
    p = p - D*np.dot(W,p)
    plist = plist + [list(p)]
plot.plot(np.array(plist)[:,0])
plot.plot(np.array(plist)[:,1])
plot.plot(np.array(plist)[:,2])