#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import sys
import codecs
import pyautogui
import re
from multiprocessing import Pool
import subprocess
import time
import requests
from termcolor import colored

acc = [ 'a', 'e', 'i', 'o', 'u', 'à', 'á', 'è', 'é', 'í', 'ì', 'ó', 'ò', 'ú', 'ù','he','hi','ia','io','ie']


# In[ ]:


# Screen ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("")
print("")
print("              `........`                                                        ")
print("             :+--+hhhhhs:                                                       ")
print("             ++//yhhhhhh+                                                       ")
print("             +hhhhhooooo:      ``                       `````                   ")
print("  .`        `ohhhhs+++.       -hh-                     -yyyhh-                  ")
print("  s-     `:oyhhhhy``          -hh- ..`        `..         -hh-      ``  ..`     ")
print("  sho- `+hhhhhhhhy/h`         -hhoyyyhs.   .ohysyhs.      -hh-     /hyohyhhs.   ")
print("  shhhhhhhhhhhhhhy            -hho` `hh+  `yh+```ohh`     -hh-     /hh/` `yhs   ")
print("   /shhhhhhhhhhhy-            -hh-   hh+  :hhyssssss`     -hh-     /hh`   ohh   ")
print("    `-shhhhhhhs:`             -hh-   hh+  .hh+`    `      -hh-     /hh`  -hho   ")
print("      `-hhs-+y:               -hh-   hh+   .oyhyyyh+   +hhhhhhhh:  /hhyyyhs:    ")
print("       .y:   +/`                              ````                 /hh.``       ")
print("       `::   .:.                                                   /hh`         ")
print("")
print("                                                             powered by MIMMO   ")


DIR = sys.path[0]
print("")
print(colored("Directory: "+DIR,'white'))
print("")
sp=input("Is it a Special Edition? [y/n]: ")
nr = input('Enter number of rows: ')

# old 2-3
#10,270,295,353 // 10,270,10-295,270-353 // 10,270,285,83
#29,370,268,405 // 29,370,29-268,370-405 // 29,370,239,35
#29,433,268,470 // 29,433,29-268,433-470 // 29,433,239,37

print("")
print ("Start : %s" % time.ctime())

if(int(nr)==0): print("TEST MODE")

if(int(nr)==1):
    print("check: window 1")
    os.system("screencapture -x -R 10,200,337,25 "+os.path.join(DIR,'cache','quest.png'))
    os.system("screencapture -x -R 35,248,285,55 "+os.path.join(DIR,'cache','ans_1.png'))
    os.system("screencapture -x -R 35,322,287,56 "+os.path.join(DIR,'cache','ans_2.png'))
    os.system("screencapture -x -R 35,396,287,57 "+os.path.join(DIR,'cache','ans_3.png'))


if(int(nr)==2):
    print("check: window 2")
    os.system("screencapture -x -R 10,195,339,53 "+os.path.join(DIR,'cache','quest.png'))
    os.system("screencapture -x -R 35,263,289,57 "+os.path.join(DIR,'cache','ans_1.png'))
    os.system("screencapture -x -R 35,338,286,57 "+os.path.join(DIR,'cache','ans_2.png'))
    os.system("screencapture -x -R 35,412,284,57 "+os.path.join(DIR,'cache','ans_3.png'))


if(int(nr)==3):
    print("check: window 3")
    os.system("screencapture -x -R 10,188,337,80 "+os.path.join(DIR,'cache','quest.png'))
    os.system("screencapture -x -R 35,279,284,57 "+os.path.join(DIR,'cache','ans_1.png'))
    os.system("screencapture -x -R 35,353,286,57 "+os.path.join(DIR,'cache','ans_2.png'))
    os.system("screencapture -x -R 35,428,286,57 "+os.path.join(DIR,'cache','ans_3.png'))


if(int(nr)==4):
    print("check: window 4")
    os.system("screencapture -x -R 10,185,339,103 "+os.path.join(DIR,'cache','quest.png'))
    os.system("screencapture -x -R 34,295,289,56 "+os.path.join(DIR,'cache','ans_1.png'))
    os.system("screencapture -x -R 34,369,285,58 "+os.path.join(DIR,'cache','ans_2.png'))
    os.system("screencapture -x -R 34,445,289,57 "+os.path.join(DIR,'cache','ans_3.png'))


print("Screen: Completed")


# In[ ]:


# OCR --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

OCRa1=os.path.join(DIR,'OCR_ans_1.py')
OCRa2=os.path.join(DIR,'OCR_ans_2.py')
OCRa3=os.path.join(DIR,'OCR_ans_3.py')
OCRq=os.path.join(DIR,'OCR_quest.py')
processes = (OCRq, OCRa1, OCRa2, OCRa3)
def run_process(process):
    os.system('python {}'.format(process))
pool = Pool(processes=4)
pool.map(run_process, processes)

print("OCR: Completed")


# In[ ]:


# Loader and Control box --------------------------------------------------------------------------------------------------------------------------------------------------------

limit_data=2011

quest=open(os.path.join(DIR,'cache','quest.txt')).read().replace(",","")

print("Check quest:")
print(colored(quest,"white"))

BOW = codecs.open(os.path.join(DIR,'BOW.txt'), 'r',encoding='utf8',errors="ignore").read()
BOW_hys = BOW.split() #bag of words hystorical events 
BOW = list(set(BOW.lower().split()+quest.lower().replace('"','').replace("?","").strip().split())) #bag of words

ans_1=open(os.path.join(DIR,'cache','ans_1.txt')).read().replace('\ufeff','').strip().replace("|","I")
ans_1F=ans_1 #full
ans_1=ans_1.split() 
ans_2=open(os.path.join(DIR,'cache','ans_2.txt')).read().replace('\ufeff','').strip().replace("|","I")
ans_2F=ans_2 #full
ans_2=ans_2.split()
ans_3=open(os.path.join(DIR,'cache','ans_3.txt')).read().replace('\ufeff','').strip().replace("|","I")
ans_3F=ans_3 #full
ans_3=ans_3.split()

precedenteILLOLA=0
pointer1=""

prima=0
dopo=0
precedente=0
stessoanno=0
entrambe=0
non=0
nessuno=0
quando=0
special=0

if(sp is not "n"): 
    special=1
    sp=open(os.path.join(DIR,'specialedition.txt')).read() 
    print("SPECIAL EDITION MODE ON: "+sp)
if((quest.find("primo?")>-1 or quest.find("per primo?")>-1 or quest.find("per prima?")>-1 or quest.find("prima?")>-1 or
    quest.find("primo!")>-1 or quest.find("per primo!")>-1 or quest.find("per prima!")>-1) or quest.find("prima!")>-1): prima=1    
if(quest.find("precedente?")>-1 or quest.find("meno recente?")>-1 or quest.find("meno recente")>-1):    
    if(quest.find("Il")>-1 or quest.find("Lo")>-1 or quest.find("La")>-1 ):
        precedenteILLOLA=1
        pointer1=quest.split()[1]
    precedente=1
    
if(quest.find("cronologicamente dopo?")>-1 or quest.find("per ultimo?")>-1 or quest.find("tardi?")>-1 or quest.find("successiva?")>-1 or quest.find("dopo?")>-1): dopo=1
if(precedente==0 and quest.find("recente?")>-1): dopo=1


if(quest.find("stesso")>-1 and quest.find("anno")>-1): stessoanno=1
if((ans_3F.find("Entrambe")>-1 or ans_2F.find("Entrambe")>-1 or ans_1F.find("Entrambe")>-1 or
    ans_3F.find("Entrambi")>-1 or ans_2F.find("Entrambi")>-1 or ans_1F.find("Entrambi")>-1)): entrambe=1
if((ans_3F.find("Nessuno")>-1 or ans_2F.find("Nessuno")>-1 or ans_1F.find("Nessuno")>-1 or
    ans_3F.find("Nessuna")>-1 or ans_2F.find("Nessuna")>-1 or ans_1F.find("Nessuna")>-1)): nessuno=1
if(quest.find('NON')>-1 or quest.find('falsa?')>-1 or quest.find('non')>-1): non=1
    
if(quest.find("Quando ")>-1):
    if(ans_1F.find("Prima ")>-1 or ans_1F.find("Dopo ")>-1 or ans_1F.find("Tra ")>-1 or ans_1F.find("Lo stesso ")>-1 or ans_1F.find("Durante ")>-1): 
        quando=1

if(special==0):
    questlink="https://www.google.com/search?q="+'+'.join(quest.split()).replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
else:
    sp='+'.join(sp.split())
    questlink="https://www.google.com/search?q="+'+'.join(quest.split()).replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")+"+"+sp


# In[ ]:


# quando --------------------------------------------------------------------------------------------------------------------------------------------------------------------

if(quando==1):
    mille = input('Choose the year range >1000 (enter 1) or <1000 (enter 2): ')
    
if(quando==1 and int(mille)==1): 
    
    print('Typology: Quando A_1000')
    
    prima1=0
    prima2=0
    prima3=0

    dopo1=0
    dopo2=0
    dopo3=0
    
    tra1=0
    tra2=0
    tra3=0
    
    stesso1=0
    stesso2=0
    stesso3=0
    
    check_tra=0
    
    if(ans_1F.find("Lo stesso ")>-1 or ans_1F.find("Durante ")>-1): stesso1=1
    if(ans_2F.find("Lo stesso ")>-1 or ans_1F.find("Durante ")>-1): stesso2=1
    if(ans_3F.find("Lo stesso ")>-1 or ans_1F.find("Durante ")>-1): stesso3=1
    
    if(ans_1F.find("Prima ")>-1): prima1=1
    if(ans_2F.find("Prima ")>-1): prima2=1
    if(ans_3F.find("Prima ")>-1): prima3=1
        
    if(ans_1F.find("Dopo ")>-1): dopo1=1
    if(ans_2F.find("Dopo ")>-1): dopo2=1
    if(ans_3F.find("Dopo ")>-1): dopo3=1
        
    if(ans_1F.find("Tra ")>-1): 
        tra1=1 
        check_tra=1
    if(ans_2F.find("Tra ")>-1): 
        tra2=1 
        check_tra=1
    if(ans_3F.find("Tra ")>-1): 
        tra3=1 
        check_tra=1
        
    
    mese = ['gen','feb','mar','apr','mag','giu','lug','ago','set','ott','nov','dic']
    
    ans_1=open(os.path.join(DIR,'cache','ans_1.txt'))
    ans_2=open(os.path.join(DIR,'cache','ans_2.txt'))
    ans_3=open(os.path.join(DIR,'cache','ans_3.txt'))
    
    print("LINK quest:")
    print(colored(questlink,'blue'))

    ans_1="https://www.google.com/search?q="+'+'.join(ans_1.read().split())+"+anno"
    ans_1=ans_1.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
    print("LINK ans_1:")
    print(colored(ans_1,'blue'))
    
    ans_2="https://www.google.com/search?q="+'+'.join(ans_2.read().split())+"+anno"
    ans_2=ans_2.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
    print("LINK ans_2:")
    print(colored(ans_2,'blue'))
    
    ans_3="https://www.google.com/search?q="+'+'.join(ans_3.read().split())+"+anno"
    ans_3=ans_3.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
    print("LINK ans_3:")
    print(colored(ans_3,'blue'))

    subprocess.Popen(["lynx -dump "+questlink+" > "+os.path.join(DIR,'cache','googling.txt')], shell=True)
    subprocess.Popen(["lynx -dump "+ans_1+" > "+os.path.join(DIR,'cache','goans1.txt')], shell=True)
    subprocess.Popen(["lynx -dump "+ans_2+" > "+os.path.join(DIR,'cache','goans2.txt')], shell=True)
    subprocess.Popen(["lynx -dump "+ans_3+" > "+os.path.join(DIR,'cache','goans3.txt')], shell=True)
        
    time.sleep(2)
    
    
    googling2=open(os.path.join(DIR,'cache','googling2.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','googling.txt'),'r+',encoding='utf8',errors="ignore") as googling:
        lines = googling.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','googling2.txt'),'w') as googling2:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                googling2.write(lines[i])
    os.remove(os.path.join(DIR,'cache','googling.txt'))
    os.rename(os.path.join(DIR,'cache','googling2.txt'),os.path.join(DIR,'cache','googling.txt'))
    
    
    goans11=open(os.path.join(DIR,'cache','goans11.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','goans1.txt'),'r+',encoding='utf8',errors="ignore") as goans1:
        lines = goans1.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','goans11.txt'),'w') as goans11:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                goans11.write(lines[i])
    os.remove(os.path.join(DIR,'cache','goans1.txt'))
    os.rename(os.path.join(DIR,'cache','goans11.txt'),os.path.join(DIR,'cache','goans1.txt'))
    
    
    goans22=open(os.path.join(DIR,'cache','goans22.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','goans2.txt'),'r+',encoding='utf8',errors="ignore") as goans2:
        lines = goans2.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','goans22.txt'),'w') as goans22:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                goans22.write(lines[i])
    os.remove(os.path.join(DIR,'cache','goans2.txt'))
    os.rename(os.path.join(DIR,'cache','goans22.txt'),os.path.join(DIR,'cache','goans2.txt'))
    
    
    goans33=open(os.path.join(DIR,'cache','goans33.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','goans3.txt'),'r+',encoding='utf8',errors="ignore") as goans3:
        lines = goans3.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','goans33.txt'),'w') as goans33:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                goans33.write(lines[i])
    os.remove(os.path.join(DIR,'cache','goans3.txt'))
    os.rename(os.path.join(DIR,'cache','goans33.txt'),os.path.join(DIR,'cache','goans3.txt'))
    
    googling=codecs.open(os.path.join(DIR,'cache','googling.txt'), 'r',encoding='utf8',errors="ignore").read()
    goans1=codecs.open(os.path.join(DIR,'cache','goans1.txt'), 'r',encoding='utf8',errors="ignore").read()
    goans2=codecs.open(os.path.join(DIR,'cache','goans2.txt'), 'r',encoding='utf8',errors="ignore").read()
    goans3=codecs.open(os.path.join(DIR,'cache','goans3.txt'), 'r',encoding='utf8',errors="ignore").read()
    
    
    D0 = re.findall(r'\d+', googling) # DATA googling
    date = []
    
    for i in range(0,len(D0)): 
        if(len(D0[i])==4 and (int(str(D0[i])[0])==1 or int(str(D0[i])[0])==2)): 
            if (int(D0[i])<limit_data): 
                date.append(D0[i])

    date0 = list(set(date))
    DATA0 = 0
    temp = 0
    
    for i in range(0,len(date0)):
        if(date.count(date0[i])>temp): 
            DATA0=date0[i]
            temp=date.count(date0[i])
    
    
    D1 = re.findall(r'\d+', goans1) # DATA ans_1
    date = []
    
    for i in range(0,len(D1)): 
        if(len(D1[i])==4 and (int(str(D1[i])[0])==1 or int(str(D1[i])[0])==2)): 
            if (int(D1[i])<limit_data): 
                date.append(D1[i])
                
    date1 = list(set(date))
    DATA1 = 0
    temp = 0
    
    for i in range(0,len(date1)):
        if(date.count(date1[i])>temp): 
            DATA1=date1[i]
            temp=date.count(date1[i])
    
    D2 = re.findall(r'\d+', goans2) # DATA ans_2
    date = []
    
    for i in range(0,len(D2)): 
        if(len(D2[i])==4 and (int(str(D2[i])[0])==1 or int(str(D2[i])[0])==2)): 
            if (int(D2[i])<limit_data): 
                date.append(D2[i])
                
    date2 = list(set(date))
    DATA2 = 0
    temp = 0
    
    for i in range(0,len(date2)):
        if(date.count(date2[i])>temp): 
            DATA2=date2[i]
            temp=date.count(date2[i])

    D3 = re.findall(r'\d+', goans3) # DATA ans_3
    date = []
    
    for i in range(0,len(D3)): 
        if(len(D3[i])==4 and (int(str(D3[i])[0])==1 or int(str(D3[i])[0])==2)): 
            if (int(D3[i])<limit_data): 
                date.append(D3[i])
                
    date3 = list(set(date))
    DATA3 = 0
    temp = 0
    
    for i in range(0,len(date3)):
        if(date.count(date3[i])>temp): 
            DATA3=date3[i]
            temp=date.count(date3[i])
            
    if(tra1==1): DATA1 = str(DATA2)+"-"+str(DATA3)
    if(tra2==1): DATA2 = str(DATA1)+"-"+str(DATA3) 
    if(tra3==1): DATA3 = str(DATA1)+"-"+str(DATA2)
            
    print('Check date: ',end ="")
    print(colored(str(DATA0)+", ","red"),end ="")
    print(colored(str(DATA1)+", "+str(DATA2)+", "+str(DATA3),"yellow"))
            
    exception=0
    if(DATA0==0 or DATA1==0 or DATA2==0 or DATA3==0): exception=1
    if(exception==1): print(colored("ZEROS EXCEPTION",'red'))
        
        
    if(stesso1==1 and DATA0==DATA1 and exception==0):
        print(colored("A: " + ans_1F,'red'))
    if(stesso2==1 and DATA0==DATA2 and exception==0):
        print(colored("B: " + ans_2F,'red'))
    if(stesso3==1 and DATA0==DATA3 and exception==0):
        print(colored("C: " + ans_3F,'red'))

    if(tra1==1 and exception==0):                                              # ans_1 = tra
        if(DATA0>DATA2 and DATA0<DATA3):
            print(colored("A: " + ans_1F,'red'))
        if(DATA0<DATA2 and DATA0>DATA3):
            print(colored("A: " + ans_1F,'red'))

    if(tra2==1 and exception==0):                                              # ans_2 = tra     
        if(DATA0>DATA1 and DATA0<DATA3):
            print(colored("B: " + ans_2F,'red'))
        if(DATA0<DATA1 and DATA0>DATA3):
            print(colored("B: " + ans_2F,'red'))
            
    if(tra3==1 and exception==0):                                              # ans_3 = tra
        if(DATA0>DATA1 and DATA0<DATA2):
            print(colored("C: " + ans_3F,'red'))
        if(DATA0<DATA1 and DATA0>DATA2):
            print(colored("C: " + ans_3F,'red'))

    
    if(prima1==1 and DATA0<DATA1 and tra1==0 and exception==0): 
        print(colored("A: " + ans_1F,'red'))
    if(dopo1==1 and DATA0>DATA1 and tra1==0 and exception==0):
        print(colored("A: " + ans_1F,'red'))
    if(prima2==1 and DATA0<DATA2 and tra2==0 and exception==0): 
        print(colored("B: " + ans_2F,'red'))
    if(dopo2==1 and DATA0>DATA2 and tra2==0 and exception==0):
        print(colored("B: " + ans_2F,'red'))
    if(prima3==1 and DATA0<DATA3 and tra3==0 and exception==0):
        print(colored("C: " + ans_3F,'red'))
    if(dopo3==1 and DATA0>DATA3 and tra3==0 and exception==0):
        print(colored("C: " + ans_3F,'red'))

            
    os.remove(os.path.join(DIR,'cache','goans1.txt'))
    os.remove(os.path.join(DIR,'cache','goans2.txt'))
    os.remove(os.path.join(DIR,'cache','goans3.txt'))
    os.remove(os.path.join(DIR,'cache','googling.txt'))
    
    
if(quando==1 and int(mille)==2): 
    
    print('Typology: Quando B_1000')
    
    prima1=0
    prima2=0
    prima3=0

    dopo1=0
    dopo2=0
    dopo3=0
    
    tra1=0
    tra2=0
    tra3=0
    
    stesso1=0
    stesso2=0
    stesso3=0
    
    check_tra=0
    
    if(ans_1F.find("Lo stesso ")>-1): stesso1=1 
    if(ans_2F.find("Lo stesso ")>-1): stesso2=1 
    if(ans_3F.find("Lo stesso ")>-1): stesso3=1 
    
    if(ans_1F.find("Prima ")>-1): prima1=1
    if(ans_2F.find("Prima ")>-1): prima2=1
    if(ans_3F.find("Prima ")>-1): prima3=1
        
    if(ans_1F.find("Dopo ")>-1): dopo1=1
    if(ans_2F.find("Dopo ")>-1): dopo2=1
    if(ans_3F.find("Dopo ")>-1): dopo3=1
        
    if(ans_1F.find("Tra ")>-1): 
        tra1=1 
        check_tra=1
    if(ans_2F.find("Tra ")>-1): 
        tra2=1 
        check_tra=1
    if(ans_3F.find("Tra ")>-1): 
        tra3=1 
        check_tra=1
        
    
    mese = ['gen','feb','mar','apr','mag','giu','lug','ago','set','ott','nov','dic']
    
    ans_1=open(os.path.join(DIR,'cache','ans_1.txt'))
    ans_2=open(os.path.join(DIR,'cache','ans_2.txt'))
    ans_3=open(os.path.join(DIR,'cache','ans_3.txt'))
    
    print("LINK quest:")
    print(colored(questlink,'blue'))

    ans_1="https://www.google.com/search?q="+'+'.join(ans_1.read().split())+"+anno"
    ans_1=ans_1.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
    print("LINK ans_1:")
    print(colored(ans_1,'blue'))
    
    ans_2="https://www.google.com/search?q="+'+'.join(ans_2.read().split())+"+anno"
    ans_2=ans_2.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
    print("LINK ans_2:")
    print(colored(ans_2,'blue'))
    
    ans_3="https://www.google.com/search?q="+'+'.join(ans_3.read().split())+"+anno"
    ans_3=ans_3.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
    print("LINK ans_3:")
    print(colored(ans_3,'blue'))

    subprocess.Popen(["lynx -dump "+questlink+" > "+os.path.join(DIR,'cache','googling.txt')], shell=True)
    subprocess.Popen(["lynx -dump "+ans_1+" > "+os.path.join(DIR,'cache','goans1.txt')], shell=True)
    subprocess.Popen(["lynx -dump "+ans_2+" > "+os.path.join(DIR,'cache','goans2.txt')], shell=True)
    subprocess.Popen(["lynx -dump "+ans_3+" > "+os.path.join(DIR,'cache','goans3.txt')], shell=True)
        
    time.sleep(2)
    
    
    googling2=open(os.path.join(DIR,'cache','googling2.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','googling.txt'),'r+',encoding='utf8',errors="ignore") as googling:
        lines = googling.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','googling2.txt'),'w') as googling2:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                googling2.write(lines[i])
    os.remove(os.path.join(DIR,'cache','googling.txt'))
    os.rename(os.path.join(DIR,'cache','googling2.txt'),os.path.join(DIR,'cache','googling.txt'))
    
    
    goans11=open(os.path.join(DIR,'cache','goans11.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','goans1.txt'),'r+',encoding='utf8',errors="ignore") as goans1:
        lines = goans1.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','goans11.txt'),'w') as goans11:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                goans11.write(lines[i])
    os.remove(os.path.join(DIR,'cache','goans1.txt'))
    os.rename(os.path.join(DIR,'cache','goans11.txt'),os.path.join(DIR,'cache','goans1.txt'))
    
    
    goans22=open(os.path.join(DIR,'cache','goans22.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','goans2.txt'),'r+',encoding='utf8',errors="ignore") as goans2:
        lines = goans2.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','goans22.txt'),'w') as goans22:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                goans22.write(lines[i])
    os.remove(os.path.join(DIR,'cache','goans2.txt'))
    os.rename(os.path.join(DIR,'cache','goans22.txt'),os.path.join(DIR,'cache','goans2.txt'))
    
    
    goans33=open(os.path.join(DIR,'cache','goans33.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','goans3.txt'),'r+',encoding='utf8',errors="ignore") as goans3:
        lines = goans3.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','goans33.txt'),'w') as goans33:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                goans33.write(lines[i])
    os.remove(os.path.join(DIR,'cache','goans3.txt'))
    os.rename(os.path.join(DIR,'cache','goans33.txt'),os.path.join(DIR,'cache','goans3.txt'))
    
    googling=codecs.open(os.path.join(DIR,'cache','googling.txt'), 'r',encoding='utf8',errors="ignore").read()
    goans1=codecs.open(os.path.join(DIR,'cache','goans1.txt'), 'r',encoding='utf8',errors="ignore").read()
    goans2=codecs.open(os.path.join(DIR,'cache','goans2.txt'), 'r',encoding='utf8',errors="ignore").read()
    goans3=codecs.open(os.path.join(DIR,'cache','goans3.txt'), 'r',encoding='utf8',errors="ignore").read()
    
    
    D0 = re.findall(r'\d+', googling) # DATA googling
    date = []
    
    for i in range(0,len(D0)): 
        if(len(D0[i])==3): 
            date.append(D0[i])
                
    date0 = list(set(date))
    DATA0 = 0
    temp = 0
    
    for i in range(0,len(date0)):
        if(date.count(date0[i])>temp): 
            DATA0=date0[i]
            temp=date.count(date0[i])
    
    
    D1 = re.findall(r'\d+', goans1) # DATA ans_1
    date = []
    
    for i in range(0,len(D1)): 
        if(len(D1[i])==3): 
            date.append(D1[i])
                
    date1 = list(set(date))
    DATA1 = 0
    temp = 0
    
    for i in range(0,len(date1)):
        if(date.count(date1[i])>temp): 
            DATA1=date1[i]
            temp=date.count(date1[i])
    
    D2 = re.findall(r'\d+', goans2) # DATA ans_2
    date = []
    
    for i in range(0,len(D2)): 
        if(len(D2[i])==3): 
            date.append(D2[i])
                
    date2 = list(set(date))
    DATA2 = 0
    temp = 0
    
    for i in range(0,len(date2)):
        if(date.count(date2[i])>temp): 
            DATA2=date2[i]
            temp=date.count(date2[i])

    D3 = re.findall(r'\d+', goans3) # DATA ans_3
    date = []
    
    for i in range(0,len(D3)): 
        if(len(D3[i])==3): 
            date.append(D3[i])
                
    date3 = list(set(date))
    DATA3 = 0
    temp = 0
    
    for i in range(0,len(date3)):
        if(date.count(date3[i])>temp): 
            DATA3=date3[i]
            temp=date.count(date3[i])
            
    if(tra1==1): DATA1 = str(DATA2)+"-"+str(DATA3)
    if(tra2==1): DATA2 = str(DATA1)+"-"+str(DATA3) 
    if(tra3==1): DATA3 = str(DATA1)+"-"+str(DATA2)

    print('Check date: ',end ="")
    print(colored(str(DATA0)+", ","red"),end ="")
    print(colored(str(DATA1)+", "+str(DATA2)+", "+str(DATA3),"yellow"))
    
    exception=0
    if(DATA0==0 or DATA1==0 or DATA2==0 or DATA3==0): exception=1
    if(exception==1): print(colored("ZEROS EXCEPTION",'red'))
        
    if(stesso1==1 and DATA0==DATA1 and exception==0):
        print(colored("A: " + ans_1F,'red'))
    if(stesso2==1 and DATA0==DATA2 and exception==0):
        print(colored("B: " + ans_2F,'red'))
    if(stesso3==1 and DATA0==DATA3 and exception==0):
        print(colored("C: " + ans_3F,'red'))

    if(tra1==1 and exception==0):                                              # ans_1 = tra
        if(DATA0>DATA2 and DATA0<DATA3):
            print(colored("A: " + ans_1F,'red'))
        if(DATA0<DATA2 and DATA0>DATA3):
            print(colored("A: " + ans_1F,'red'))

    if(tra2==1 and exception==0):                                              # ans_2 = tra     
        if(DATA0>DATA1 and DATA0<DATA3):
            print(colored("B: " + ans_2F,'red'))
        if(DATA0<DATA1 and DATA0>DATA3):
            print(colored("B: " + ans_2F,'red'))
            
    if(tra3==1 and exception==0):                                              # ans_3 = tra
        if(DATA0>DATA1 and DATA0<DATA2):
            print(colored("C: " + ans_3F,'red'))
        if(DATA0<DATA1 and DATA0>DATA2):
            print(colored("C: " + ans_3F,'red'))
    
    if(prima1==1 and DATA0<DATA1 and tra1==0 and exception==0): 
        print(colored("A: " + ans_1F,'red')) 
    if(dopo1==1 and DATA0>DATA1 and tra1==0 and exception==0):
        print(colored("A: " + ans_1F,'red'))
    if(prima2==1 and DATA0<DATA2 and tra2==0 and exception==0): 
        print(colored("B: " + ans_2F,'red'))  
    if(dopo2==1 and DATA0>DATA2 and tra2==0 and exception==0):
        print(colored("B: " + ans_2F,'red'))
    if(prima3==1 and DATA0<DATA3 and tra3==0 and exception==0):
        print(colored("C: " + ans_3F,'red'))
    if(dopo3==1 and DATA0>DATA3 and tra3==0 and exception==0):
        print(colored("C: " + ans_3F,'red'))

            
    os.remove(os.path.join(DIR,'cache','goans1.txt'))
    os.remove(os.path.join(DIR,'cache','goans2.txt'))
    os.remove(os.path.join(DIR,'cache','goans3.txt'))
    os.remove(os.path.join(DIR,'cache','googling.txt'))




# In[ ]:


# stesso anno MOD --------------------------------------------------------------------------------------------------------------------------------------------------------------------

if(stessoanno==1):
    
    print('Typology: stesso anno')
    
    mese = ['gen','feb','mar','apr','mag','giu','lug','ago','set','ott','nov','dic']
    
    print("LINK quest:")
    print(colored(questlink,'blue'))
    
    ans_1=open(os.path.join(DIR,'cache','ans_1.txt'))
    ans_2=open(os.path.join(DIR,'cache','ans_2.txt'))
    ans_3=open(os.path.join(DIR,'cache','ans_3.txt'))

    
    ans_1="https://www.google.com/search?q="+'+'.join(ans_1.read().split())+"+anno"
    ans_1=ans_1.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
    print("LINK ans_1:")
    print(colored(ans_1,'blue'))
    
    ans_2="https://www.google.com/search?q="+'+'.join(ans_2.read().split()) + "+anno"
    ans_2=ans_2.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
    print("LINK ans_2:")
    print(colored(ans_2,'blue'))
    
    ans_3="https://www.google.com/search?q="+'+'.join(ans_3.read().split()) + "+anno"
    ans_3=ans_3.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
    print("LINK ans_3:")
    print(colored(ans_3,'blue'))
    
    subprocess.Popen(["lynx -dump "+questlink+" > "+os.path.join(DIR,'cache','googling.txt')], shell=True)
    subprocess.Popen(["lynx -dump "+ans_1+" > "+os.path.join(DIR,'cache','goans1.txt')], shell=True)
    subprocess.Popen(["lynx -dump "+ans_2+" > "+os.path.join(DIR,'cache','goans2.txt')], shell=True)
    subprocess.Popen(["lynx -dump "+ans_3+" > "+os.path.join(DIR,'cache','goans3.txt')], shell=True)
    
    time.sleep(2)
    
    googling2=open(os.path.join(DIR,'cache','googling2.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','googling.txt'),'r+',encoding='utf8',errors="ignore") as googling:
        lines = googling.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','googling2.txt'),'w') as googling2:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                googling2.write(lines[i])
    os.remove(os.path.join(DIR,'cache','googling.txt'))
    os.rename(os.path.join(DIR,'cache','googling2.txt'),os.path.join(DIR,'cache','googling.txt'))
    
    goans11=open(os.path.join(DIR,'cache','goans11.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','goans1.txt'),'r+',encoding='utf8',errors="ignore") as goans1:
        lines = goans1.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','goans11.txt'),'w') as goans11:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                goans11.write(lines[i])
    os.remove(os.path.join(DIR,'cache','goans1.txt'))
    os.rename(os.path.join(DIR,'cache','goans11.txt'),os.path.join(DIR,'cache','goans1.txt'))
    
    goans22=open(os.path.join(DIR,'cache','goans22.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','goans2.txt'),'r+',encoding='utf8',errors="ignore") as goans2:
        lines = goans2.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','goans22.txt'),'w') as goans22:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                goans22.write(lines[i])
    os.remove(os.path.join(DIR,'cache','goans2.txt'))
    os.rename(os.path.join(DIR,'cache','goans22.txt'),os.path.join(DIR,'cache','goans2.txt'))
    
    goans33=open(os.path.join(DIR,'cache','goans33.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','goans3.txt'),'r+',encoding='utf8',errors="ignore") as goans3:
        lines = goans3.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','goans33.txt'),'w') as goans33:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                goans33.write(lines[i])
    os.remove(os.path.join(DIR,'cache','goans3.txt'))
    os.rename(os.path.join(DIR,'cache','goans33.txt'),os.path.join(DIR,'cache','goans3.txt'))
    
    googling=codecs.open(os.path.join(DIR,'cache','googling.txt'), 'r',encoding='utf8',errors="ignore").read()
    goans1=codecs.open(os.path.join(DIR,'cache','goans1.txt'), 'r',encoding='utf8',errors="ignore").read()
    goans2=codecs.open(os.path.join(DIR,'cache','goans2.txt'), 'r',encoding='utf8',errors="ignore").read()
    goans3=codecs.open(os.path.join(DIR,'cache','goans3.txt'), 'r',encoding='utf8',errors="ignore").read()

    
    D0 = re.findall(r'\d+', googling) # DATA googling
    date = []
    
    for i in range(0,len(D0)): 
        if(len(D0[i])==4): 
            date.append(D0[i])
                
    date0 = list(set(date))
    DATA0 = 0
    temp = 0
    
    for i in range(0,len(date0)):
        if(date.count(date0[i])>temp): 
            DATA0=date0[i]
            temp=date.count(date0[i])
    
    
    D1 = re.findall(r'\d+', goans1) # DATA ans_1
    date = []
    
    for i in range(0,len(D1)): 
        if(len(D1[i])==4): 
            date.append(D1[i])
                
    date1 = list(set(date))
    DATA1 = 0
    temp = 0
    
    for i in range(0,len(date1)):
        if(date.count(date1[i])>temp): 
            DATA1=date1[i]
            temp=date.count(date1[i])
    
    D2 = re.findall(r'\d+', goans2) # DATA ans_2
    date = []
    
    for i in range(0,len(D2)): 
        if(len(D2[i])==4): 
            date.append(D2[i])
                
    date2 = list(set(date))
    DATA2 = 0
    temp = 0
    
    for i in range(0,len(date2)):
        if(date.count(date2[i])>temp): 
            DATA2=date2[i]
            temp=date.count(date2[i])

    D3 = re.findall(r'\d+', goans3) # DATA ans_3
    date = []
    
    for i in range(0,len(D3)): 
        if(len(D3[i])==4): 
            date.append(D3[i])
                
    date3 = list(set(date))
    DATA3 = 0
    temp = 0
    
    for i in range(0,len(date3)):
        if(date.count(date3[i])>temp): 
            DATA3=date3[i]
            temp=date.count(date3[i])
    
    date0 = list(map(int, date0))
    date1 = list(map(int, date1))
    date2 = list(map(int, date2))
    date3 = list(map(int, date3))

    print("All the datas:")
    print(colored(date0,"white"))
    print(colored(date1,"white"))
    print(colored(date2,"white"))
    print(colored(date3,"white"))
                
    print('Check date: ', end ="")
    print(colored(str(DATA0)+", ","red"), end ="")
    print(colored(str(DATA1)+", "+str(DATA2)+", "+str(DATA3),"yellow"))

    exception=0
    if(DATA0==0 or DATA1==0 or DATA2==0 or DATA3==0): 
        exception=1
        print(colored("ZEROS EXCEPTION",'red'))
    if(DATA0!=DATA1 or DATA0!=DATA2 or DATA0!=DATA3): 
        exception=1
        print(colored("NO MATCHES FOUND",'red'))
    
    if(DATA0==DATA1 and exception==0):
        print(colored("A",'red'))  
    if(DATA0==DATA2 and exception==0):
        print(colored("B",'red'))
    if(DATA0==DATA3 and exception==0):
        print(colored("C",'red'))
    
    os.remove(os.path.join(DIR,'cache','goans1.txt'))
    os.remove(os.path.join(DIR,'cache','goans2.txt'))
    os.remove(os.path.join(DIR,'cache','goans3.txt'))
    os.remove(os.path.join(DIR,'cache','googling.txt'))
    


# In[ ]:


