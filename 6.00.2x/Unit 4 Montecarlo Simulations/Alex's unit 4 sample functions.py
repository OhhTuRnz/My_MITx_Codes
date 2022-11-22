# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 22:40:10 2022

@author: turnz
"""
import random
import numpy as np

def throwNeedles(numNeedles):
    needlesIn = 0
    for i in range(1, numNeedles + 1, 1):
        x = random.random()
        y = random.random()
        if ((x*x + y*y)**0.5) <= 1.0:
            needlesIn+=1
    return 4*(needlesIn/float(numNeedles))

def getEstimates(numNeedles, numTrials):
    estimates = []
    for i in range(numTrials):
        piGuess = throwNeedles(numNeedles)
        estimates.append(piGuess)
    sDev = np.std(estimates)
    curEst = sum(estimates)/numTrials
    print('Est. = ' + str(curEst) +\
          ', Std. dev. = ' + str(round(sDev, 6))\
        + ', Needles = ' + str(numNeedles))
    return (curEst, sDev)

def estPi(precision, numTrials):
    numNeedles = 1000
    sDev = precision
    while sDev >= precision/2:
        curEst, sDev = getEstimates(numNeedles, numTrials)
        numNeedles *= 2
    return curEst