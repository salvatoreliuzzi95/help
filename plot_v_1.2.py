#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from IPython.display import clear_output
import os

os.system("clear")

x=[" ","1","2","3","4","5","6","7","8","9","0","1","2"]
c=["C"," "," "," "," "," "," "," "," "," "," "," "," "]
b=["B"," "," "," "," "," "," "," "," "," "," "," "," "]
a=["A"," "," "," "," "," "," "," "," "," "," "," "," "]

for i in range(0,len(a)-1):
    try:
        ans = input("enter actual answer: ")
        os.system("clear")
        clear_output(wait=True)   
    except:
        pass
    print(" ")
    if(int(ans)==3):
        c[i+1]="*"
    if(int(ans)==2):
        b[i+1]="*"
    if(int(ans)==1):
        a[i+1]="*"
    print(' '.join(a))
    print(' '.join(b))
    print(' '.join(c))
    print(' '.join(x))
    print(" ")


