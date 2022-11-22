# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 23:18:49 2022

@author: turnz
"""
import random as rn
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    balls = ['r', 'r', 'r', 'r', 'g', 'g', 'g', 'g']
    trialWithSameColor = 0
    for i in range (numTrials):
        rn.shuffle(balls)
        if(balls[0] == balls[1]) & (balls[1] == balls[2]):
            trialWithSameColor += 1
    return float(trialWithSameColor)/float(numTrials)

for i in range(20):
    print(noReplacementSimulation(1000))
            
        