# Entrambe -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if(entrambe==1):
    
    ans_1=open(os.path.join(DIR,'cache','ans_1.txt')).read().replace('\ufeff','').strip().replace("|","I")
    ans_1F=ans_1 #full
    ans_1=ans_1.split() 
    ans_2=open(os.path.join(DIR,'cache','ans_2.txt')).read().replace('\ufeff','').strip().replace("|","I")
    ans_2F=ans_2 #full
    ans_2=ans_2.split()
    ans_3=open(os.path.join(DIR,'cache','ans_3.txt')).read().replace('\ufeff','').strip().replace("|","I")
    ans_3F=ans_3 #full
    ans_3=ans_3.split()
    quest=open(os.path.join(DIR,'cache','quest.txt')).read().replace('\ufeff','').strip().replace("|","I")
    
    print('Typology: Entrambi/e')
    
    print("LINK quest:")
    print(colored(questlink,'blue'))
    
    os.system("lynx -dump "+questlink+" > "+os.path.join(DIR,'cache','googling.txt'))
    googling=codecs.open(os.path.join(DIR,'cache','googling.txt'), 'r',encoding='utf8',errors="ignore").read()
    googling=' '.join(googling.split())
    
    
    if(ans_3F.find("Entrambe")>-1 or ans_3F.find("Entrambi")>-1): # Entrambe è la risposta 3
        
        todelete=[] # filtraggio ans_1
        
        for i in range(0,len(BOW)):
            for j in range(0,len(ans_1)):
                BOWi=" "+BOW[i]+" "
                ans_1j=" "+ans_1[j]+" "
                if(BOWi.lower().find(ans_1j.lower())>-1):
                    todelete.append(ans_1[j])
                if(len(ans_1[j])==1 and ans_1[j].find("1")>-1): todelete.append(ans_1[j])
                if(len(ans_1[j])==1 and ans_1[j].find("2")>-1): ans_1[j]="due"
                if(len(ans_1[j])==1 and ans_1[j].find("3")>-1): ans_1[j]="tre"
                if(len(ans_1[j])==1 and ans_1[j].find("4")>-1): ans_1[j]="quattro"            
                if(len(ans_1[j])==1 and ans_1[j].find("5")>-1): ans_1[j]="cinque"            
                if(len(ans_1[j])==1 and ans_1[j].find("6")>-1): ans_1[j]="sei"            
                if(len(ans_1[j])==1 and ans_1[j].find("7")>-1): ans_1[j]="sette"
                if(len(ans_1[j])==1 and ans_1[j].find("8")>-1): ans_1[j]="otto"            
                if(len(ans_1[j])==1 and ans_1[j].find("9")>-1): ans_1[j]="nove"           
                if(len(ans_1[j])==2 and ans_1[j].find("10")>-1): ans_1[j]="dieci"               
    
        
        for k in range(0,len(todelete)):
            ans_1.remove(todelete[k])
            
        ans_1temp=' '.join(ans_1).split()
    
        for i in range(0,len(acc)):
            for j in range(0,len(ans_1temp)):
                temp=list(ans_1temp[j])
                temp[-1]=acc[i]
                temp=str(''.join(temp))
                ans_1.append(temp)
                
        
        ca1 = (googling.count(" "+ans_1F+" ") + googling.count(" "+ans_1F.lower()+" ") + 
               googling.count(" "+ans_1F+".") + googling.count(" "+ans_1F.lower()+".") +
               googling.count(" "+ans_1F+",") + googling.count(" "+ans_1F.lower()+",") +
               googling.count(" "+ans_1F+":") + googling.count(" "+ans_1F.lower()+":") +
               googling.count(" "+ans_1F+";") + googling.count(" "+ans_1F.lower()+";") +
               googling.count(" "+ans_1F+")") + googling.count(" "+ans_1F.lower()+")") +
               googling.count("("+ans_1F+" ") + googling.count("("+ans_1F.lower()+" ") +
               googling.count('"'+ans_1F+' ') + googling.count('"'+ans_1F.lower()+' ') +
               googling.count(' '+ans_1F+'"') + googling.count(' '+ans_1F.lower()+'"')) 
        
        for i in range(0,len(ans_1)):
            ca1 = (googling.count(" "+ans_1[i]+" ") + googling.count(" "+ans_1[i].lower()+" ") + 
                   googling.count(" "+ans_1[i]+".") + googling.count(" "+ans_1[i].lower()+".") + 
                   googling.count(" "+ans_1[i]+",") + googling.count(" "+ans_1[i].lower()+",") +
                   googling.count(" "+ans_1[i]+":") + googling.count(" "+ans_1[i].lower()+":") +
                   googling.count(" "+ans_1[i]+";") + googling.count(" "+ans_1[i].lower()+";") +
                   googling.count(" "+ans_1[i]+")") + googling.count(" "+ans_1[i].lower()+")") +
                   googling.count("("+ans_1[i]+" ") + googling.count("("+ans_1[i].lower()+" ") +
                   googling.count('"'+ans_1[i]+' ') + googling.count('"'+ans_1[i].lower()+' ') +
                   googling.count(' '+ans_1[i]+'"') + googling.count(" "+ans_1[i].lower()+'"') + ca1)
        
        todelete=[] # filtraggio ans_2
        
        for i in range(0,len(BOW)):
            for j in range(0,len(ans_2)):
                BOWi=" "+BOW[i]+" "
                ans_2j=" "+ans_2[j]+" "
                if(BOWi.lower().find(ans_2j.lower())>-1):
                    todelete.append(ans_2[j])
                if(len(ans_2[j])==1 and ans_2[j].find("1")>-1): todelete.append(ans_2[j])
                if(len(ans_2[j])==1 and ans_2[j].find("2")>-1): ans_2[j]="due"
                if(len(ans_2[j])==1 and ans_2[j].find("3")>-1): ans_2[j]="tre"
                if(len(ans_2[j])==1 and ans_2[j].find("4")>-1): ans_2[j]="quattro"            
                if(len(ans_2[j])==1 and ans_2[j].find("5")>-1): ans_2[j]="cinque"            
                if(len(ans_2[j])==1 and ans_2[j].find("6")>-1): ans_2[j]="sei"            
                if(len(ans_2[j])==1 and ans_2[j].find("7")>-1): ans_2[j]="sette"
                if(len(ans_2[j])==1 and ans_2[j].find("8")>-1): ans_2[j]="otto"            
                if(len(ans_2[j])==1 and ans_2[j].find("9")>-1): ans_2[j]="nove"           
                if(len(ans_2[j])==2 and ans_2[j].find("10")>-1): ans_2[j]="dieci"  

        for k in range(0,len(todelete)):
            ans_2.remove(todelete[k])
            
        ans_2temp=' '.join(ans_2).split()
    
        for i in range(0,len(acc)):
            for j in range(0,len(ans_2temp)):
                temp=list(ans_2temp[j])
                temp[-1]=acc[i]
                temp=str(''.join(temp))
                ans_2.append(temp)
        
        ca2 = (googling.count(" "+ans_2F+" ") + googling.count(" "+ans_2F.lower()+" ") + 
               googling.count(" "+ans_2F+".") + googling.count(" "+ans_2F.lower()+".") +
               googling.count(" "+ans_2F+",") + googling.count(" "+ans_2F.lower()+",") +
               googling.count(" "+ans_2F+":") + googling.count(" "+ans_2F.lower()+":") +
               googling.count(" "+ans_2F+";") + googling.count(" "+ans_2F.lower()+";") +
               googling.count(" "+ans_2F+")") + googling.count(" "+ans_2F.lower()+")") +
               googling.count("("+ans_2F+" ") + googling.count("("+ans_2F.lower()+" ") +
               googling.count('"'+ans_2F+' ') + googling.count('"'+ans_2F.lower()+' ') +
               googling.count(' '+ans_2F+'"') + googling.count(' '+ans_2F.lower()+'"')) 
        
        for i in range(0,len(ans_2)):
            ca2 = (googling.count(" "+ans_2[i]+" ") + googling.count(" "+ans_2[i].lower()+" ") + 
                   googling.count(" "+ans_2[i]+".") + googling.count(" "+ans_2[i].lower()+".") + 
                   googling.count(" "+ans_2[i]+",") + googling.count(" "+ans_2[i].lower()+",") +
                   googling.count(" "+ans_2[i]+":") + googling.count(" "+ans_2[i].lower()+":") +
                   googling.count(" "+ans_2[i]+";") + googling.count(" "+ans_2[i].lower()+";") +
                   googling.count(" "+ans_2[i]+")") + googling.count(" "+ans_2[i].lower()+")") +
                   googling.count("("+ans_2[i]+" ") + googling.count("("+ans_2[i].lower()+" ") +
                   googling.count('"'+ans_2[i]+' ') + googling.count('"'+ans_2[i].lower()+' ') +
                   googling.count(' '+ans_2[i]+'"') + googling.count(" "+ans_2[i].lower()+'"') + ca2)
    
        p1=(100/(ca1+ca2+0.000001))*ca1
        p2=(100/(ca1+ca2+0.000001))*ca2
        
        print("Words searched:")
        print(colored(ans_1,"yellow"))
        print(colored(ans_2,"yellow"))
        
        exception=0
        
        if(len(ans_1)==0 or len(ans_2)==0 or len(ans_3)==0 and exception==0): 
            exception=1
            print(colored('VOID ANSWERS','red'))
            print(colored('A: '+str(p1),'red'))
            print(colored('B: '+str(p2),'red'))
            
        if(ca1==0 and ca2==ca1):
            exception=1
            print(colored("NO MATCHES FOUND","red"))
        
        ent=0
        
        if(ca1!=0 and ca2!=0 and exception==0):
            print(colored("C: Entrambi/e",'red'))
            ent=1
        if(ca1!=0 and ca1>ca2 and exception==0 and ent==0):
            print(colored("A: " + ans_1F,'red'))
            print("Percentage: "+ str(p1)+"%")
        if(ca2!=0 and ca2>ca1 and exception==0 and ent==0):
            print(colored("B: " + ans_2F,'red'))
            print("Percentage: "+ str(p2)+"%")

    if(ans_2F.find("Entrambe")>-1 or ans_2F.find("Entrambi")>-1): # Entrambe è la risposta 2
       
        todelete=[] # filtraggio ans_1
    
        for i in range(0,len(BOW)):
            for j in range(0,len(ans_1)):
                BOWi=" "+BOW[i]+" "
                ans_1j=" "+ans_1[j]+" "
                if(BOWi.lower().find(ans_1j.lower())>-1):
                    todelete.append(ans_1[j])
                if(len(ans_1[j])==1 and ans_1[j].find("1")>-1): todelete.append(ans_1[j])
                if(len(ans_1[j])==1 and ans_1[j].find("2")>-1): ans_1[j]="due"
                if(len(ans_1[j])==1 and ans_1[j].find("3")>-1): ans_1[j]="tre"
                if(len(ans_1[j])==1 and ans_1[j].find("4")>-1): ans_1[j]="quattro"            
                if(len(ans_1[j])==1 and ans_1[j].find("5")>-1): ans_1[j]="cinque"            
                if(len(ans_1[j])==1 and ans_1[j].find("6")>-1): ans_1[j]="sei"            
                if(len(ans_1[j])==1 and ans_1[j].find("7")>-1): ans_1[j]="sette"
                if(len(ans_1[j])==1 and ans_1[j].find("8")>-1): ans_1[j]="otto"            
                if(len(ans_1[j])==1 and ans_1[j].find("9")>-1): ans_1[j]="nove"           
                if(len(ans_1[j])==2 and ans_1[j].find("10")>-1): ans_1[j]="dieci"    
            
        for k in range(0,len(todelete)):
            ans_1.remove(todelete[k])
            
        ans_1temp=' '.join(ans_1).split()
    
        for i in range(0,len(acc)):
            for j in range(0,len(ans_1temp)):
                temp=list(ans_1temp[j])
                temp[-1]=acc[i]
                temp=str(''.join(temp))
                ans_1.append(temp)

        
        ca1 = (googling.count(" "+ans_1F+" ") + googling.count(" "+ans_1F.lower()+" ") + 
               googling.count(" "+ans_1F+".") + googling.count(" "+ans_1F.lower()+".") +
               googling.count(" "+ans_1F+",") + googling.count(" "+ans_1F.lower()+",") +
               googling.count(" "+ans_1F+":") + googling.count(" "+ans_1F.lower()+":") +
               googling.count(" "+ans_1F+";") + googling.count(" "+ans_1F.lower()+";") +
               googling.count(" "+ans_1F+")") + googling.count(" "+ans_1F.lower()+")") +
               googling.count("("+ans_1F+" ") + googling.count("("+ans_1F.lower()+" ") +
               googling.count('"'+ans_1F+' ') + googling.count('"'+ans_1F.lower()+' ') +
               googling.count(' '+ans_1F+'"') + googling.count(' '+ans_1F.lower()+'"')) 
        
        for i in range(0,len(ans_1)):
            ca1 = (googling.count(" "+ans_1[i]+" ") + googling.count(" "+ans_1[i].lower()+" ") + 
                   googling.count(" "+ans_1[i]+".") + googling.count(" "+ans_1[i].lower()+".") + 
                   googling.count(" "+ans_1[i]+",") + googling.count(" "+ans_1[i].lower()+",") +
                   googling.count(" "+ans_1[i]+":") + googling.count(" "+ans_1[i].lower()+":") +
                   googling.count(" "+ans_1[i]+";") + googling.count(" "+ans_1[i].lower()+";") +
                   googling.count(" "+ans_1[i]+")") + googling.count(" "+ans_1[i].lower()+")") +
                   googling.count("("+ans_1[i]+" ") + googling.count("("+ans_1[i].lower()+" ") +
                   googling.count('"'+ans_1[i]+' ') + googling.count('"'+ans_1[i].lower()+' ') +
                   googling.count(' '+ans_1[i]+'"') + googling.count(" "+ans_1[i].lower()+'"') + ca1)
        
        todelete=[] # filtraggio ans_3
        
        for i in range(0,len(BOW)):
            for j in range(0,len(ans_3)):
                BOWi=" "+BOW[i]+" "
                ans_3j=" "+ans_3[j]+" "
                if(BOWi.lower().find(ans_3j.lower())>-1):
                    todelete.append(ans_3[j])
                if(len(ans_3[j])==1 and ans_3[j].find("1")>-1): todelete.append(ans_3[j])
                if(len(ans_3[j])==1 and ans_3[j].find("2")>-1): ans_3[j]="due"
                if(len(ans_3[j])==1 and ans_3[j].find("3")>-1): ans_3[j]="tre"
                if(len(ans_3[j])==1 and ans_3[j].find("4")>-1): ans_3[j]="quattro"            
                if(len(ans_3[j])==1 and ans_3[j].find("5")>-1): ans_3[j]="cinque"            
                if(len(ans_3[j])==1 and ans_3[j].find("6")>-1): ans_3[j]="sei"            
                if(len(ans_3[j])==1 and ans_3[j].find("7")>-1): ans_3[j]="sette"
                if(len(ans_3[j])==1 and ans_3[j].find("8")>-1): ans_3[j]="otto"            
                if(len(ans_3[j])==1 and ans_3[j].find("9")>-1): ans_3[j]="nove"           
                if(len(ans_3[j])==2 and ans_3[j].find("10")>-1): ans_3[j]="dieci"    

                    
        for k in range(0,len(todelete)):
            ans_3.remove(todelete[k])
            
        ans_3temp=' '.join(ans_3).split()
    
        for i in range(0,len(acc)):
            for j in range(0,len(ans_3temp)):
                temp=list(ans_3temp[j])
                temp[-1]=acc[i]
                temp=str(''.join(temp))
                ans_3.append(temp)

        
        ca3 = (googling.count(" "+ans_3F+" ") + googling.count(" "+ans_3F.lower()+" ") + 
               googling.count(" "+ans_3F+".") + googling.count(" "+ans_3F.lower()+".") +
               googling.count(" "+ans_3F+",") + googling.count(" "+ans_3F.lower()+",") +
               googling.count(" "+ans_3F+":") + googling.count(" "+ans_3F.lower()+":") +
               googling.count(" "+ans_3F+";") + googling.count(" "+ans_3F.lower()+";") +
               googling.count(" "+ans_3F+")") + googling.count(" "+ans_3F.lower()+")") +
               googling.count("("+ans_3F+" ") + googling.count("("+ans_3F.lower()+" ") +
               googling.count('"'+ans_3F+' ') + googling.count('"'+ans_3F.lower()+' ') +
               googling.count(' '+ans_3F+'"') + googling.count(' '+ans_3F.lower()+'"')) 
        
        for i in range(0,len(ans_3)):
            ca3 = (googling.count(" "+ans_3[i]+" ") + googling.count(" "+ans_3[i].lower()+" ") + 
                   googling.count(" "+ans_3[i]+".") + googling.count(" "+ans_3[i].lower()+".") + 
                   googling.count(" "+ans_3[i]+",") + googling.count(" "+ans_3[i].lower()+",") +
                   googling.count(" "+ans_3[i]+":") + googling.count(" "+ans_3[i].lower()+":") +
                   googling.count(" "+ans_3[i]+";") + googling.count(" "+ans_3[i].lower()+";") +
                   googling.count(" "+ans_3[i]+")") + googling.count(" "+ans_3[i].lower()+")") +
                   googling.count("("+ans_3[i]+" ") + googling.count("("+ans_3[i].lower()+" ") +
                   googling.count('"'+ans_3[i]+' ') + googling.count('"'+ans_3[i].lower()+' ') +
                   googling.count(' '+ans_3[i]+'"') + googling.count(" "+ans_3[i].lower()+'"') + ca3)
    
        p1=(100/(ca1+ca3+0.000001))*ca1
        p3=(100/(ca1+ca3+0.000001))*ca3
        
        print("Words searched:")
        print(colored(ans_1,"yellow"))
        print(colored(ans_3,"yellow"))
        
        exception=0
        
        if(len(ans_1)==0 or len(ans_2)==0 or len(ans_3)==0 and exception==0): 
            exception=1
            print(colored('VOID ANSWERS','red'))
            print(colored('A: '+str(p1),'red'))
            print(colored('C: '+str(p3),'red'))
            
        if(ca1==0 and ca3==ca1):
            exception=1
            print(colored("NO MATCHES FOUND","red"))
        
        ent=0
        
        if(ca1!=0 and ca3!=0 and exception==0):
            print(colored("B: Entrambi/e",'red'))
            ent=1
        if(ca1!=0 and ca1>ca3 and exception==0 and ent==0):
            print(colored("A: " + ans_1F,'red'))
            print("Percentage: "+ str(p1)+"%")
        if(ca3!=0 and ca3>ca1 and exception==0 and ent==0):
            print(colored("C: " + ans_3F,'red'))
            print("Percentage: "+ str(p3)+"%")
                
    
    if(ans_1F.find("Entrambe")>-1 or ans_1F.find("Entrambi")>-1): # Entrambe è la risposta 1
        
        todelete=[] # filtraggio ans_2
        
        for i in range(0,len(BOW)):
            for j in range(0,len(ans_2)):
                BOWi=" "+BOW[i]+" "
                ans_2j=" "+ans_2[j]+" "
                if(BOWi.lower().find(ans_2j.lower())>-1):
                    todelete.append(ans_2[j])
                if(len(ans_2[j])==1 and ans_2[j].find("1")>-1): todelete.append(ans_2[j])
                if(len(ans_2[j])==1 and ans_2[j].find("2")>-1): ans_2[j]="due"
                if(len(ans_2[j])==1 and ans_2[j].find("3")>-1): ans_2[j]="tre"
                if(len(ans_2[j])==1 and ans_2[j].find("4")>-1): ans_2[j]="quattro"            
                if(len(ans_2[j])==1 and ans_2[j].find("5")>-1): ans_2[j]="cinque"            
                if(len(ans_2[j])==1 and ans_2[j].find("6")>-1): ans_2[j]="sei"            
                if(len(ans_2[j])==1 and ans_2[j].find("7")>-1): ans_2[j]="sette"
                if(len(ans_2[j])==1 and ans_2[j].find("8")>-1): ans_2[j]="otto"            
                if(len(ans_2[j])==1 and ans_2[j].find("9")>-1): ans_2[j]="nove"           
                if(len(ans_2[j])==2 and ans_2[j].find("10")>-1): ans_2[j]="dieci"  
            
        for k in range(0,len(todelete)):
            ans_2.remove(todelete[k])
            
        ans_2temp=' '.join(ans_2).split()
    
        for i in range(0,len(acc)):
            for j in range(0,len(ans_2temp)):
                temp=list(ans_2temp[j])
                temp[-1]=acc[i]
                temp=str(''.join(temp))
                ans_2.append(temp)
                
        
        ca2 = (googling.count(" "+ans_2F+" ") + googling.count(" "+ans_2F.lower()+" ") + 
               googling.count(" "+ans_2F+".") + googling.count(" "+ans_2F.lower()+".") +
               googling.count(" "+ans_2F+",") + googling.count(" "+ans_2F.lower()+",") +
               googling.count(" "+ans_2F+":") + googling.count(" "+ans_2F.lower()+":") +
               googling.count(" "+ans_2F+";") + googling.count(" "+ans_2F.lower()+";") +
               googling.count(" "+ans_2F+")") + googling.count(" "+ans_2F.lower()+")") +
               googling.count("("+ans_2F+" ") + googling.count("("+ans_2F.lower()+" ") +
               googling.count('"'+ans_2F+' ') + googling.count('"'+ans_2F.lower()+' ') +
               googling.count(' '+ans_2F+'"') + googling.count(' '+ans_2F.lower()+'"')) 
        
        for i in range(0,len(ans_2)):
            ca2 = (googling.count(" "+ans_2[i]+" ") + googling.count(" "+ans_2[i].lower()+" ") + 
                   googling.count(" "+ans_2[i]+".") + googling.count(" "+ans_2[i].lower()+".") + 
                   googling.count(" "+ans_2[i]+",") + googling.count(" "+ans_2[i].lower()+",") +
                   googling.count(" "+ans_2[i]+":") + googling.count(" "+ans_2[i].lower()+":") +
                   googling.count(" "+ans_2[i]+";") + googling.count(" "+ans_2[i].lower()+";") +
                   googling.count(" "+ans_2[i]+")") + googling.count(" "+ans_2[i].lower()+")") +
                   googling.count("("+ans_2[i]+" ") + googling.count("("+ans_2[i].lower()+" ") +
                   googling.count('"'+ans_2[i]+' ') + googling.count('"'+ans_2[i].lower()+' ') +
                   googling.count(' '+ans_2[i]+'"') + googling.count(" "+ans_2[i].lower()+'"') + ca2)
        
        todelete=[] # filtraggio ans_3
        
        for i in range(0,len(BOW)):
            for j in range(0,len(ans_3)):
                BOWi=" "+BOW[i]+" "
                ans_3j=" "+ans_3[j]+" "
                if(BOWi.lower().find(ans_3j.lower())>-1):
                    todelete.append(ans_3[j])
                if(len(ans_3[j])==1 and ans_3[j].find("1")>-1): todelete.append(ans_3[j])
                if(len(ans_3[j])==1 and ans_3[j].find("2")>-1): ans_3[j]="due"
                if(len(ans_3[j])==1 and ans_3[j].find("3")>-1): ans_3[j]="tre"
                if(len(ans_3[j])==1 and ans_3[j].find("4")>-1): ans_3[j]="quattro"            
                if(len(ans_3[j])==1 and ans_3[j].find("5")>-1): ans_3[j]="cinque"            
                if(len(ans_3[j])==1 and ans_3[j].find("6")>-1): ans_3[j]="sei"            
                if(len(ans_3[j])==1 and ans_3[j].find("7")>-1): ans_3[j]="sette"
                if(len(ans_3[j])==1 and ans_3[j].find("8")>-1): ans_3[j]="otto"            
                if(len(ans_3[j])==1 and ans_3[j].find("9")>-1): ans_3[j]="nove"           
                if(len(ans_3[j])==2 and ans_3[j].find("10")>-1): ans_3[j]="dieci"    
        
        for k in range(0,len(todelete)):
            ans_3.remove(todelete[k])
            
        ans_3temp=' '.join(ans_3).split()
    
        for i in range(0,len(acc)):
            for j in range(0,len(ans_3temp)):
                temp=list(ans_3temp[j])
                temp[-1]=acc[i]
                temp=str(''.join(temp))
                ans_3.append(temp)

        
        ca3 = (googling.count(" "+ans_3F+" ") + googling.count(" "+ans_3F.lower()+" ") + 
               googling.count(" "+ans_3F+".") + googling.count(" "+ans_3F.lower()+".") +
               googling.count(" "+ans_3F+",") + googling.count(" "+ans_3F.lower()+",") +
               googling.count(" "+ans_3F+":") + googling.count(" "+ans_3F.lower()+":") +
               googling.count(" "+ans_3F+";") + googling.count(" "+ans_3F.lower()+";") +
               googling.count(" "+ans_3F+")") + googling.count(" "+ans_3F.lower()+")") +
               googling.count("("+ans_3F+" ") + googling.count("("+ans_3F.lower()+" ") +
               googling.count('"'+ans_3F+' ') + googling.count('"'+ans_3F.lower()+' ') +
               googling.count(' '+ans_3F+'"') + googling.count(' '+ans_3F.lower()+'"')) 
        
        for i in range(0,len(ans_3)):
            ca3 = (googling.count(" "+ans_3[i]+" ") + googling.count(" "+ans_3[i].lower()+" ") + 
                   googling.count(" "+ans_3[i]+".") + googling.count(" "+ans_3[i].lower()+".") + 
                   googling.count(" "+ans_3[i]+",") + googling.count(" "+ans_3[i].lower()+",") +
                   googling.count(" "+ans_3[i]+":") + googling.count(" "+ans_3[i].lower()+":") +
                   googling.count(" "+ans_3[i]+";") + googling.count(" "+ans_3[i].lower()+";") +
                   googling.count(" "+ans_3[i]+")") + googling.count(" "+ans_3[i].lower()+")") +
                   googling.count("("+ans_3[i]+" ") + googling.count("("+ans_3[i].lower()+" ") +
                   googling.count('"'+ans_3[i]+' ') + googling.count('"'+ans_3[i].lower()+' ') +
                   googling.count(' '+ans_3[i]+'"') + googling.count(" "+ans_3[i].lower()+'"') + ca3)
        
        p2=(100/(ca2+ca3+0.000001))*ca2
        p3=(100/(ca2+ca3+0.000001))*ca3
        
        print("Words searched:")
        print(colored(ans_2,"yellow"))
        print(colored(ans_3,"yellow"))
        
        exception=0
        
        if(len(ans_1)==0 or len(ans_2)==0 or len(ans_3)==0 and exception==0): 
            exception=1
            print(colored('VOID ANSWERS','red'))
            print(colored('B: '+str(p2),'red'))
            print(colored('C: '+str(p3),'red'))
            
        if(ca3==0 and ca3==ca2):
            exception=1
            print(colored("NO MATCHES FOUND","red"))
        
        ent=0
        
        if(ca2!=0 and ca3!=0 and exception==0):
            print(colored("A: Entrambi/e",'red'))
            ent=1
        if(ca2!=0 and ca2>ca3 and exception==0 and ent==0):
            print(colored("B: " + ans_2F,'red'))
            print("Percentage: "+ str(p2)+"%")
        if(ca3!=0 and ca3>ca2 and exception==0 and ent==0):
            print(colored("C: " + ans_3F,'red'))
            print("Percentage: "+ str(p3)+"%")
    
    os.remove(os.path.join(DIR,'cache','googling.txt'))
    
    


