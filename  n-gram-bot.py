#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 13:35:17 2020

@author: toma_hal
"""


import pandas as pd
import numpy as np
from collections import *

def train_char_lm(fname, order = 4):
    data = file(fname).read()
    lm = deaefaultdict(Counter)
    pad = '*' * order 
    data += pad
    for i in range(len(data) - order):
        history, char = data[i:i+order], data[i+order]
        lm[history][char] +=1
    
    def normalize(counter):
        s = float(sum(counter.values()))
        return [(c,cnt/s) for c,cnt in counter.items()]

    outlm = {hist:normalize(char) for hist, char in lm.iteritems()}
    return outlm



from random import random

def generate_letter(lm, history, order):
        history = history[-order:]
        dist = lm[history]
        x = random()
        for c,v in dist:
            x = x - v
            if x <= 0: return c

def generate_text(lm, order, nletters=1000):
    history = "~" * order
    out = []
    for i in xrange(nletters):
        c = generate_letter(lm, history, order)
        history = history[-order:] + c
        out.append(c)
    return "".join(out)