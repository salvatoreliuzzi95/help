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
import PIL.ImageOps
#from PIL import ImageEnhance


DIR = sys.path[0]

quest = Image.open(os.path.join(DIR,'cache','quest.png'))
quest = quest.convert('L')
quest = PIL.ImageOps.invert(quest)

#quest = ImageEnhance.Brightness(quest).enhance(2.0)
#quest = ImageEnhance.Contrast(quest).enhance(20.0)

threshold = 100
quest = quest.point(lambda p: p > threshold and 255)


#quest.show()


text = pytesseract.image_to_string(quest)

with open(os.path.join(DIR,'cache','quest.txt'), 'w') as f:
    f.write(text)

