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

ans_1 = Image.open(os.path.join(DIR,'cache','ans_1.png'))
ans_1 = ans_1.convert('L')
text = pytesseract.image_to_string(ans_1)

with open(os.path.join(DIR,'cache','ans_1.txt'), 'w') as f:
    f.write(text)

