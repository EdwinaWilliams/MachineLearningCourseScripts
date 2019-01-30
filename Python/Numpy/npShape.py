# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 07:39:53 2019

@author: edwinaw
"""
import numpy as np 

x = np.array([23, 21, 0, 24])
y = np.array([23, 21, 0, 24])

z= np.row_stack([x,y])
print(z.shape)