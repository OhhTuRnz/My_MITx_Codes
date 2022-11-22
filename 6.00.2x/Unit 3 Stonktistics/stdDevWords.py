# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 20:56:10 2022

@author: turnz
"""
def stdDevOfLengths(L):
    sum = 0
    sqSum = 0
    length = len(L)
    for item in L:
        if len(item) <= 0:
            return("NaN")
        sum += len(item)
        sqSum += len(item)**2
    return ((sqSum/length-(sum/length)**2)**0.5)