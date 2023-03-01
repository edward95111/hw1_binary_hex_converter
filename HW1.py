#!/usr/bin/env python
# coding: utf-8

# In[8]:


a = input("Please enter a number: ")
d1 = int(int(a) / 128)
d2 = int(int(a) / 64 % 2)
d3 = int(int(a) / 32 % 2)
d4 = int(int(a) / 16 % 2)
d5 = int(int(a) / 8 % 2)
d6 = int(int(a) / 4 % 2)
d7 = int(int(a) / 2 % 2)
d8 = int(int(a) % 2)
print("Binary number is: " + str(d1) + str(d2) + str(d3) + str(d4)+ str(d5) + str(d6) + str(d7) + str(d8))

h1 = int(int(a) / 16)
h2 = int(int(a) % 16)
if h1 == 10:
    h1 = 'A'
if h1 == 11:
    h1 = 'B'
if h1 == 12:
    h1 = 'C'
if h1 == 13:
    h1 = 'D'
if h1 == 14:
    h1 = 'E'
if h1 == 15:
    h1 = 'F'
if h2 == 10:
    h2 = 'A'
if h2 == 11:
    h2 = 'B'
if h2 == 12:
    h2 = 'C'
if h2 == 13:
    h2 = 'D'
if h2 == 14:
    h2 = 'E'
if h2 == 15:
    h2 = 'F'
print("Hex number is: " + str(h1) + str(h2))


# In[ ]:





# In[ ]:




