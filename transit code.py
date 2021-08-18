# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:17:12 2018

@author: zwolfe
"""

import numpy as np
import matplotlib.pyplot as plt

d = np.loadtxt("C:\\Users\\zwolfe\\Desktop\\04_KeplerData.txt")
t=d[:,1]
f=d[:,2]
plt.plot(t, f, 'b-', 
         300, -.002, 'gs',
         329, -.00197, 'gs',
         360, -.002, 'gs',
         390, -.0022, 'gs',
         416, -.0024, 'gs',)
plt.show()