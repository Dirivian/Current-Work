import numpy as np
import matplotlib.pyplot as plt
from scipy.special import spence
hl = 4500
hr = 480
p=10000
w = 16333
def exit_time(w,hr,hl):
	return 2*w*np.sqrt(9.81)*(hr**1.5-hl**1.5)/(3*3600*(hr-hl))

hi = np.linspace(hl,hr, 10)
x2 = 4*w*np.sqrt(hr)*(np.sqrt(hi)-np.sqrt(hl))/(hr-hl)
 
greens = ((hl/hr)**(0.25) )* 2 #amplitude is here so don't worry about it later
def super(x,a):
	return 4*spence(1-np.sqrt(x)/a)-0.5*np.log(x)*(-4*np.log(1-np.sqrt(x)/a)+np.log(x)-2*np.log(x/(np.sqrt(x)-a)**2))

def man(x,a):
	 return -4*spence(1+np.sqrt(x)/a)-0.5*np.log(x)*(4*np.log((a+np.sqrt(x))/a)+np.log(x)-2*np.log((np.sqrt(x)+a)**2))
def slab(hl,hr,a):
	if a >= np.sqrt(hl)-np.sqrt(hr):
		fbab = -(1.0/32.0)*(np.log(hr/hl)**2) 
		manpack =0
	else:
		hj = (np.sqrt(hr)-a)**2
		fbab =-(1.0/32.0)*(np.log(hj/hl)**2) 
		manpack =(man(hr-a,a)- man(hl,a))/16
		
	return manpack+fbab
	
a = np.linspace(1,100, 100)
print(slab(hl,hr,0.00000001))

jason = [slab(hl,hr,ae) for ae in a]

peak  = greens*(1-(1.0/32.0)*(np.log(hi/hl)**2))
ctrans = 2*np.sqrt(hl)/(np.sqrt(hl)+np.sqrt(hr)) * 2
print(peak[-1])
print(greens)
print(ctrans)
print(exit_time(w,hr,hl))
plt.plot(jason)
'''
hl = 4500.
hr = 480.
i = 0# -np.sqrt(9.81*hl)*675

w = 16333
hi = np.linspace(hl,hr, 1000)

x = i+4*w*np.sqrt(hl)*(np.sqrt(hi)-np.sqrt(hl))/(hr-hl)
greens = ((hl/hr)**(0.25) )* 2 #amplitude is here so don't worry about it later
peak  = greens*(1-(1.0/32.0)*(np.log(hi/hl)**2))
y = 2*(1+0.25*np.log(hl/hi))
plt.plot(x,y, 'r--')
'''
plt.show()