# In[ ]:


# Nessuno -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if(nessuno==1):
    
    ans_1=open(os.path.join(DIR,'cache','ans_1.txt')).read().replace('\ufeff','').strip().replace("|","I")
    ans_1F=ans_1 #full
    ans_1=ans_1.split() 
    ans_2=open(os.path.join(DIR,'cache','ans_2.txt')).read().replace('\ufeff','').strip().replace("|","I")
    ans_2F=ans_2 #full
    ans_2=ans_2.split()
    ans_3=open(os.path.join(DIR,'cache','ans_3.txt')).read().replace('\ufeff','').strip().replace("|","I")
    ans_3F=ans_3 #full
    ans_3=ans_3.split()
    quest=open(os.path.join(DIR,'cache','quest.txt')).read().replace('\ufeff','').strip().replace("|","I")
    
    print('Typology: Nessuno/a')
    
    print("LINK quest:")
    print(colored(questlink,'blue'))
    
    os.system("lynx -dump "+questlink+" > "+os.path.join(DIR,'cache','googling.txt'))
    googling=codecs.open(os.path.join(DIR,'cache','googling.txt'), 'r',encoding='utf8',errors="ignore").read()
    googling=' '.join(googling.split())
    
    
    if(ans_3F.find("Nessuno")>-1 or ans_3F.find("Nessuna")>-1): # Nessuno/a è la risposta 3
        
        todelete=[] # filtraggio ans_1
        
        for i in range(0,len(BOW)):
            for j in range(0,len(ans_1)):
                BOWi=" "+BOW[i]+" "
                ans_1j=" "+ans_1[j]+" "
                if(BOWi.lower().find(ans_1j.lower())>-1):
                    todelete.append(ans_1[j])
                if(len(ans_1[j])==1 and ans_1[j].find("1")>-1): todelete.append(ans_1[j])
                if(len(ans_1[j])==1 and ans_1[j].find("2")>-1): ans_1[j]="due"
                if(len(ans_1[j])==1 and ans_1[j].find("3")>-1): ans_1[j]="tre"
                if(len(ans_1[j])==1 and ans_1[j].find("4")>-1): ans_1[j]="quattro"            
                if(len(ans_1[j])==1 and ans_1[j].find("5")>-1): ans_1[j]="cinque"            
                if(len(ans_1[j])==1 and ans_1[j].find("6")>-1): ans_1[j]="sei"            
                if(len(ans_1[j])==1 and ans_1[j].find("7")>-1): ans_1[j]="sette"
                if(len(ans_1[j])==1 and ans_1[j].find("8")>-1): ans_1[j]="otto"            
                if(len(ans_1[j])==1 and ans_1[j].find("9")>-1): ans_1[j]="nove"           
                if(len(ans_1[j])==2 and ans_1[j].find("10")>-1): ans_1[j]="dieci"               
    
        
        for k in range(0,len(todelete)):
            ans_1.remove(todelete[k])
            
        ans_1temp=' '.join(ans_1).split()
    
        for i in range(0,len(acc)):
            for j in range(0,len(ans_1temp)):
                temp=list(ans_1temp[j])
                temp[-1]=acc[i]
                temp=str(''.join(temp))
                ans_1.append(temp)

        
        ca1 = (googling.count(" "+ans_1F+" ") + googling.count(" "+ans_1F.lower()+" ") + 
               googling.count(" "+ans_1F+".") + googling.count(" "+ans_1F.lower()+".") +
               googling.count(" "+ans_1F+",") + googling.count(" "+ans_1F.lower()+",") +
               googling.count(" "+ans_1F+":") + googling.count(" "+ans_1F.lower()+":") +
               googling.count(" "+ans_1F+";") + googling.count(" "+ans_1F.lower()+";") +
               googling.count(" "+ans_1F+")") + googling.count(" "+ans_1F.lower()+")") +
               googling.count("("+ans_1F+" ") + googling.count("("+ans_1F.lower()+" ") +
               googling.count('"'+ans_1F+' ') + googling.count('"'+ans_1F.lower()+' ') +
               googling.count(' '+ans_1F+'"') + googling.count(' '+ans_1F.lower()+'"')) 
        
        for i in range(0,len(ans_1)):
            ca1 = (googling.count(" "+ans_1[i]+" ") + googling.count(" "+ans_1[i].lower()+" ") + 
                   googling.count(" "+ans_1[i]+".") + googling.count(" "+ans_1[i].lower()+".") + 
                   googling.count(" "+ans_1[i]+",") + googling.count(" "+ans_1[i].lower()+",") +
                   googling.count(" "+ans_1[i]+":") + googling.count(" "+ans_1[i].lower()+":") +
                   googling.count(" "+ans_1[i]+";") + googling.count(" "+ans_1[i].lower()+";") +
                   googling.count(" "+ans_1[i]+")") + googling.count(" "+ans_1[i].lower()+")") +
                   googling.count("("+ans_1[i]+" ") + googling.count("("+ans_1[i].lower()+" ") +
                   googling.count('"'+ans_1[i]+' ') + googling.count('"'+ans_1[i].lower()+' ') +
                   googling.count(' '+ans_1[i]+'"') + googling.count(" "+ans_1[i].lower()+'"') + ca1)
        
        todelete=[] # filtraggio ans_2
        
        for i in range(0,len(BOW)):
            for j in range(0,len(ans_2)):
                BOWi=" "+BOW[i]+" "
                ans_2j=" "+ans_2[j]+" "
                if(BOWi.lower().find(ans_2j.lower())>-1):
                    todelete.append(ans_2[j])
                if(len(ans_2[j])==1 and ans_2[j].find("1")>-1): todelete.append(ans_2[j])
                if(len(ans_2[j])==1 and ans_2[j].find("2")>-1): ans_2[j]="due"
                if(len(ans_2[j])==1 and ans_2[j].find("3")>-1): ans_2[j]="tre"
                if(len(ans_2[j])==1 and ans_2[j].find("4")>-1): ans_2[j]="quattro"            
                if(len(ans_2[j])==1 and ans_2[j].find("5")>-1): ans_2[j]="cinque"            
                if(len(ans_2[j])==1 and ans_2[j].find("6")>-1): ans_2[j]="sei"            
                if(len(ans_2[j])==1 and ans_2[j].find("7")>-1): ans_2[j]="sette"
                if(len(ans_2[j])==1 and ans_2[j].find("8")>-1): ans_2[j]="otto"            
                if(len(ans_2[j])==1 and ans_2[j].find("9")>-1): ans_2[j]="nove"           
                if(len(ans_2[j])==2 and ans_2[j].find("10")>-1): ans_2[j]="dieci"  


        for k in range(0,len(todelete)):
            ans_2.remove(todelete[k])
            
        ans_2temp=' '.join(ans_2).split()
    
        for i in range(0,len(acc)):
            for j in range(0,len(ans_2temp)):
                temp=list(ans_2temp[j])
                temp[-1]=acc[i]
                temp=str(''.join(temp))
                ans_2.append(temp)
                
        
        ca2 = (googling.count(" "+ans_2F+" ") + googling.count(" "+ans_2F.lower()+" ") + 
               googling.count(" "+ans_2F+".") + googling.count(" "+ans_2F.lower()+".") +
               googling.count(" "+ans_2F+",") + googling.count(" "+ans_2F.lower()+",") +
               googling.count(" "+ans_2F+":") + googling.count(" "+ans_2F.lower()+":") +
               googling.count(" "+ans_2F+";") + googling.count(" "+ans_2F.lower()+";") +
               googling.count(" "+ans_2F+")") + googling.count(" "+ans_2F.lower()+")") +
               googling.count("("+ans_2F+" ") + googling.count("("+ans_2F.lower()+" ") +
               googling.count('"'+ans_2F+' ') + googling.count('"'+ans_2F.lower()+' ') +
               googling.count(' '+ans_2F+'"') + googling.count(' '+ans_2F.lower()+'"')) 
        
        for i in range(0,len(ans_2)):
            ca2 = (googling.count(" "+ans_2[i]+" ") + googling.count(" "+ans_2[i].lower()+" ") + 
                   googling.count(" "+ans_2[i]+".") + googling.count(" "+ans_2[i].lower()+".") + 
                   googling.count(" "+ans_2[i]+",") + googling.count(" "+ans_2[i].lower()+",") +
                   googling.count(" "+ans_2[i]+":") + googling.count(" "+ans_2[i].lower()+":") +
                   googling.count(" "+ans_2[i]+";") + googling.count(" "+ans_2[i].lower()+";") +
                   googling.count(" "+ans_2[i]+")") + googling.count(" "+ans_2[i].lower()+")") +
                   googling.count("("+ans_2[i]+" ") + googling.count("("+ans_2[i].lower()+" ") +
                   googling.count('"'+ans_2[i]+' ') + googling.count('"'+ans_2[i].lower()+' ') +
                   googling.count(' '+ans_2[i]+'"') + googling.count(" "+ans_2[i].lower()+'"') + ca2)
    
        p1=(100/(ca1+ca2+0.000001))*ca1
        p2=(100/(ca1+ca2+0.000001))*ca2
        
        print("Words searched:")
        print(colored(ans_1,"yellow"))
        print(colored(ans_2,"yellow"))
        
        exception=0
        
        if(len(ans_1)==0 or len(ans_2)==0 or len(ans_3)==0 and exception==0): 
            exception=1
            print(colored('VOID ANSWERS','red'))
            print(colored('A: '+str(p1),'red'))
            print(colored('B: '+str(p2),'red'))
            
        if(ca1!=0 and ca2==ca1):
            exception=1
            print(colored("MATCHES FOUND: A or B","red"))
            
        nes=0
        
        if(ca1==0 and ca2==0 and exception==0):
            print(colored("C: Nessuno/a",'red'))
            nes=1
        if(ca1!=0 and ca1>ca2 and exception==0 and nes==0):
            print(colored("A: " + ans_1F,'red'))
            print("Percentage: "+ str(p1)+"%")
        if(ca2!=0 and ca2>ca1 and exception==0 and nes==0):
            print(colored("B: " + ans_2F,'red'))
            print("Percentage: "+ str(p2)+"%")

    if(ans_2F.find("Nessuno")>-1 or ans_2F.find("Nessuna")>-1): # Nessuno/a è la risposta 2
       
        todelete=[] # filtraggio ans_1
    
        for i in range(0,len(BOW)):
            for j in range(0,len(ans_1)):
                BOWi=" "+BOW[i]+" "
                ans_1j=" "+ans_1[j]+" "
                if(BOWi.lower().find(ans_1j.lower())>-1):
                    todelete.append(ans_1[j])
                if(len(ans_1[j])==1 and ans_1[j].find("1")>-1): todelete.append(ans_1[j])
                if(len(ans_1[j])==1 and ans_1[j].find("2")>-1): ans_1[j]="due"
                if(len(ans_1[j])==1 and ans_1[j].find("3")>-1): ans_1[j]="tre"
                if(len(ans_1[j])==1 and ans_1[j].find("4")>-1): ans_1[j]="quattro"            
                if(len(ans_1[j])==1 and ans_1[j].find("5")>-1): ans_1[j]="cinque"            
                if(len(ans_1[j])==1 and ans_1[j].find("6")>-1): ans_1[j]="sei"            
                if(len(ans_1[j])==1 and ans_1[j].find("7")>-1): ans_1[j]="sette"
                if(len(ans_1[j])==1 and ans_1[j].find("8")>-1): ans_1[j]="otto"            
                if(len(ans_1[j])==1 and ans_1[j].find("9")>-1): ans_1[j]="nove"           
                if(len(ans_1[j])==2 and ans_1[j].find("10")>-1): ans_1[j]="dieci"    
    
        
        for k in range(0,len(todelete)):
            ans_1.remove(todelete[k])
            
        ans_1temp=' '.join(ans_1).split()
    
        for i in range(0,len(acc)):
            for j in range(0,len(ans_1temp)):
                temp=list(ans_1temp[j])
                temp[-1]=acc[i]
                temp=str(''.join(temp))
                ans_1.append(temp)

        
        ca1 = (googling.count(" "+ans_1F+" ") + googling.count(" "+ans_1F.lower()+" ") + 
               googling.count(" "+ans_1F+".") + googling.count(" "+ans_1F.lower()+".") +
               googling.count(" "+ans_1F+",") + googling.count(" "+ans_1F.lower()+",") +
               googling.count(" "+ans_1F+":") + googling.count(" "+ans_1F.lower()+":") +
               googling.count(" "+ans_1F+";") + googling.count(" "+ans_1F.lower()+";") +
               googling.count(" "+ans_1F+")") + googling.count(" "+ans_1F.lower()+")") +
               googling.count("("+ans_1F+" ") + googling.count("("+ans_1F.lower()+" ") +
               googling.count('"'+ans_1F+' ') + googling.count('"'+ans_1F.lower()+' ') +
               googling.count(' '+ans_1F+'"') + googling.count(' '+ans_1F.lower()+'"')) 
        
        for i in range(0,len(ans_1)):
            ca1 = (googling.count(" "+ans_1[i]+" ") + googling.count(" "+ans_1[i].lower()+" ") + 
                   googling.count(" "+ans_1[i]+".") + googling.count(" "+ans_1[i].lower()+".") + 
                   googling.count(" "+ans_1[i]+",") + googling.count(" "+ans_1[i].lower()+",") +
                   googling.count(" "+ans_1[i]+":") + googling.count(" "+ans_1[i].lower()+":") +
                   googling.count(" "+ans_1[i]+";") + googling.count(" "+ans_1[i].lower()+";") +
                   googling.count(" "+ans_1[i]+")") + googling.count(" "+ans_1[i].lower()+")") +
                   googling.count("("+ans_1[i]+" ") + googling.count("("+ans_1[i].lower()+" ") +
                   googling.count('"'+ans_1[i]+' ') + googling.count('"'+ans_1[i].lower()+' ') +
                   googling.count(' '+ans_1[i]+'"') + googling.count(" "+ans_1[i].lower()+'"') + ca1)
        
        todelete=[] # filtraggio ans_3
        
        for i in range(0,len(BOW)):
            for j in range(0,len(ans_3)):
                BOWi=" "+BOW[i]+" "
                ans_3j=" "+ans_3[j]+" "
                if(BOWi.lower().find(ans_3j.lower())>-1):
                    todelete.append(ans_3[j])
                if(len(ans_3[j])==1 and ans_3[j].find("1")>-1): todelete.append(ans_3[j])
                if(len(ans_3[j])==1 and ans_3[j].find("2")>-1): ans_3[j]="due"
                if(len(ans_3[j])==1 and ans_3[j].find("3")>-1): ans_3[j]="tre"
                if(len(ans_3[j])==1 and ans_3[j].find("4")>-1): ans_3[j]="quattro"            
                if(len(ans_3[j])==1 and ans_3[j].find("5")>-1): ans_3[j]="cinque"            
                if(len(ans_3[j])==1 and ans_3[j].find("6")>-1): ans_3[j]="sei"            
                if(len(ans_3[j])==1 and ans_3[j].find("7")>-1): ans_3[j]="sette"
                if(len(ans_3[j])==1 and ans_3[j].find("8")>-1): ans_3[j]="otto"            
                if(len(ans_3[j])==1 and ans_3[j].find("9")>-1): ans_3[j]="nove"           
                if(len(ans_3[j])==2 and ans_3[j].find("10")>-1): ans_3[j]="dieci"    

        for k in range(0,len(todelete)):
            ans_3.remove(todelete[k])
            
        ans_3temp=' '.join(ans_3).split()
    
        for i in range(0,len(acc)):
            for j in range(0,len(ans_3temp)):
                temp=list(ans_3temp[j])
                temp[-1]=acc[i]
                temp=str(''.join(temp))
                ans_3.append(temp)

        
        ca3 = (googling.count(" "+ans_3F+" ") + googling.count(" "+ans_3F.lower()+" ") + 
               googling.count(" "+ans_3F+".") + googling.count(" "+ans_3F.lower()+".") +
               googling.count(" "+ans_3F+",") + googling.count(" "+ans_3F.lower()+",") +
               googling.count(" "+ans_3F+":") + googling.count(" "+ans_3F.lower()+":") +
               googling.count(" "+ans_3F+";") + googling.count(" "+ans_3F.lower()+";") +
               googling.count(" "+ans_3F+")") + googling.count(" "+ans_3F.lower()+")") +
               googling.count("("+ans_3F+" ") + googling.count("("+ans_3F.lower()+" ") +
               googling.count('"'+ans_3F+' ') + googling.count('"'+ans_3F.lower()+' ') +
               googling.count(' '+ans_3F+'"') + googling.count(' '+ans_3F.lower()+'"')) 
        
        for i in range(0,len(ans_3)):
            ca3 = (googling.count(" "+ans_3[i]+" ") + googling.count(" "+ans_3[i].lower()+" ") + 
                   googling.count(" "+ans_3[i]+".") + googling.count(" "+ans_3[i].lower()+".") + 
                   googling.count(" "+ans_3[i]+",") + googling.count(" "+ans_3[i].lower()+",") +
                   googling.count(" "+ans_3[i]+":") + googling.count(" "+ans_3[i].lower()+":") +
                   googling.count(" "+ans_3[i]+";") + googling.count(" "+ans_3[i].lower()+";") +
                   googling.count(" "+ans_3[i]+")") + googling.count(" "+ans_3[i].lower()+")") +
                   googling.count("("+ans_3[i]+" ") + googling.count("("+ans_3[i].lower()+" ") +
                   googling.count('"'+ans_3[i]+' ') + googling.count('"'+ans_3[i].lower()+' ') +
                   googling.count(' '+ans_3[i]+'"') + googling.count(" "+ans_3[i].lower()+'"') + ca3)
    
        p1=(100/(ca1+ca3+0.000001))*ca1
        p3=(100/(ca1+ca3+0.000001))*ca3
        
        print("Words searched:")
        print(colored(ans_1,"yellow"))
        print(colored(ans_3,"yellow"))
        
        exception=0
        
        if(len(ans_1)==0 or len(ans_2)==0 or len(ans_3)==0 and exception==0): 
            exception=1
            print(colored('VOID ANSWERS','red'))
            print(colored('A: '+str(p1),'red'))
            print(colored('C: '+str(p3),'red'))
            
        if(ca1!=0 and ca3==ca1):
            exception=1
            print(colored("MATCHES FOUND: A or C","red"))
        
        nes=0
        
        if(ca1==0 and ca3==0 and exception==0):
            print(colored("B: Nessuno/a",'red'))
            nes=1
        if(ca1!=0 and ca1>ca3 and exception==0 and nes==0):
            print(colored("A: " + ans_1F,'red'))
            print("Percentage: "+ str(p1)+"%")
        if(ca3!=0 and ca3>ca1 and exception==0 and nes==0):
            print(colored("C: " + ans_3F,'red'))
            print("Percentage: "+ str(p3)+"%")
    
    if(ans_1F.find("Nessuno")>-1 or ans_1F.find("Nessuna")>-1): # Nessuno/a è la risposta 1
        
        todelete=[] # filtraggio ans_2
        
        for i in range(0,len(BOW)):
            for j in range(0,len(ans_2)):
                BOWi=" "+BOW[i]+" "
                ans_2j=" "+ans_2[j]+" "
                if(BOWi.lower().find(ans_2j.lower())>-1):
                    todelete.append(ans_2[j])
                if(len(ans_2[j])==1 and ans_2[j].find("1")>-1): todelete.append(ans_2[j])
                if(len(ans_2[j])==1 and ans_2[j].find("2")>-1): ans_2[j]="due"
                if(len(ans_2[j])==1 and ans_2[j].find("3")>-1): ans_2[j]="tre"
                if(len(ans_2[j])==1 and ans_2[j].find("4")>-1): ans_2[j]="quattro"            
                if(len(ans_2[j])==1 and ans_2[j].find("5")>-1): ans_2[j]="cinque"            
                if(len(ans_2[j])==1 and ans_2[j].find("6")>-1): ans_2[j]="sei"            
                if(len(ans_2[j])==1 and ans_2[j].find("7")>-1): ans_2[j]="sette"
                if(len(ans_2[j])==1 and ans_2[j].find("8")>-1): ans_2[j]="otto"            
                if(len(ans_2[j])==1 and ans_2[j].find("9")>-1): ans_2[j]="nove"           
                if(len(ans_2[j])==2 and ans_2[j].find("10")>-1): ans_2[j]="dieci"  
            
        for k in range(0,len(todelete)):
            ans_2.remove(todelete[k])
            
        ans_2temp=' '.join(ans_2).split()
    
        for i in range(0,len(acc)):
            for j in range(0,len(ans_2temp)):
                temp=list(ans_2temp[j])
                temp[-1]=acc[i]
                temp=str(''.join(temp))
                ans_2.append(temp)
                
        
        ca2 = (googling.count(" "+ans_2F+" ") + googling.count(" "+ans_2F.lower()+" ") + 
               googling.count(" "+ans_2F+".") + googling.count(" "+ans_2F.lower()+".") +
               googling.count(" "+ans_2F+",") + googling.count(" "+ans_2F.lower()+",") +
               googling.count(" "+ans_2F+":") + googling.count(" "+ans_2F.lower()+":") +
               googling.count(" "+ans_2F+";") + googling.count(" "+ans_2F.lower()+";") +
               googling.count(" "+ans_2F+")") + googling.count(" "+ans_2F.lower()+")") +
               googling.count("("+ans_2F+" ") + googling.count("("+ans_2F.lower()+" ") +
               googling.count('"'+ans_2F+' ') + googling.count('"'+ans_2F.lower()+' ') +
               googling.count(' '+ans_2F+'"') + googling.count(' '+ans_2F.lower()+'"')) 
        
        for i in range(0,len(ans_2)):
            ca2 = (googling.count(" "+ans_2[i]+" ") + googling.count(" "+ans_2[i].lower()+" ") + 
                   googling.count(" "+ans_2[i]+".") + googling.count(" "+ans_2[i].lower()+".") + 
                   googling.count(" "+ans_2[i]+",") + googling.count(" "+ans_2[i].lower()+",") +
                   googling.count(" "+ans_2[i]+":") + googling.count(" "+ans_2[i].lower()+":") +
                   googling.count(" "+ans_2[i]+";") + googling.count(" "+ans_2[i].lower()+";") +
                   googling.count(" "+ans_2[i]+")") + googling.count(" "+ans_2[i].lower()+")") +
                   googling.count("("+ans_2[i]+" ") + googling.count("("+ans_2[i].lower()+" ") +
                   googling.count('"'+ans_2[i]+' ') + googling.count('"'+ans_2[i].lower()+' ') +
                   googling.count(' '+ans_2[i]+'"') + googling.count(" "+ans_2[i].lower()+'"') + ca2)
        
        todelete=[] # filtraggio ans_3
        
        for i in range(0,len(BOW)):
            for j in range(0,len(ans_3)):
                BOWi=" "+BOW[i]+" "
                ans_3j=" "+ans_3[j]+" "
                if(BOWi.lower().find(ans_3j.lower())>-1):
                    todelete.append(ans_3[j])
                if(len(ans_3[j])==1 and ans_3[j].find("1")>-1): todelete.append(ans_3[j])
                if(len(ans_3[j])==1 and ans_3[j].find("2")>-1): ans_3[j]="due"
                if(len(ans_3[j])==1 and ans_3[j].find("3")>-1): ans_3[j]="tre"
                if(len(ans_3[j])==1 and ans_3[j].find("4")>-1): ans_3[j]="quattro"            
                if(len(ans_3[j])==1 and ans_3[j].find("5")>-1): ans_3[j]="cinque"            
                if(len(ans_3[j])==1 and ans_3[j].find("6")>-1): ans_3[j]="sei"            
                if(len(ans_3[j])==1 and ans_3[j].find("7")>-1): ans_3[j]="sette"
                if(len(ans_3[j])==1 and ans_3[j].find("8")>-1): ans_3[j]="otto"            
                if(len(ans_3[j])==1 and ans_3[j].find("9")>-1): ans_3[j]="nove"           
                if(len(ans_3[j])==2 and ans_3[j].find("10")>-1): ans_3[j]="dieci"    
        
        for k in range(0,len(todelete)):
            ans_3.remove(todelete[k])
            
        ans_3temp=' '.join(ans_3).split()
    
        for i in range(0,len(acc)):
            for j in range(0,len(ans_3temp)):
                temp=list(ans_3temp[j])
                temp[-1]=acc[i]
                temp=str(''.join(temp))
                ans_3.append(temp)

        
        ca3 = (googling.count(" "+ans_3F+" ") + googling.count(" "+ans_3F.lower()+" ") + 
               googling.count(" "+ans_3F+".") + googling.count(" "+ans_3F.lower()+".") +
               googling.count(" "+ans_3F+",") + googling.count(" "+ans_3F.lower()+",") +
               googling.count(" "+ans_3F+":") + googling.count(" "+ans_3F.lower()+":") +
               googling.count(" "+ans_3F+";") + googling.count(" "+ans_3F.lower()+";") +
               googling.count(" "+ans_3F+")") + googling.count(" "+ans_3F.lower()+")") +
               googling.count("("+ans_3F+" ") + googling.count("("+ans_3F.lower()+" ") +
               googling.count('"'+ans_3F+' ') + googling.count('"'+ans_3F.lower()+' ') +
               googling.count(' '+ans_3F+'"') + googling.count(' '+ans_3F.lower()+'"')) 
        
        for i in range(0,len(ans_3)):
            ca3 = (googling.count(" "+ans_3[i]+" ") + googling.count(" "+ans_3[i].lower()+" ") + 
                   googling.count(" "+ans_3[i]+".") + googling.count(" "+ans_3[i].lower()+".") + 
                   googling.count(" "+ans_3[i]+",") + googling.count(" "+ans_3[i].lower()+",") +
                   googling.count(" "+ans_3[i]+":") + googling.count(" "+ans_3[i].lower()+":") +
                   googling.count(" "+ans_3[i]+";") + googling.count(" "+ans_3[i].lower()+";") +
                   googling.count(" "+ans_3[i]+")") + googling.count(" "+ans_3[i].lower()+")") +
                   googling.count("("+ans_3[i]+" ") + googling.count("("+ans_3[i].lower()+" ") +
                   googling.count('"'+ans_3[i]+' ') + googling.count('"'+ans_3[i].lower()+' ') +
                   googling.count(' '+ans_3[i]+'"') + googling.count(" "+ans_3[i].lower()+'"') + ca3)
        
        p2=(100/(ca2+ca3+0.000001))*ca2
        p3=(100/(ca2+ca3+0.000001))*ca3
        
        print("Words searched:")
        print(colored(ans_2,"yellow"))
        print(colored(ans_3,"yellow"))
        
        exception=0
        
        if(len(ans_1)==0 or len(ans_2)==0 or len(ans_3)==0 and exception==0): 
            exception=1
            print(colored('VOID ANSWERS','red'))
            print(colored('B: '+str(p2),'red'))
            print(colored('C: '+str(p3),'red'))
            
        if(ca2!=0 and ca3==ca2):
            exception=1
            print(colored("MATCHES FOUND: B or C","red")) 
            
        nes=0
        
        if(ca2==0 and ca3==0 and exception==0):
            print(colored("A: Nessuno/a",'red'))
            nes=1
        if(ca2!=0 and ca2>ca3 and exception==0 and nes==0):
            print(colored("B: " + ans_2F,'red'))
            print("Percentage: "+ str(p2)+"%")
        if(ca3!=0 and ca3>ca2 and exception==0 and nes==0):
            print(colored("C: " + ans_3F,'red'))
            print("Percentage: "+ str(p3)+"%")

    os.remove(os.path.join(DIR,'cache','googling.txt'))
    
    


# In[ ]:


# NON -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if(non==1):
    
    print('Typology: NON')
    
    ans_1=open(os.path.join(DIR,'cache','ans_1.txt')).read().replace('\ufeff','').strip().replace("|","I")
    ans_1F=ans_1 #full
    ans_1=ans_1.split() 
    ans_2=open(os.path.join(DIR,'cache','ans_2.txt')).read().replace('\ufeff','').strip().replace("|","I")
    ans_2F=ans_2 #full
    ans_2=ans_2.split()
    ans_3=open(os.path.join(DIR,'cache','ans_3.txt')).read().replace('\ufeff','').strip().replace("|","I")
    ans_3F=ans_3 #full
    ans_3=ans_3.split()
    quest=open(os.path.join(DIR,'cache','quest.txt')).read().replace('\ufeff','').strip().replace("|","I")
    
    print("LINK quest:")
    url = questlink+'&num=30'
    print(colored(url,'blue'))
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    googling = str(response.content)
    
    
    todelete=[] # filtraggio ans_1

    for i in range(0,len(BOW)):
        for j in range(0,len(ans_1)):
            BOWi=" "+BOW[i]+" "
            ans_1j=" "+ans_1[j]+" "
            if(BOWi.lower().find(ans_1j.lower())>-1):
                todelete.append(ans_1[j])
            if(len(ans_1[j])==1 and ans_1[j].find("1")>-1): todelete.append(ans_1[j])
            if(len(ans_1[j])==1 and ans_1[j].find("2")>-1): ans_1[j]="due"
            if(len(ans_1[j])==1 and ans_1[j].find("3")>-1): ans_1[j]="tre"
            if(len(ans_1[j])==1 and ans_1[j].find("4")>-1): ans_1[j]="quattro"            
            if(len(ans_1[j])==1 and ans_1[j].find("5")>-1): ans_1[j]="cinque"            
            if(len(ans_1[j])==1 and ans_1[j].find("6")>-1): ans_1[j]="sei"            
            if(len(ans_1[j])==1 and ans_1[j].find("7")>-1): ans_1[j]="sette"
            if(len(ans_1[j])==1 and ans_1[j].find("8")>-1): ans_1[j]="otto"            
            if(len(ans_1[j])==1 and ans_1[j].find("9")>-1): ans_1[j]="nove"           
            if(len(ans_1[j])==2 and ans_1[j].find("10")>-1): ans_1[j]="dieci"    
    
    for k in range(0,len(todelete)):
        ans_1.remove(todelete[k])
        
    ans_1temp=' '.join(ans_1).split()
    
    for i in range(0,len(acc)):
        for j in range(0,len(ans_1temp)):
            temp=list(ans_1temp[j])
            temp[-1]=acc[i]
            temp=str(''.join(temp))
            ans_1.append(temp)


    ca1 = (googling.count(" "+ans_1F+" ") + googling.count(" "+ans_1F.lower()+" ") + 
           googling.count(" "+ans_1F+".") + googling.count(" "+ans_1F.lower()+".") +
           googling.count(" "+ans_1F+",") + googling.count(" "+ans_1F.lower()+",") +
           googling.count(" "+ans_1F+":") + googling.count(" "+ans_1F.lower()+":") +
           googling.count(" "+ans_1F+";") + googling.count(" "+ans_1F.lower()+";") +
           googling.count(" "+ans_1F+")") + googling.count(" "+ans_1F.lower()+")") +
           googling.count("("+ans_1F+" ") + googling.count("("+ans_1F.lower()+" ") +
           googling.count('"'+ans_1F+' ') + googling.count('"'+ans_1F.lower()+' ') +
           googling.count(' '+ans_1F+'"') + googling.count(' '+ans_1F.lower()+'"')) 

    for i in range(0,len(ans_1)):
        ca1 = (googling.count(" "+ans_1[i]+" ") + googling.count(" "+ans_1[i].lower()+" ") + 
               googling.count(" "+ans_1[i]+".") + googling.count(" "+ans_1[i].lower()+".") + 
               googling.count(" "+ans_1[i]+",") + googling.count(" "+ans_1[i].lower()+",") +
               googling.count(" "+ans_1[i]+":") + googling.count(" "+ans_1[i].lower()+":") +
               googling.count(" "+ans_1[i]+";") + googling.count(" "+ans_1[i].lower()+";") +
               googling.count(" "+ans_1[i]+")") + googling.count(" "+ans_1[i].lower()+")") +
               googling.count("("+ans_1[i]+" ") + googling.count("("+ans_1[i].lower()+" ") +
               googling.count('"'+ans_1[i]+' ') + googling.count('"'+ans_1[i].lower()+' ') +
               googling.count(' '+ans_1[i]+'"') + googling.count(" "+ans_1[i].lower()+'"') + ca1)

    todelete=[] # filtraggio ans_2

    for i in range(0,len(BOW)):
        for j in range(0,len(ans_2)):
            BOWi=" "+BOW[i]+" "
            ans_2j=" "+ans_2[j]+" "
            if(BOWi.lower().find(ans_2j.lower())>-1):
                todelete.append(ans_2[j])
            if(len(ans_2[j])==1 and ans_2[j].find("1")>-1): todelete.append(ans_2[j])
            if(len(ans_2[j])==1 and ans_2[j].find("2")>-1): ans_2[j]="due"
            if(len(ans_2[j])==1 and ans_2[j].find("3")>-1): ans_2[j]="tre"
            if(len(ans_2[j])==1 and ans_2[j].find("4")>-1): ans_2[j]="quattro"            
            if(len(ans_2[j])==1 and ans_2[j].find("5")>-1): ans_2[j]="cinque"            
            if(len(ans_2[j])==1 and ans_2[j].find("6")>-1): ans_2[j]="sei"            
            if(len(ans_2[j])==1 and ans_2[j].find("7")>-1): ans_2[j]="sette"
            if(len(ans_2[j])==1 and ans_2[j].find("8")>-1): ans_2[j]="otto"            
            if(len(ans_2[j])==1 and ans_2[j].find("9")>-1): ans_2[j]="nove"           
            if(len(ans_2[j])==2 and ans_2[j].find("10")>-1): ans_2[j]="dieci"  

    for k in range(0,len(todelete)):
        ans_2.remove(todelete[k])
        
    ans_2temp=' '.join(ans_2).split()
    
    for i in range(0,len(acc)):
        for j in range(0,len(ans_2temp)):
            temp=list(ans_2temp[j])
            temp[-1]=acc[i]
            temp=str(''.join(temp))
            ans_2.append(temp)
            

    ca2 = (googling.count(" "+ans_2F+" ") + googling.count(" "+ans_2F.lower()+" ") + 
           googling.count(" "+ans_2F+".") + googling.count(" "+ans_2F.lower()+".") +
           googling.count(" "+ans_2F+",") + googling.count(" "+ans_2F.lower()+",") +
           googling.count(" "+ans_2F+":") + googling.count(" "+ans_2F.lower()+":") +
           googling.count(" "+ans_2F+";") + googling.count(" "+ans_2F.lower()+";") +
           googling.count(" "+ans_2F+")") + googling.count(" "+ans_2F.lower()+")") +
           googling.count("("+ans_2F+" ") + googling.count("("+ans_2F.lower()+" ") +
           googling.count('"'+ans_2F+' ') + googling.count('"'+ans_2F.lower()+' ') +
           googling.count(' '+ans_2F+'"') + googling.count(' '+ans_2F.lower()+'"')) 

    for i in range(0,len(ans_2)):
        ca2 = (googling.count(" "+ans_2[i]+" ") + googling.count(" "+ans_2[i].lower()+" ") + 
               googling.count(" "+ans_2[i]+".") + googling.count(" "+ans_2[i].lower()+".") + 
               googling.count(" "+ans_2[i]+",") + googling.count(" "+ans_2[i].lower()+",") +
               googling.count(" "+ans_2[i]+":") + googling.count(" "+ans_2[i].lower()+":") +
               googling.count(" "+ans_2[i]+";") + googling.count(" "+ans_2[i].lower()+";") +
               googling.count(" "+ans_2[i]+")") + googling.count(" "+ans_2[i].lower()+")") +
               googling.count("("+ans_2[i]+" ") + googling.count("("+ans_2[i].lower()+" ") +
               googling.count('"'+ans_2[i]+' ') + googling.count('"'+ans_2[i].lower()+' ') +
               googling.count(' '+ans_2[i]+'"') + googling.count(" "+ans_2[i].lower()+'"') + ca2)
        
    todelete=[] # filtraggio ans_3

    for i in range(0,len(BOW)):
        for j in range(0,len(ans_3)):
            BOWi=" "+BOW[i]+" "
            ans_3j=" "+ans_3[j]+" "
            if(BOWi.lower().find(ans_3j.lower())>-1):
                todelete.append(ans_3[j])
            if(len(ans_3[j])==1 and ans_3[j].find("1")>-1): todelete.append(ans_3[j])
            if(len(ans_3[j])==1 and ans_3[j].find("2")>-1): ans_3[j]="due"
            if(len(ans_3[j])==1 and ans_3[j].find("3")>-1): ans_3[j]="tre"
            if(len(ans_3[j])==1 and ans_3[j].find("4")>-1): ans_3[j]="quattro"            
            if(len(ans_3[j])==1 and ans_3[j].find("5")>-1): ans_3[j]="cinque"            
            if(len(ans_3[j])==1 and ans_3[j].find("6")>-1): ans_3[j]="sei"            
            if(len(ans_3[j])==1 and ans_3[j].find("7")>-1): ans_3[j]="sette"
            if(len(ans_3[j])==1 and ans_3[j].find("8")>-1): ans_3[j]="otto"            
            if(len(ans_3[j])==1 and ans_3[j].find("9")>-1): ans_3[j]="nove"           
            if(len(ans_3[j])==2 and ans_3[j].find("10")>-1): ans_3[j]="dieci"   

    for k in range(0,len(todelete)):
        ans_3.remove(todelete[k])
        
    ans_3temp=' '.join(ans_3).split()
    
    for i in range(0,len(acc)):
        for j in range(0,len(ans_3temp)):
            temp=list(ans_3temp[j])
            temp[-1]=acc[i]
            temp=str(''.join(temp))
            ans_3.append(temp)


    ca3 = (googling.count(" "+ans_3F+" ") + googling.count(" "+ans_3F.lower()+" ") + 
           googling.count(" "+ans_3F+".") + googling.count(" "+ans_3F.lower()+".") +
           googling.count(" "+ans_3F+",") + googling.count(" "+ans_3F.lower()+",") +
           googling.count(" "+ans_3F+":") + googling.count(" "+ans_3F.lower()+":") +
           googling.count(" "+ans_3F+";") + googling.count(" "+ans_3F.lower()+";") +
           googling.count(" "+ans_3F+")") + googling.count(" "+ans_3F.lower()+")") +
           googling.count("("+ans_3F+" ") + googling.count("("+ans_3F.lower()+" ") +
           googling.count('"'+ans_3F+' ') + googling.count('"'+ans_3F.lower()+' ') +
           googling.count(' '+ans_3F+'"') + googling.count(' '+ans_3F.lower()+'"')) 

    for i in range(0,len(ans_3)):
        ca3 = (googling.count(" "+ans_3[i]+" ") + googling.count(" "+ans_3[i].lower()+" ") + 
               googling.count(" "+ans_3[i]+".") + googling.count(" "+ans_3[i].lower()+".") + 
               googling.count(" "+ans_3[i]+",") + googling.count(" "+ans_3[i].lower()+",") +
               googling.count(" "+ans_3[i]+":") + googling.count(" "+ans_3[i].lower()+":") +
               googling.count(" "+ans_3[i]+";") + googling.count(" "+ans_3[i].lower()+";") +
               googling.count(" "+ans_3[i]+")") + googling.count(" "+ans_3[i].lower()+")") +
               googling.count("("+ans_3[i]+" ") + googling.count("("+ans_3[i].lower()+" ") +
               googling.count('"'+ans_3[i]+' ') + googling.count('"'+ans_3[i].lower()+' ') +
               googling.count(' '+ans_3[i]+'"') + googling.count(" "+ans_3[i].lower()+'"') + ca3)
    
    p1=(100/(ca1+ca2+ca3+0.000001))*ca1
    p2=(100/(ca1+ca2+ca3+0.000001))*ca2
    p3=(100/(ca1+ca2+ca3+0.000001))*ca3
    
    print("Words searched:")
    print(colored(ans_1,"yellow"))
    print(colored(ans_2,"yellow"))
    print(colored(ans_3,"yellow"))
    
    
    exception=0
    
    if(len(ans_1)==0 or len(ans_2)==0 or len(ans_3)==0 and exception==0): 
        exception=1
        print(colored('VOID ANSWERS','red'))
        print(colored('A: '+str(p1),'red'))
        print(colored('B: '+str(p2),'red'))
        print(colored('C: '+str(p3),'red'))
    if(ca1!=0 and ca2!=0 and ca3!=0 and exception==0): 
        exception=1
        print(colored("NO MATCHES FOUND",'red'))
    if(ca1==0 and ca2==0 and ca3==0 and exception==0): 
        exception=1
        print(colored("NO MATCHES FOUND: all true",'red'))
    if(ca1==0 and ca2==0 and ca3!=0 and exception==0): 
        exception=1
        print(colored("MATCHES FOUND: A or B",'red'))
    if(ca1==0 and ca2!=0 and ca3==0 and exception==0): 
        exception=1
        print(colored("MATCHES FOUND: A or C",'red'))
    if(ca1!=0 and ca2==0 and ca3==0 and exception==0): 
        exception=1
        print(colored("MATCHES FOUND: B or C",'red'))
        
    if(ca1==0 and exception==0):
        print(colored("A: " + ans_1F,'red'))
    if(ca2==0 and exception==0):
        print(colored("B: " + ans_2F,'red'))
    if(ca3==0 and exception==0):
        print(colored("C: " + ans_3F,'red'))

   


