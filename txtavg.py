# -*- coding: utf-8 -*-
"""
Created on Wed May  5 16:15:09 2021

@author: HYDRO
"""

from collections import Counter
import glob
import os

os.chdir(r'C:\Users\HYDRO\Desktop\2021 HUD\CODE FOR UTAU\Phonetic Lyrics\finished')
myFiles = glob.glob('*.txt')

def txtavg():
    count = 0
    length = len(myFiles)
    merger = ""
    while length != 0:
        txt = open(myFiles[count])
        content = txt.read()
        merger += ' '
        merger += content
        count += 1
        length -= 1
    nonewline = merger.replace('\n', ' ')
    line = nonewline.split(' ')
    print("")
    print("Average across all txt documents")
    print(Counter(line))