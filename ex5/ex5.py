# -*- coding: utf-8 -*-
"""
thy all rights reserved

"""

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0.0,20.0,201)
def f(x): return (1-np.exp(-x))*10
v=[]
t=[]
a=10;b=1
dt=0.1
v.append(30.0)
t.append(0)
end_time=20
for i in range(int(end_time/dt)):
    tmp=v[-1]+dt*(a-b*v[-1])
    v.append(tmp)
    t.append(dt*(i+1))
    print t[-1],v[-1]
line1,=plt.plot(t,v,'g.')
line2,=plt.plot(x,f(x),'r-')
plt.xlabel("time/(s)")
plt.ylabel("velocity/(m/s)")
plt.legend((line1,line2),('numerical line','analytical line'))
plt.title("The Time-dependence of the Velocity of A Ball Falling with Friction")
plt.show()
x=np.linspace(0.0,20.0,201)
def f(x): return (1-np.exp(-x))*10
v=[]
t=[]
a=10;b=1
dt=0.1
v.append(0.0)
t.append(0)
end_time=20
for i in range(int(end_time/dt)):
    tmp=v[-1]+dt*(a-b*v[-1])
    v.append(tmp)
    t.append(dt*(i+1))
    print t[-1],v[-1]
line1,=plt.plot(t,v,'g.')
line2,=plt.plot(x,f(x),'r-')
plt.xlabel("time/(s)")
plt.ylabel("velocity/(m/s)")
plt.legend((line1,line2),('numerical line','analytical line'))
plt.title("The Time-dependence of the Velocity of A Ball Falling with Friction")
plt.show()