# In[ ]:


# prima --------------------------------------------------------------------------------------------------------------------------------------------------------------------

if(prima==1):
    mille = input('Choose the year range >1000 (enter 1) or <1000 (enter 2): ')
    
if(prima==1 and int(mille)==1):    
    
    print('Typology: prima A_1000')
    
    mese = ['gen','feb','mar','apr','mag','giu','lug','ago','set','ott','nov','dic']
    
    ans_1=open(os.path.join(DIR,'cache','ans_1.txt'))
    ans_2=open(os.path.join(DIR,'cache','ans_2.txt'))
    ans_3=open(os.path.join(DIR,'cache','ans_3.txt'))
    
    quest=open(os.path.join(DIR,'cache','quest.txt'))
    quest=quest.read().split()
    
    todelete=[] # filtraggio qpointer

    for i in range(0,len(BOW_hys)):
        for j in range(0,len(quest)):
            if(BOW_hys[i].lower().find(quest[j].lower())>-1):
                todelete.append(quest[j]) 
                    
    for k in range(0,len(todelete)):
        quest.remove(todelete[k])
    
    pointer=quest[-2]
        
    ans_1="https://www.google.com/search?q="+'+'.join(ans_1.read().split())+"+"+pointer+"+anno"
    ans_1=ans_1.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
    print("LINK ans_1:")
    print(colored(ans_1,'blue'))
    
    ans_2="https://www.google.com/search?q="+'+'.join(ans_2.read().split())+"+"+pointer+"+anno"
    ans_2=ans_2.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
    print("LINK ans_2:")
    print(colored(ans_2,'blue'))
    
    ans_3="https://www.google.com/search?q="+'+'.join(ans_3.read().split())+"+"+pointer+"+anno"
    ans_3=ans_3.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
    print("LINK ans_3:")
    print(colored(ans_3,'blue'))

    
    subprocess.Popen(["lynx -dump "+ans_1+" > "+os.path.join(DIR,'cache','goans1.txt')], shell=True)
    subprocess.Popen(["lynx -dump "+ans_2+" > "+os.path.join(DIR,'cache','goans2.txt')], shell=True)
    subprocess.Popen(["lynx -dump "+ans_3+" > "+os.path.join(DIR,'cache','goans3.txt')], shell=True)

    time.sleep(2)
    
    
    goans11=open(os.path.join(DIR,'cache','goans11.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','goans1.txt'),'r+',encoding='utf8',errors="ignore") as goans1:
        lines = goans1.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','goans11.txt'),'w') as goans11:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                goans11.write(lines[i])
    os.remove(os.path.join(DIR,'cache','goans1.txt'))
    os.rename(os.path.join(DIR,'cache','goans11.txt'),os.path.join(DIR,'cache','goans1.txt'))
    
    
    goans22=open(os.path.join(DIR,'cache','goans22.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','goans2.txt'),'r+',encoding='utf8',errors="ignore") as goans2:
        lines = goans2.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','goans22.txt'),'w') as goans22:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                goans22.write(lines[i])
    os.remove(os.path.join(DIR,'cache','goans2.txt'))
    os.rename(os.path.join(DIR,'cache','goans22.txt'),os.path.join(DIR,'cache','goans2.txt'))
    
    
    goans33=open(os.path.join(DIR,'cache','goans33.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','goans3.txt'),'r+',encoding='utf8',errors="ignore") as goans3:
        lines = goans3.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','goans33.txt'),'w') as goans33:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                goans33.write(lines[i])
    os.remove(os.path.join(DIR,'cache','goans3.txt'))
    os.rename(os.path.join(DIR,'cache','goans33.txt'),os.path.join(DIR,'cache','goans3.txt'))
    
    
    goans1=codecs.open(os.path.join(DIR,'cache','goans1.txt'), 'r',encoding='utf8',errors="ignore").read()
    goans2=codecs.open(os.path.join(DIR,'cache','goans2.txt'), 'r',encoding='utf8',errors="ignore").read()
    goans3=codecs.open(os.path.join(DIR,'cache','goans3.txt'), 'r',encoding='utf8',errors="ignore").read()
    
    
    D1 = re.findall(r'\d+', goans1) # DATA ans_1
    date = []
    
    for i in range(0,len(D1)): 
        if(len(D1[i])==4 and (int(str(D1[i])[0])==1 or int(str(D1[i])[0])==2)): 
            if (int(D1[i])<limit_data): 
                date.append(D1[i])
                
    date1 = list(set(date))
    DATA1 = 0
    temp = 0
    
    for i in range(0,len(date1)):
        if(date.count(date1[i])>temp): 
            DATA1=date1[i]
            temp=date.count(date1[i])
    
    D2 = re.findall(r'\d+', goans2) # DATA ans_2
    date = []
    
    for i in range(0,len(D2)): 
        if(len(D2[i])==4 and (int(str(D2[i])[0])==1 or int(str(D2[i])[0])==2)): 
            if (int(D2[i])<limit_data): 
                date.append(D2[i])
                
    date2 = list(set(date))
    DATA2 = 0
    temp = 0
    
    for i in range(0,len(date2)):
        if(date.count(date2[i])>temp): 
            DATA2=date2[i]
            temp=date.count(date2[i])

    D3 = re.findall(r'\d+', goans3) # DATA ans_3
    date = []
    
    for i in range(0,len(D3)): 
        if(len(D3[i])==4 and (int(str(D3[i])[0])==1 or int(str(D3[i])[0])==2)): 
            if (int(D3[i])<limit_data): 
                date.append(D3[i])
                
    date3 = list(set(date))
    DATA3 = 0
    temp = 0
    
    for i in range(0,len(date3)):
        if(date.count(date3[i])>temp): 
            DATA3=date3[i]
            temp=date.count(date3[i])

    print('Check date: ', DATA1, DATA2, DATA3)

    exception=0
    if(DATA1==0 or DATA2==0 or DATA3==0): exception=1
    if(exception==1): print(colored("ZEROS EXCEPTION",'red'))
    
    if(int(DATA1)<int(DATA2) and int(DATA1)<int(DATA3) and exception==0):
        print(colored("A",'red'))
    if(int(DATA2)<int(DATA1) and int(DATA2)<int(DATA3) and exception==0):
        print(colored("B",'red'))
    if(int(DATA3)<int(DATA1) and int(DATA3)<int(DATA2) and exception==0):
        print(colored("C",'red'))

    os.remove(os.path.join(DIR,'cache','goans1.txt'))
    os.remove(os.path.join(DIR,'cache','goans2.txt'))
    os.remove(os.path.join(DIR,'cache','goans3.txt'))
    

if(prima==1 and int(mille)==2): # <1000
    
    print('Typology: prima B_1000')
    
    mese = ['gen','feb','mar','apr','mag','giu','lug','ago','set','ott','nov','dic']
    
    ans_1=open(os.path.join(DIR,'cache','ans_1.txt'))
    ans_2=open(os.path.join(DIR,'cache','ans_2.txt'))
    ans_3=open(os.path.join(DIR,'cache','ans_3.txt'))
    
    quest=open(os.path.join(DIR,'cache','quest.txt'))
    quest=quest.read().split()
    
    todelete=[] # filtraggio qpointer

    for i in range(0,len(BOW_hys)):
        for j in range(0,len(quest)):
            if(BOW_hys[i].lower().find(quest[j].lower())>-1):
                todelete.append(quest[j]) 
                    
    for k in range(0,len(todelete)):
        quest.remove(todelete[k])
    
    pointer=quest[-2]
        
    ans_1="https://www.google.com/search?q="+'+'.join(ans_1.read().split())+"+"+pointer+"+anno"
    ans_1=ans_1.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
    print("LINK ans_1:")
    print(colored(ans_1,'blue'))
    
    ans_2="https://www.google.com/search?q="+'+'.join(ans_2.read().split())+"+"+pointer+"+anno"
    ans_2=ans_2.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
    print("LINK ans_2:")
    print(colored(ans_2,'blue'))
    
    ans_3="https://www.google.com/search?q="+'+'.join(ans_3.read().split())+"+"+pointer+"+anno"
    ans_3=ans_3.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
    print("LINK ans_3:")
    print(colored(ans_3,'blue'))

    
    subprocess.Popen(["lynx -dump "+ans_1+" > "+os.path.join(DIR,'cache','goans1.txt')], shell=True)
    subprocess.Popen(["lynx -dump "+ans_2+" > "+os.path.join(DIR,'cache','goans2.txt')], shell=True)
    subprocess.Popen(["lynx -dump "+ans_3+" > "+os.path.join(DIR,'cache','goans3.txt')], shell=True)

    time.sleep(2)
    
    
    goans11=open(os.path.join(DIR,'cache','goans11.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','goans1.txt'),'r+',encoding='utf8',errors="ignore") as goans1:
        lines = goans1.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','goans11.txt'),'w') as goans11:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                goans11.write(lines[i])
    os.remove(os.path.join(DIR,'cache','goans1.txt'))
    os.rename(os.path.join(DIR,'cache','goans11.txt'),os.path.join(DIR,'cache','goans1.txt'))
    
    
    goans22=open(os.path.join(DIR,'cache','goans22.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','goans2.txt'),'r+',encoding='utf8',errors="ignore") as goans2:
        lines = goans2.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','goans22.txt'),'w') as goans22:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                goans22.write(lines[i])
    os.remove(os.path.join(DIR,'cache','goans2.txt'))
    os.rename(os.path.join(DIR,'cache','goans22.txt'),os.path.join(DIR,'cache','goans2.txt'))
    
    
    goans33=open(os.path.join(DIR,'cache','goans33.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','goans3.txt'),'r+',encoding='utf8',errors="ignore") as goans3:
        lines = goans3.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','goans33.txt'),'w') as goans33:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                goans33.write(lines[i])
    os.remove(os.path.join(DIR,'cache','goans3.txt'))
    os.rename(os.path.join(DIR,'cache','goans33.txt'),os.path.join(DIR,'cache','goans3.txt'))
    
    
    goans1=codecs.open(os.path.join(DIR,'cache','goans1.txt'), 'r',encoding='utf8',errors="ignore").read()
    goans2=codecs.open(os.path.join(DIR,'cache','goans2.txt'), 'r',encoding='utf8',errors="ignore").read()
    goans3=codecs.open(os.path.join(DIR,'cache','goans3.txt'), 'r',encoding='utf8',errors="ignore").read()
    
    
    D1 = re.findall(r'\d+', goans1) # DATA ans_1
    date = []
    
    for i in range(0,len(D1)): 
        if(len(D1[i])==3): 
            date.append(D1[i])
                
    date1 = list(set(date))
    DATA1 = 0
    temp = 0
    
    for i in range(0,len(date1)):
        if(date.count(date1[i])>temp): 
            DATA1=date1[i]
            temp=date.count(date1[i])
    
    D2 = re.findall(r'\d+', goans2) # DATA ans_2
    date = []
    
    for i in range(0,len(D2)): 
        if(len(D2[i])==3): 
            date.append(D2[i])
                
    date2 = list(set(date))
    DATA2 = 0
    temp = 0
    
    for i in range(0,len(date2)):
        if(date.count(date2[i])>temp): 
            DATA2=date2[i]
            temp=date.count(date2[i])

    D3 = re.findall(r'\d+', goans3) # DATA ans_3
    date = []
    
    for i in range(0,len(D3)): 
        if(len(D3[i])==3): 
            date.append(D3[i])
                
    date3 = list(set(date))
    DATA3 = 0
    temp = 0
    
    for i in range(0,len(date3)):
        if(date.count(date3[i])>temp): 
            DATA3=date3[i]
            temp=date.count(date3[i])

    print('Check date: ', DATA1, DATA2, DATA3)    

    exception=0
    if(DATA1==0 or DATA2==0 or DATA3==0): exception=1
    if(exception==1): print(colored("ZEROS EXCEPTION",'red'))
    
    if(int(DATA1)<int(DATA2) and int(DATA1)<int(DATA3) and exception==0):
        print(colored("A",'red'))
    if(int(DATA2)<int(DATA1) and int(DATA2)<int(DATA3) and exception==0):
        print(colored("B",'red'))
    if(int(DATA3)<int(DATA1) and int(DATA3)<int(DATA2) and exception==0):
        print(colored("C",'red'))
    
    os.remove(os.path.join(DIR,'cache','goans1.txt'))
    os.remove(os.path.join(DIR,'cache','goans2.txt'))
    os.remove(os.path.join(DIR,'cache','goans3.txt'))
    


# In[ ]:


# dopo --------------------------------------------------------------------------------------------------------------------------------------------------------------------

if(dopo==1):
    mille = input('Choose the year range >1000 (enter 1) or <1000 (enter 2): ')

