#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyautogui
input("Posizionare il mouse nell'angolo in ALTO a SINISTRA e premere Enter")
LU = pyautogui.position()
input("Posizionare il mouse nell'angolo in BASSO a DESTRA e premere Enter")
RD = pyautogui.position()

#10,270,295,353 // 10,270,10-295,270-353 // 10,270,285,83 // 10,270,285+10,270+83 // a,b,c-a,d-b

a=LU[0]
b=LU[1]
c=RD[0]-a
d=RD[1]-b
print("RAW data: "+str(a)+", "+ str(b)+", "+str(RD[0])+", "+str(RD[1]))
print("BOX data: "+str(a)+", "+ str(b)+", "+str(c)+", "+str(d))

