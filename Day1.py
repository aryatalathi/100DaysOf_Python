#!/usr/bin/env python
# coding: utf-8

# # Reverse that number and print it.

# In[1]:


N = int(input())
R = 0    
while(N > 0):    
  rem = N %10    
  R = (R*10) + rem    
  N = N//10    
print(R)