if(dopo==1 and int(mille)==1):
    
    print('Typology: dopo A_1000')
    
    mese = ['gen','feb','mar','apr','mag','giu','lug','ago','set','ott','nov','dic']
    
    ans_1=open(os.path.join(DIR,'cache','ans_1.txt'))
    ans_2=open(os.path.join(DIR,'cache','ans_2.txt'))
    ans_3=open(os.path.join(DIR,'cache','ans_3.txt'))
    
    quest=open(os.path.join(DIR,'cache','quest.txt'))
    quest=quest.read().split()
    
    todelete=[] # filtraggio qpointer

    for i in range(0,len(BOW_hys)):
        for j in range(0,len(quest)):
            if(BOW_hys[i].lower().find(quest[j].lower())>-1):
                todelete.append(quest[j]) 
                    
    for k in range(0,len(todelete)):
        quest.remove(todelete[k])
    
    pointer=quest[-2]
        
    ans_1="https://www.google.com/search?q="+'+'.join(ans_1.read().split())+"+"+pointer+"+anno"
    ans_1=ans_1.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
    print("LINK ans_1:")
    print(colored(ans_1,'blue'))
    
    ans_2="https://www.google.com/search?q="+'+'.join(ans_2.read().split())+"+"+pointer+"+anno"
    ans_2=ans_2.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
    print("LINK ans_2:")
    print(colored(ans_2,'blue'))
    
    ans_3="https://www.google.com/search?q="+'+'.join(ans_3.read().split())+"+"+pointer+"+anno"
    ans_3=ans_3.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
    print("LINK ans_3:")
    print(colored(ans_3,'blue'))

    
    subprocess.Popen(["lynx -dump "+ans_1+" > "+os.path.join(DIR,'cache','goans1.txt')], shell=True)
    subprocess.Popen(["lynx -dump "+ans_2+" > "+os.path.join(DIR,'cache','goans2.txt')], shell=True)
    subprocess.Popen(["lynx -dump "+ans_3+" > "+os.path.join(DIR,'cache','goans3.txt')], shell=True)

    time.sleep(2)
    
    
    goans11=open(os.path.join(DIR,'cache','goans11.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','goans1.txt'),'r+',encoding='utf8',errors="ignore") as goans1:
        lines = goans1.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','goans11.txt'),'w') as goans11:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                goans11.write(lines[i])
    os.remove(os.path.join(DIR,'cache','goans1.txt'))
    os.rename(os.path.join(DIR,'cache','goans11.txt'),os.path.join(DIR,'cache','goans1.txt'))
    
    
    goans22=open(os.path.join(DIR,'cache','goans22.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','goans2.txt'),'r+',encoding='utf8',errors="ignore") as goans2:
        lines = goans2.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','goans22.txt'),'w') as goans22:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                goans22.write(lines[i])
    os.remove(os.path.join(DIR,'cache','goans2.txt'))
    os.rename(os.path.join(DIR,'cache','goans22.txt'),os.path.join(DIR,'cache','goans2.txt'))
    
    
    goans33=open(os.path.join(DIR,'cache','goans33.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','goans3.txt'),'r+',encoding='utf8',errors="ignore") as goans3:
        lines = goans3.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','goans33.txt'),'w') as goans33:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                goans33.write(lines[i])
    os.remove(os.path.join(DIR,'cache','goans3.txt'))
    os.rename(os.path.join(DIR,'cache','goans33.txt'),os.path.join(DIR,'cache','goans3.txt'))
    
    
    goans1=codecs.open(os.path.join(DIR,'cache','goans1.txt'), 'r',encoding='utf8',errors="ignore").read()
    goans2=codecs.open(os.path.join(DIR,'cache','goans2.txt'), 'r',encoding='utf8',errors="ignore").read()
    goans3=codecs.open(os.path.join(DIR,'cache','goans3.txt'), 'r',encoding='utf8',errors="ignore").read()
    
    
    D1 = re.findall(r'\d+', goans1) # DATA ans_1
    date = []
    
    for i in range(0,len(D1)): 
        if(len(D1[i])==4 and (int(str(D1[i])[0])==1 or int(str(D1[i])[0])==2)): 
            if (int(D1[i])<limit_data): 
                date.append(D1[i])
                
    date1 = list(set(date))
    DATA1 = 0
    temp = 0
    
    for i in range(0,len(date1)):
        if(date.count(date1[i])>temp): 
            DATA1=date1[i]
            temp=date.count(date1[i])
    
    D2 = re.findall(r'\d+', goans2) # DATA ans_2
    date = []
    
    for i in range(0,len(D2)): 
        if(len(D2[i])==4 and (int(str(D2[i])[0])==1 or int(str(D2[i])[0])==2)): 
            if (int(D2[i])<limit_data): 
                date.append(D2[i])
                
    date2 = list(set(date))
    DATA2 = 0
    temp = 0
    
    for i in range(0,len(date2)):
        if(date.count(date2[i])>temp): 
            DATA2=date2[i]
            temp=date.count(date2[i])

    D3 = re.findall(r'\d+', goans3) # DATA ans_3
    date = []
    
    for i in range(0,len(D3)): 
        if(len(D3[i])==4 and (int(str(D3[i])[0])==1 or int(str(D3[i])[0])==2)): 
            if (int(D3[i])<limit_data): 
                date.append(D3[i])
                
    date3 = list(set(date))
    DATA3 = 0
    temp = 0
    
    for i in range(0,len(date3)):
        if(date.count(date3[i])>temp): 
            DATA3=date3[i]
            temp=date.count(date3[i])
            
    print('Check date: ', DATA1, DATA2, DATA3)

    exception=0
    if(DATA1==0 or DATA2==0 or DATA3==0): exception=1
    if(exception==1): print(colored("ZEROS EXCEPTION",'red'))
    
    if(int(DATA1)>int(DATA2) and int(DATA1)>int(DATA3) and exception==0):
        print(colored("A",'red'))    
    if(int(DATA2)>int(DATA1) and int(DATA2)>int(DATA3) and exception==0):
        print(colored("B",'red'))
    if(int(DATA3)>int(DATA1) and int(DATA3)>int(DATA2) and exception==0):
        print(colored("C",'red'))
    
    os.remove(os.path.join(DIR,'cache','goans1.txt'))
    os.remove(os.path.join(DIR,'cache','goans2.txt'))
    os.remove(os.path.join(DIR,'cache','goans3.txt'))
    

if(dopo==1 and int(mille)==2):
    
    print('Typology: dopo B_1000')
    
    mese = ['gen','feb','mar','apr','mag','giu','lug','ago','set','ott','nov','dic']
    
    ans_1=open(os.path.join(DIR,'cache','ans_1.txt'))
    ans_2=open(os.path.join(DIR,'cache','ans_2.txt'))
    ans_3=open(os.path.join(DIR,'cache','ans_3.txt'))
    
    quest=open(os.path.join(DIR,'cache','quest.txt'))
    quest=quest.read().split()
    
    todelete=[] # filtraggio qpointer

    for i in range(0,len(BOW_hys)):
        for j in range(0,len(quest)):
            if(BOW_hys[i].lower().find(quest[j].lower())>-1):
                todelete.append(quest[j]) 
                    
    for k in range(0,len(todelete)):
        quest.remove(todelete[k])
    
    pointer=quest[-2]
        
    ans_1="https://www.google.com/search?q="+'+'.join(ans_1.read().split())+"+"+pointer+"+anno"
    ans_1=ans_1.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
    print("LINK ans_1:")
    print(colored(ans_1,'blue'))
    
    ans_2="https://www.google.com/search?q="+'+'.join(ans_2.read().split())+"+"+pointer+"+anno"
    ans_2=ans_2.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
    print("LINK ans_2:")
    print(colored(ans_2,'blue'))
    
    ans_3="https://www.google.com/search?q="+'+'.join(ans_3.read().split())+"+"+pointer+"+anno"
    ans_3=ans_3.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
    print("LINK ans_3:")
    print(colored(ans_3,'blue'))

    
    subprocess.Popen(["lynx -dump "+ans_1+" > "+os.path.join(DIR,'cache','goans1.txt')], shell=True)
    subprocess.Popen(["lynx -dump "+ans_2+" > "+os.path.join(DIR,'cache','goans2.txt')], shell=True)
    subprocess.Popen(["lynx -dump "+ans_3+" > "+os.path.join(DIR,'cache','goans3.txt')], shell=True)

    time.sleep(2)
    
    
    goans11=open(os.path.join(DIR,'cache','goans11.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','goans1.txt'),'r+',encoding='utf8',errors="ignore") as goans1:
        lines = goans1.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','goans11.txt'),'w') as goans11:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                goans11.write(lines[i])
    os.remove(os.path.join(DIR,'cache','goans1.txt'))
    os.rename(os.path.join(DIR,'cache','goans11.txt'),os.path.join(DIR,'cache','goans1.txt'))
    
    
    goans22=open(os.path.join(DIR,'cache','goans22.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','goans2.txt'),'r+',encoding='utf8',errors="ignore") as goans2:
        lines = goans2.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','goans22.txt'),'w') as goans22:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                goans22.write(lines[i])
    os.remove(os.path.join(DIR,'cache','goans2.txt'))
    os.rename(os.path.join(DIR,'cache','goans22.txt'),os.path.join(DIR,'cache','goans2.txt'))
    
    
    goans33=open(os.path.join(DIR,'cache','goans33.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','goans3.txt'),'r+',encoding='utf8',errors="ignore") as goans3:
        lines = goans3.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','goans33.txt'),'w') as goans33:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                goans33.write(lines[i])
    os.remove(os.path.join(DIR,'cache','goans3.txt'))
    os.rename(os.path.join(DIR,'cache','goans33.txt'),os.path.join(DIR,'cache','goans3.txt'))
    
    
    goans1=codecs.open(os.path.join(DIR,'cache','goans1.txt'), 'r',encoding='utf8',errors="ignore").read()
    goans2=codecs.open(os.path.join(DIR,'cache','goans2.txt'), 'r',encoding='utf8',errors="ignore").read()
    goans3=codecs.open(os.path.join(DIR,'cache','goans3.txt'), 'r',encoding='utf8',errors="ignore").read()
    
    
    D1 = re.findall(r'\d+', goans1) # DATA ans_1
    date = []
    
    for i in range(0,len(D1)): 
        if(len(D1[i])==3): 
            date.append(D1[i])
                
    date1 = list(set(date))
    DATA1 = 0
    temp = 0
    
    for i in range(0,len(date1)):
        if(date.count(date1[i])>temp): 
            DATA1=date1[i]
            temp=date.count(date1[i])
    
    D2 = re.findall(r'\d+', goans2) # DATA ans_2
    date = []
    
    for i in range(0,len(D2)): 
        if(len(D2[i])==3): 
            date.append(D2[i])
                
    date2 = list(set(date))
    DATA2 = 0
    temp = 0
    
    for i in range(0,len(date2)):
        if(date.count(date2[i])>temp): 
            DATA2=date2[i]
            temp=date.count(date2[i])

    D3 = re.findall(r'\d+', goans3) # DATA ans_3
    date = []
    
    for i in range(0,len(D3)): 
        if(len(D3[i])==3): 
            date.append(D3[i])
                
    date3 = list(set(date))
    DATA3 = 0
    temp = 0
    
    for i in range(0,len(date3)):
        if(date.count(date3[i])>temp): 
            DATA3=date3[i]
            temp=date.count(date3[i])
            
    print('Check date: ', DATA1, DATA2, DATA3)

    exception=0
    if(DATA1==0 or DATA2==0 or DATA3==0): exception=1
    if(exception==1): print(colored("ZEROS EXCEPTION",'red'))
    
    if(int(DATA1)>int(DATA2) and int(DATA1)>int(DATA3) and exception==0):
        print(colored("A",'red'))
    if(int(DATA2)>int(DATA1) and int(DATA2)>int(DATA3) and exception==0):
        print(colored("B",'red'))
    if(int(DATA3)>int(DATA1) and int(DATA3)>int(DATA2) and exception==0):
        print(colored("C",'red'))
    
    os.remove('/Users/liux/Desktop/LQ/goans1.txt')
    os.remove('/Users/liux/Desktop/LQ/goans2.txt')
    os.remove('/Users/liux/Desktop/LQ/goans3.txt')
    


# In[ ]:


# precedente --------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
if(precedente==1 and non==0):
    mille = input('Choose the year range >1000 (enter 1) or <1000 (enter 2): ')

if(precedente==1 and non==0 and int(mille)==1):
    
    print('Typology: precedente / meno recente A_1000')
    
    mese = ['gen','feb','mar','apr','mag','giu','lug','ago','set','ott','nov','dic']
    
    ans_1=open(os.path.join(DIR,'cache','ans_1.txt'))
    ans_2=open(os.path.join(DIR,'cache','ans_2.txt'))
    ans_3=open(os.path.join(DIR,'cache','ans_3.txt'))
    
    if(precedenteILLOLA==1):
        
        ans_1="https://www.google.com/search?q="+'+'.join(ans_1.read().split())+"+"+pointer1+"+anno"
        ans_1=ans_1.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
        print("LINK ans_1:")
        print(colored(ans_1,'blue'))
    
        ans_2="https://www.google.com/search?q="+'+'.join(ans_2.read().split())+"+"+pointer1+"+anno"
        ans_2=ans_2.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
        print("LINK ans_2:")
        print(colored(ans_2,'blue'))
    
        ans_3="https://www.google.com/search?q="+'+'.join(ans_3.read().split())+"+"+pointer1+"+anno"
        ans_3=ans_3.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
        print("LINK ans_3:")
        print(colored(ans_3,'blue'))
    
    else:
        ans_1="https://www.google.com/search?q="+'+'.join(ans_1.read().split())+"+anno"
        ans_1=ans_1.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
        print("LINK ans_1:")
        print(colored(ans_1,'blue'))
    
        ans_2="https://www.google.com/search?q="+'+'.join(ans_2.read().split())+"+anno"
        ans_2=ans_2.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
        print("LINK ans_2:")
        print(colored(ans_2,'blue'))
    
        ans_3="https://www.google.com/search?q="+'+'.join(ans_3.read().split())+"+anno"
        ans_3=ans_3.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
        print("LINK ans_3:")
        print(colored(ans_3,'blue'))

    
    subprocess.Popen(["lynx -dump "+ans_1+" > "+os.path.join(DIR,'cache','goans1.txt')], shell=True)
    subprocess.Popen(["lynx -dump "+ans_2+" > "+os.path.join(DIR,'cache','goans2.txt')], shell=True)
    subprocess.Popen(["lynx -dump "+ans_3+" > "+os.path.join(DIR,'cache','goans3.txt')], shell=True)

    time.sleep(2)
    
    
    goans11=open(os.path.join(DIR,'cache','goans11.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','goans1.txt'),'r+',encoding='utf8',errors="ignore") as goans1:
        lines = goans1.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','goans11.txt'),'w') as goans11:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                goans11.write(lines[i])
    os.remove(os.path.join(DIR,'cache','goans1.txt'))
    os.rename(os.path.join(DIR,'cache','goans11.txt'),os.path.join(DIR,'cache','goans1.txt'))
    
    
    goans22=open(os.path.join(DIR,'cache','goans22.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','goans2.txt'),'r+',encoding='utf8',errors="ignore") as goans2:
        lines = goans2.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','goans22.txt'),'w') as goans22:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                goans22.write(lines[i])
    os.remove(os.path.join(DIR,'cache','goans2.txt'))
    os.rename(os.path.join(DIR,'cache','goans22.txt'),os.path.join(DIR,'cache','goans2.txt'))
    
    
    goans33=open(os.path.join(DIR,'cache','goans33.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','goans3.txt'),'r+',encoding='utf8',errors="ignore") as goans3:
        lines = goans3.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','goans33.txt'),'w') as goans33:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                goans33.write(lines[i])
    os.remove(os.path.join(DIR,'cache','goans3.txt'))
    os.rename(os.path.join(DIR,'cache','goans33.txt'),os.path.join(DIR,'cache','goans3.txt'))
    
    
    goans1=codecs.open(os.path.join(DIR,'cache','goans1.txt'), 'r',encoding='utf8',errors="ignore").read()
    goans2=codecs.open(os.path.join(DIR,'cache','goans2.txt'), 'r',encoding='utf8',errors="ignore").read()
    goans3=codecs.open(os.path.join(DIR,'cache','goans3.txt'), 'r',encoding='utf8',errors="ignore").read()
    
    
    D1 = re.findall(r'\d+', goans1) # DATA ans_1
    date = []
    
    for i in range(0,len(D1)): 
        if(len(D1[i])==4 and (int(str(D1[i])[0])==1 or int(str(D1[i])[0])==2)): 
            if (int(D1[i])<limit_data): 
                date.append(D1[i])
                
    date1 = list(set(date))
    DATA1 = 0
    temp = 0
    
    for i in range(0,len(date1)):
        if(date.count(date1[i])>temp): 
            DATA1=date1[i]
            temp=date.count(date1[i])
    
    D2 = re.findall(r'\d+', goans2) # DATA ans_2
    date = []
    
    for i in range(0,len(D2)): 
        if(len(D2[i])==4 and (int(str(D2[i])[0])==1 or int(str(D2[i])[0])==2)):
            if (int(D2[i])<limit_data): 
                date.append(D2[i])
                
    date2 = list(set(date))
    DATA2 = 0
    temp = 0
    
    for i in range(0,len(date2)):
        if(date.count(date2[i])>temp): 
            DATA2=date2[i]
            temp=date.count(date2[i])

    D3 = re.findall(r'\d+', goans3) # DATA ans_3
    date = []
    
    for i in range(0,len(D3)): 
        if(len(D3[i])==4 and (int(str(D3[i])[0])==1 or int(str(D3[i])[0])==2)):  
            if (int(D3[i])<limit_data): 
                date.append(D3[i])
                
    date3 = list(set(date))
    DATA3 = 0
    temp = 0
    
    for i in range(0,len(date3)):
        if(date.count(date3[i])>temp): 
            DATA3=date3[i]
            temp=date.count(date3[i])
            
    print('Check date: ', DATA1, DATA2, DATA3)
    
    exception=0
    if(DATA1==0 or DATA2==0 or DATA3==0): exception=1
    if(exception==1): print(colored("ZEROS EXCEPTION",'red'))
    
    if(int(DATA1)<int(DATA2) and int(DATA1)<int(DATA3) and exception==0):
        print(colored("A",'red')) 
    if(int(DATA2)<int(DATA1) and int(DATA2)<int(DATA3) and exception==0):
        print(colored("B",'red'))
    if(int(DATA3)<int(DATA1) and int(DATA3)<int(DATA2) and exception==0):
        print(colored("C",'red'))
    
    os.remove(os.path.join(DIR,'cache','goans1.txt'))
    os.remove(os.path.join(DIR,'cache','goans2.txt'))
    os.remove(os.path.join(DIR,'cache','goans3.txt'))
    
    
