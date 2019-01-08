# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 10:30:57 2019

@author: edwinaw
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='Simple Plot')
ax.grid()

fig.savefig("test.png")
plt.show()