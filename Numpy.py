# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 19:59:01 2022

@author: sanjay a l
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,10,0.2)
y=np.sin(x)
z=np.cos(x)
v=np.tan(x)
u=np.sinh(x)
#plt.figure(figsize=(10,10))
plt.subplot(1,3,1)
plt.plot(x,y)
plt.title("Sine plot")

plt.subplot(1,3,2)
plt.plot(x,z)
plt.title("cos plot")
plt.subplot(1,3,3)
plt.plot(x,v)
plt.title("tan plot")