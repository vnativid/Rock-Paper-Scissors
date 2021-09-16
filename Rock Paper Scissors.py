#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 12:54:35 2021

@author: vincenatividad
"""

#rock paper scissors
import random

def play():
    user = input("Choose Rock Paper Scissors: 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer: #same choice = draw
        return 'It is a Draw.'
            
    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lose.'
    
def is_win(player, opponent):
    #return true if player wins
    #r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
        or (player == 'p' and opponent == 'r'):
        return True
    
print(play())