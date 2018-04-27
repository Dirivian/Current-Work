#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 21:57:59 2018

@author: jithin
"""
import numpy as np
import matplotlib.pyplot as plt
obstacle_list = np.array([[1,0],[0,3], [-15,4]])#,[-0,8]])
plt.figure()
plt.xlim([-25,5])
plt.ylim([-2,15])
x_0 =np.array([[-2.0,4.0],[-1,3],[-2,3.5]])
xlist=x_0
j =list(xlist)
dt = 0.01
dlist =np.array([[[0,0],[1,2],[1,3]],[[1,2],[0,0],[0,2]],[[1,3],[0,2],[0,0] ] ])
def obstacle_force(x):
    w=0
    for obstacle in obstacle_list:
        a_1 = obstacle[0]
        a_2 = obstacle[1]
        plt.plot([a_1], [a_2], marker='o', markersize=8, color="red")
        w += np.array([2*(x[0]-a_1)/((x[0]-a_1)**2+ (x[1]-a_2)**2), 2*(x[1]-a_2)/((x[0]-a_1)**2+ (x[1]-a_2)**2)])
    return w
delta =100000


def formation_force(xlist, dlist):
    i=0
    arr = np.zeros((len(xlist),2))
    for drow in dlist:
        j =0
        for d in drow:
            if list(d) != [0,0]:
                factor = 2/(delta-np.linalg.norm(d)-np.linalg.norm(abs(xlist[i]-xlist[j])-d))
                if factor == 0:
                    print(d)
                arr[i,:] += factor*(xlist[i]-xlist[j]-d)
            j+=1
        i+=1
    return -arr
goal = [-20,10]
def goal_force(xlist):
    w=0
    a_1 = goal[0]
    a_2 = goal[1]
    x_cm = sum(xlist)/len(xlist)
    w -= np.array([(x_cm[0]-a_1)*2, (x_cm[1]-a_2)*2])
    return w

for i in range(80):

    goal_f = 20*goal_force(xlist)
    form_f = 1000*formation_force(xlist,dlist)
    #print(form_f)
    ob_list = [10*obstacle_force(x) for x in x_0]
    xlist = xlist +dt*goal_f+dt*np.array(ob_list)+ dt*form_f
    plt.plot(np.append(xlist[:,0],xlist[0,0]),np.append(xlist[:,1],xlist[0,1]),color='green', linewidth = 1,
         marker='o', markerfacecolor='blue', markersize=5)
    plt.show()
    #plt.pause(0.1)
    #plt.clf()
   # plt.close()
    
    #print(xlist)


j = np.array(j)
#plt.plot(j[:,0],j[:,1])
