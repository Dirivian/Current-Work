import numpy as np
import matplotlib.pyplot as plt

hl = 4500
hr = 480
x = np.linspace(hr,hl,2000)
y = 2*(1+(1/8)*(np.log(x/hl))**2)
b = 2*(1+0.25*np.log(hl/hr)+ (1/192)*(np.log(hr/hl))**3)
print(2*(1+0.25*np.log(hl/hr)))
print(b)
greens = (hl/hr)**(0.25) 
ctrans = 2*np.sqrt(hl)/(np.sqrt(hl)+np.sqrt(hr))
print(ctrans*2)
print((1-(1/8)*(np.log(hr/hl))**2-0.25*np.log(hr/hl))*greens) 
print((1-(1/32)*(np.log(hr/hl))**2)*greens) 
#plt.plot(x,y)
#plt.show() 