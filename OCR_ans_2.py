#!/usr/bin/env python
# coding: utf-8

# In[ ]:


try:
    from PIL import Image
except ImportError:
    import Image
    
import pytesseract
from pytesseract import image_to_string
import os
import sys

DIR = sys.path[0] 

ans_2 = Image.open(os.path.join(DIR,'cache','ans_2.png'))
ans_2 = ans_2.convert('L')
text = pytesseract.image_to_string(ans_2)

with open(os.path.join(DIR,'cache','ans_2.txt'), 'w') as f:
    f.write(text)

