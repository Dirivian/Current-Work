# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 12:32:37 2018

@author: amath
"""
import numpy as np
r=100
l=30
N=2000
summ =0
for n in range(N):
    summ += np.sqrt(r/(l+n*(r-l)/N))
print(summ/N)