if(precedente==1 and non==0 and int(mille)==2):
    
    print('Typology: precedente / meno recente B_1000')
    
    mese = ['gen','feb','mar','apr','mag','giu','lug','ago','set','ott','nov','dic']
    
    ans_1=open(os.path.join(DIR,'cache','ans_1.txt'))
    ans_2=open(os.path.join(DIR,'cache','ans_2.txt'))
    ans_3=open(os.path.join(DIR,'cache','ans_3.txt'))
    
    if(precedenteILLOLA==1):
        
        ans_1="https://www.google.com/search?q="+'+'.join(ans_1.read().split())+"+"+pointer1+"+anno"
        ans_1=ans_1.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
        print("LINK ans_1:")
        print(colored(ans_1,'blue'))
    
        ans_2="https://www.google.com/search?q="+'+'.join(ans_2.read().split())+"+"+pointer1+"+anno"
        ans_2=ans_2.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
        print("LINK ans_2:")
        print(colored(ans_2,'blue'))
    
        ans_3="https://www.google.com/search?q="+'+'.join(ans_3.read().split())+"+"+pointer1+"+anno"
        ans_3=ans_3.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
        print("LINK ans_3:")
        print(colored(ans_3,'blue'))
    
    else:
        ans_1="https://www.google.com/search?q="+'+'.join(ans_1.read().split())+"+anno"
        ans_1=ans_1.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
        print("LINK ans_1:")
        print(colored(ans_1,'blue'))
    
        ans_2="https://www.google.com/search?q="+'+'.join(ans_2.read().split())+"+anno"
        ans_2=ans_2.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
        print("LINK ans_2:")
        print(colored(ans_2,'blue'))
    
        ans_3="https://www.google.com/search?q="+'+'.join(ans_3.read().split())+"+anno"
        ans_3=ans_3.replace("'","+").replace("(","%28").replace(")","%29").replace('"',"").replace("|","I")
        print("LINK ans_3:")
        print(colored(ans_3,'blue'))

    
    subprocess.Popen(["lynx -dump "+ans_1+" > "+os.path.join(DIR,'cache','goans1.txt')], shell=True)
    subprocess.Popen(["lynx -dump "+ans_2+" > "+os.path.join(DIR,'cache','goans2.txt')], shell=True)
    subprocess.Popen(["lynx -dump "+ans_3+" > "+os.path.join(DIR,'cache','goans3.txt')], shell=True)

    time.sleep(2)
    
    
    goans11=open(os.path.join(DIR,'cache','goans11.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','goans1.txt'),'r+',encoding='utf8',errors="ignore") as goans1:
        lines = goans1.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','goans11.txt'),'w') as goans11:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                goans11.write(lines[i])
    os.remove(os.path.join(DIR,'cache','goans1.txt'))
    os.rename(os.path.join(DIR,'cache','goans11.txt'),os.path.join(DIR,'cache','goans1.txt'))
    
    
    goans22=open(os.path.join(DIR,'cache','goans22.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','goans2.txt'),'r+',encoding='utf8',errors="ignore") as goans2:
        lines = goans2.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','goans22.txt'),'w') as goans22:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                goans22.write(lines[i])
    os.remove(os.path.join(DIR,'cache','goans2.txt'))
    os.rename(os.path.join(DIR,'cache','goans22.txt'),os.path.join(DIR,'cache','goans2.txt'))
    
    
    goans33=open(os.path.join(DIR,'cache','goans33.txt'),'w',encoding='utf8',errors="ignore")
    with open(os.path.join(DIR,'cache','goans3.txt'),'r+',encoding='utf8',errors="ignore") as goans3:
        lines = goans3.readlines()
        index=len(lines)
        for i in range (0,len(lines)):
            if(lines[i].find("Ricerche")>-1):
                index=i
        with open(os.path.join(DIR,'cache','goans33.txt'),'w') as goans33:
            for i in range (0,index):
                lines[i]=lines[i].split()
                for j in range(0,len(lines[i])):
                    for k in range (0,len(mese)):
                        if(lines[i][j].find(mese[k])>-1 and j==1 and len(lines[i])>2):
                            lines[i][j]=" "
                            lines[i][j-1]=" "
                            lines[i][j+1]=" "
                lines[i]=' '.join(lines[i])
                lines[i]=str(lines[i])
                goans33.write(lines[i])
    os.remove(os.path.join(DIR,'cache','goans3.txt'))
    os.rename(os.path.join(DIR,'cache','goans33.txt'),os.path.join(DIR,'cache','goans3.txt'))
    
    
    goans1=codecs.open(os.path.join(DIR,'cache','goans1.txt'), 'r',encoding='utf8',errors="ignore").read()
    goans2=codecs.open(os.path.join(DIR,'cache','goans2.txt'), 'r',encoding='utf8',errors="ignore").read()
    goans3=codecs.open(os.path.join(DIR,'cache','goans3.txt'), 'r',encoding='utf8',errors="ignore").read()
    
    
    D1 = re.findall(r'\d+', goans1) # DATA ans_1
    date = []
    
    for i in range(0,len(D1)): 
        if(len(D1[i])==3): 
            date.append(D1[i])
                
    date1 = list(set(date))
    DATA1 = 0
    temp = 0
    
    for i in range(0,len(date1)):
        if(date.count(date1[i])>temp): 
            DATA1=date1[i]
            temp=date.count(date1[i])
    
    D2 = re.findall(r'\d+', goans2) # DATA ans_2
    date = []
    
    for i in range(0,len(D2)): 
        if(len(D2[i])==3):
            date.append(D2[i])
                
    date2 = list(set(date))
    DATA2 = 0
    temp = 0
    
    for i in range(0,len(date2)):
        if(date.count(date2[i])>temp): 
            DATA2=date2[i]
            temp=date.count(date2[i])

    D3 = re.findall(r'\d+', goans3) # DATA ans_3
    date = []
    
    for i in range(0,len(D3)): 
        if(len(D3[i])==3):  
            date.append(D3[i])
                
    date3 = list(set(date))
    DATA3 = 0
    temp = 0
    
    for i in range(0,len(date3)):
        if(date.count(date3[i])>temp): 
            DATA3=date3[i]
            temp=date.count(date3[i])
            
    print('Check date: ', DATA1, DATA2, DATA3)
    
    exception=0
    if(DATA1==0 or DATA2==0 or DATA3==0): exception=1
    if(exception==1): print(colored("ZEROS EXCEPTION",'red'))
    
    if(int(DATA1)<int(DATA2) and int(DATA1)<int(DATA3) and exception==0):
        print(colored("A",'red'))
    if(int(DATA2)<int(DATA1) and int(DATA2)<int(DATA3) and exception==0):
        print(colored("B",'red'))
    if(int(DATA3)<int(DATA1) and int(DATA3)<int(DATA2) and exception==0):
        print(colored("C",'red'))

    os.remove(os.path.join(DIR,'cache','goans1.txt'))
    os.remove(os.path.join(DIR,'cache','goans2.txt'))
    os.remove(os.path.join(DIR,'cache','goans3.txt'))
    


# In[ ]:


# standard ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

if(non==0 and stessoanno==0 and entrambe==0 and prima==0 and precedente==0 and nessuno==0 and dopo==0 and quando==0):
    
    print('Typology: standard')
    
    ans_1=open(os.path.join(DIR,'cache','ans_1.txt')).read().replace('\ufeff','').replace("|","I").strip()
    ans_1F=ans_1 #full
    ans_1=ans_1.split() 
    ans_2=open(os.path.join(DIR,'cache','ans_2.txt')).read().replace('\ufeff','').replace("|","I").strip()
    ans_2F=ans_2 #full
    ans_2=ans_2.split()
    ans_3=open(os.path.join(DIR,'cache','ans_3.txt')).read().replace('\ufeff','').replace("|","I").strip()
    ans_3F=ans_3 #full
    ans_3=ans_3.split()
    quest=open(os.path.join(DIR,'cache','quest.txt')).read().replace('\ufeff','').replace("|","I").strip()
    
    print("LINK quest:")
    print(colored(questlink,'blue'))
    
    os.system("lynx -dump "+questlink+" > " + os.path.join(DIR,'cache','googling.txt'))
    googling=codecs.open(os.path.join(DIR,'cache','googling.txt'), 'r',encoding='utf8',errors="ignore").read()
    googling=' '.join(googling.split())
    
    
    todelete=[] # filtraggio ans_1
    
    for i in range(0,len(BOW)):
        for j in range(0,len(ans_1)):
            BOWi=" "+BOW[i]+" "
            ans_1j=" "+ans_1[j]+" "
            if(BOWi.lower().find(ans_1j.lower())>-1):
                todelete.append(ans_1[j])
            if(len(ans_1[j])==1 and ans_1[j].find("1")>-1): todelete.append(ans_1[j])
            if(len(ans_1[j])==1 and ans_1[j].find("2")>-1): ans_1[j]="due"
            if(len(ans_1[j])==1 and ans_1[j].find("3")>-1): ans_1[j]="tre"
            if(len(ans_1[j])==1 and ans_1[j].find("4")>-1): ans_1[j]="quattro"            
            if(len(ans_1[j])==1 and ans_1[j].find("5")>-1): ans_1[j]="cinque"            
            if(len(ans_1[j])==1 and ans_1[j].find("6")>-1): ans_1[j]="sei"            
            if(len(ans_1[j])==1 and ans_1[j].find("7")>-1): ans_1[j]="sette"
            if(len(ans_1[j])==1 and ans_1[j].find("8")>-1): ans_1[j]="otto"            
            if(len(ans_1[j])==1 and ans_1[j].find("9")>-1): ans_1[j]="nove"           
            if(len(ans_1[j])==2 and ans_1[j].find("10")>-1): ans_1[j]="dieci" 

    for k in range(0,len(todelete)):
        ans_1.remove(todelete[k])
        
    ans_1temp=' '.join(ans_1).split()
    
    for i in range(0,len(acc)):
        for j in range(0,len(ans_1temp)):
            temp=list(ans_1temp[j])
            temp[-1]=acc[i]
            temp=str(''.join(temp))
            ans_1.append(temp)


    ca1 = (googling.count(" "+ans_1F+" ") + googling.count(" "+ans_1F.lower()+" ") + 
           googling.count(" "+ans_1F+".") + googling.count(" "+ans_1F.lower()+".") +
           googling.count(" "+ans_1F+",") + googling.count(" "+ans_1F.lower()+",") +
           googling.count(" "+ans_1F+":") + googling.count(" "+ans_1F.lower()+":") +
           googling.count(" "+ans_1F+";") + googling.count(" "+ans_1F.lower()+";") +
           googling.count(" "+ans_1F+")") + googling.count(" "+ans_1F.lower()+")") +
           googling.count("("+ans_1F+" ") + googling.count("("+ans_1F.lower()+" ") +
           googling.count('"'+ans_1F+' ') + googling.count('"'+ans_1F.lower()+' ') +
           googling.count(' '+ans_1F+'"') + googling.count(' '+ans_1F.lower()+'"')) 

    for i in range(0,len(ans_1)):
        ca1 = (googling.count(" "+ans_1[i]+" ") + googling.count(" "+ans_1[i].lower()+" ") + 
               googling.count(" "+ans_1[i]+".") + googling.count(" "+ans_1[i].lower()+".") + 
               googling.count(" "+ans_1[i]+",") + googling.count(" "+ans_1[i].lower()+",") +
               googling.count(" "+ans_1[i]+":") + googling.count(" "+ans_1[i].lower()+":") +
               googling.count(" "+ans_1[i]+";") + googling.count(" "+ans_1[i].lower()+";") +
               googling.count(" "+ans_1[i]+")") + googling.count(" "+ans_1[i].lower()+")") +
               googling.count("("+ans_1[i]+" ") + googling.count("("+ans_1[i].lower()+" ") +
               googling.count('"'+ans_1[i]+' ') + googling.count('"'+ans_1[i].lower()+' ') +
               googling.count(' '+ans_1[i]+'"') + googling.count(" "+ans_1[i].lower()+'"') + ca1)

    todelete=[] # filtraggio ans_2

    for i in range(0,len(BOW)):
        for j in range(0,len(ans_2)):
            BOWi=" "+BOW[i]+" "
            ans_2j=" "+ans_2[j]+" "
            if(BOWi.lower().find(ans_2j.lower())>-1):
                todelete.append(ans_2[j])
            if(len(ans_2[j])==1 and ans_2[j].find("1")>-1): todelete.append(ans_2[j])
            if(len(ans_2[j])==1 and ans_2[j].find("2")>-1): ans_2[j]="due"
            if(len(ans_2[j])==1 and ans_2[j].find("3")>-1): ans_2[j]="tre"
            if(len(ans_2[j])==1 and ans_2[j].find("4")>-1): ans_2[j]="quattro"            
            if(len(ans_2[j])==1 and ans_2[j].find("5")>-1): ans_2[j]="cinque"            
            if(len(ans_2[j])==1 and ans_2[j].find("6")>-1): ans_2[j]="sei"            
            if(len(ans_2[j])==1 and ans_2[j].find("7")>-1): ans_2[j]="sette"
            if(len(ans_2[j])==1 and ans_2[j].find("8")>-1): ans_2[j]="otto"            
            if(len(ans_2[j])==1 and ans_2[j].find("9")>-1): ans_2[j]="nove"           
            if(len(ans_2[j])==2 and ans_2[j].find("10")>-1): ans_2[j]="dieci"  

    for k in range(0,len(todelete)):
        ans_2.remove(todelete[k])
        
    ans_2temp=' '.join(ans_2).split()
    
    for i in range(0,len(acc)):
        for j in range(0,len(ans_2temp)):
            temp=list(ans_2temp[j])
            temp[-1]=acc[i]
            temp=str(''.join(temp))
            ans_2.append(temp)


    ca2 = (googling.count(" "+ans_2F+" ") + googling.count(" "+ans_2F.lower()+" ") + 
           googling.count(" "+ans_2F+".") + googling.count(" "+ans_2F.lower()+".") +
           googling.count(" "+ans_2F+",") + googling.count(" "+ans_2F.lower()+",") +
           googling.count(" "+ans_2F+":") + googling.count(" "+ans_2F.lower()+":") +
           googling.count(" "+ans_2F+";") + googling.count(" "+ans_2F.lower()+";") +
           googling.count(" "+ans_2F+")") + googling.count(" "+ans_2F.lower()+")") +
           googling.count("("+ans_2F+" ") + googling.count("("+ans_2F.lower()+" ") +
           googling.count('"'+ans_2F+' ') + googling.count('"'+ans_2F.lower()+' ') +
           googling.count(' '+ans_2F+'"') + googling.count(' '+ans_2F.lower()+'"')) 

    for i in range(0,len(ans_2)):
        ca2 = (googling.count(" "+ans_2[i]+" ") + googling.count(" "+ans_2[i].lower()+" ") + 
               googling.count(" "+ans_2[i]+".") + googling.count(" "+ans_2[i].lower()+".") + 
               googling.count(" "+ans_2[i]+",") + googling.count(" "+ans_2[i].lower()+",") +
               googling.count(" "+ans_2[i]+":") + googling.count(" "+ans_2[i].lower()+":") +
               googling.count(" "+ans_2[i]+";") + googling.count(" "+ans_2[i].lower()+";") +
               googling.count(" "+ans_2[i]+")") + googling.count(" "+ans_2[i].lower()+")") +
               googling.count("("+ans_2[i]+" ") + googling.count("("+ans_2[i].lower()+" ") +
               googling.count('"'+ans_2[i]+' ') + googling.count('"'+ans_2[i].lower()+' ') +
               googling.count(' '+ans_2[i]+'"') + googling.count(" "+ans_2[i].lower()+'"') + ca2)
    
    todelete=[] # filtraggio ans_3

    for i in range(0,len(BOW)):
        for j in range(0,len(ans_3)):
            BOWi=" "+BOW[i]+" "
            ans_3j=" "+ans_3[j]+" "
            if(BOWi.lower().find(ans_3j.lower())>-1):
                todelete.append(ans_3[j])
            if(len(ans_3[j])==1 and ans_3[j].find("1")>-1): todelete.append(ans_3[j])
            if(len(ans_3[j])==1 and ans_3[j].find("2")>-1): ans_3[j]="due"
            if(len(ans_3[j])==1 and ans_3[j].find("3")>-1): ans_3[j]="tre"
            if(len(ans_3[j])==1 and ans_3[j].find("4")>-1): ans_3[j]="quattro"            
            if(len(ans_3[j])==1 and ans_3[j].find("5")>-1): ans_3[j]="cinque"            
            if(len(ans_3[j])==1 and ans_3[j].find("6")>-1): ans_3[j]="sei"            
            if(len(ans_3[j])==1 and ans_3[j].find("7")>-1): ans_3[j]="sette"
            if(len(ans_3[j])==1 and ans_3[j].find("8")>-1): ans_3[j]="otto"            
            if(len(ans_3[j])==1 and ans_3[j].find("9")>-1): ans_3[j]="nove"           
            if(len(ans_3[j])==2 and ans_3[j].find("10")>-1): ans_3[j]="dieci"   
  
    for k in range(0,len(todelete)):
        ans_3.remove(todelete[k])
        
    ans_3temp=' '.join(ans_3).split()
    
    for i in range(0,len(acc)):
        for j in range(0,len(ans_3temp)):
            temp=list(ans_3temp[j])
            temp[-1]=acc[i]
            temp=str(''.join(temp))
            ans_3.append(temp)
    

    ca3 = (googling.count(" "+ans_3F+" ") + googling.count(" "+ans_3F.lower()+" ") + 
           googling.count(" "+ans_3F+".") + googling.count(" "+ans_3F.lower()+".") +
           googling.count(" "+ans_3F+",") + googling.count(" "+ans_3F.lower()+",") +
           googling.count(" "+ans_3F+":") + googling.count(" "+ans_3F.lower()+":") +
           googling.count(" "+ans_3F+";") + googling.count(" "+ans_3F.lower()+";") +
           googling.count(" "+ans_3F+")") + googling.count(" "+ans_3F.lower()+")") +
           googling.count("("+ans_3F+" ") + googling.count("("+ans_3F.lower()+" ") +
           googling.count('"'+ans_3F+' ') + googling.count('"'+ans_3F.lower()+' ') +
           googling.count(' '+ans_3F+'"') + googling.count(' '+ans_3F.lower()+'"')) 

    for i in range(0,len(ans_3)):
        ca3 = (googling.count(" "+ans_3[i]+" ") + googling.count(" "+ans_3[i].lower()+" ") + 
               googling.count(" "+ans_3[i]+".") + googling.count(" "+ans_3[i].lower()+".") + 
               googling.count(" "+ans_3[i]+",") + googling.count(" "+ans_3[i].lower()+",") +
               googling.count(" "+ans_3[i]+":") + googling.count(" "+ans_3[i].lower()+":") +
               googling.count(" "+ans_3[i]+";") + googling.count(" "+ans_3[i].lower()+";") +
               googling.count(" "+ans_3[i]+")") + googling.count(" "+ans_3[i].lower()+")") +
               googling.count("("+ans_3[i]+" ") + googling.count("("+ans_3[i].lower()+" ") +
               googling.count('"'+ans_3[i]+' ') + googling.count('"'+ans_3[i].lower()+' ') +
               googling.count(' '+ans_3[i]+'"') + googling.count(" "+ans_3[i].lower()+'"') + ca3)
    
    p1=(100/(ca1+ca2+ca3+0.000001))*ca1
    p2=(100/(ca1+ca2+ca3+0.000001))*ca2
    p3=(100/(ca1+ca2+ca3+0.000001))*ca3
    
    print("Words searched:")
    print(colored(ans_1,"yellow"))
    print(colored(ans_2,"yellow"))
    print(colored(ans_3,"yellow"))
    
    exception=0

    if(len(ans_1)==0 or len(ans_2)==0 or len(ans_3)==0 and exception==0): 
        exception=1
        print(colored('VOID ANSWERS','red'))
        print(colored('A: '+str(p1),'red'))
        print(colored('B: '+str(p2),'red'))
        print(colored('C: '+str(p3),'red'))
    if(ca1==0 and ca2==0 and ca3==0 and exception==0): 
        exception=1
        print(colored('NO MATCHES FOUND','red'))
    if(ca1==ca2 and ca2>ca3 and exception==0):
        exception=1
        print(colored('MATCHES FOUND: A or B','red'))
    if(ca2==ca3 and ca2>ca1 and exception==0):
        exception=1
        print(colored('MATCHES FOUND: B or C','red'))
    if(ca1==ca3 and ca1>ca2 and exception==0): 
        exception=1
        print(colored('MATCHES FOUND: A or C','red'))
    if(ca1==ca3 and ca1==ca2 and ca1!=0 and exception==0):
        exception=1
        print(colored('MATCHES FOUND: all true','red'))
        
    if(ca1!=0 and ca1>ca2 and ca1>ca3 and exception==0):
        print(colored("A: " + ans_1F,'red'))
        print("Percentage: "+ str(p1)+"%")
    if(ca2!=0 and ca2>ca1 and ca2>ca3 and exception==0):
        print(colored("B: " + ans_2F,'red'))
        print("Percentage: "+ str(p2)+"%")
    if(ca3!=0 and ca3>ca1 and ca3>ca2 and exception==0):
        print(colored("C: " + ans_3F,'red'))
        print("Percentage: "+ str(p3)+"%")
    
    os.remove(os.path.join(DIR,'cache','googling.txt'))



# In[ ]:


# "clear" ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

os.remove(os.path.join(DIR,'cache','quest.txt'))
os.remove(os.path.join(DIR,'cache','ans_1.txt'))
os.remove(os.path.join(DIR,'cache','ans_2.txt'))
os.remove(os.path.join(DIR,'cache','ans_3.txt'))

print("Cleaning process: Completed")
print ("End : %s" % time.ctime())
print("")


# In[ ]:




