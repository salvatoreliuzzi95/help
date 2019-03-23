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

ans_3 = Image.open(os.path.join(DIR,'cache','ans_3.png'))
ans_3 = ans_3.convert('L')
text = pytesseract.image_to_string(ans_3)

with open(os.path.join(DIR,'cache','ans_3.txt'), 'w') as f:
    f.write(text)

