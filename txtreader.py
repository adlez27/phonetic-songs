# -*- coding: utf-8 -*-
"""
Created on Wed May  5 16:15:07 2021

@author: HYDRO
"""

from collections import Counter
import glob
from pathlib import Path

if Path('finished/').exists():
    myFiles = glob.glob('finished/*.txt')

def txtreader():
    count = 0
    length = len(myFiles)
    while length != 0:
        txt = open(myFiles[count])  
        print(myFiles[count])
        content = txt.read()
        nonewline = content.replace('\n', ' ')
        line = nonewline.split(' ')
        result = Counter(line)
        count += 1
        length -= 1
        print(result)
        print("\n")