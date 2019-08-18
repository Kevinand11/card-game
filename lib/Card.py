# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 05:57:20 2019

@author: Kevin Izuchukwu
"""


class Card:
    def __init__(self, suit: str, rank: str):
        self.suit: str = suit
        self.rank: str = rank
        
    def __repr__(self):
        if self.suit == "Joker":
            return self.suit
        return self.rank + " of " + self.suit
