# -*- coding: utf-8 -*-
"""
Created on Wed May  5 16:15:09 2021

@author: HYDRO
"""

from collections import Counter
import glob
from pathlib import Path

if Path('finished/').exists():
    myFiles = glob.glob('finished/*.txt')
    
def txtavg():
    count = 0
    length = len(myFiles)
    merger = ""
    while length != 0:
        txt = open(myFiles[count])
        content = txt.read()
        merger += '\n'
        merger += content
        count += 1
        length -= 1
    nonewline = merger.replace('\n', ' ')
    line = nonewline.split(' ')
    print("\n")
    print("Average across all txt documents")
    print(Counter(line))
