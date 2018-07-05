# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 12:42:59 2018

@author: amath
"""
import numpy as np
h_l, h_r = 4000,480

c_g = (h_l/h_r)**0.25
c_t = 2*np.sqrt(h_l)/(np.sqrt(h_l)+np.sqrt(h_r))

first_order = np.log(c_g)
second_order = (1/2)*(np.log(c_g)**2)
third_order = (1/3)*(np.log(c_g)**3)
fourth_order = 5*(np.log(c_g)**4)/24
fifth_order = (np.log(c_g)**5)/7.5

impvec = [1,1,1/2,1/3,5/24,2/15,61/720]
impvec2=[]
t=0
for i in impvec:
	if t>0:
		impvec2 = impvec2+[i/g]
	g=i
	t=1