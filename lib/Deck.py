# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 05:58:19 2019

@author: Kevin Izuchukwu
"""

import random
from .Card import Card


class Deck:
    def __init__(self, suits: list, ranks: list):
        self.deck: list = []
        self.played: list = []
        self.current: dict = {'rank': str, 'suit': str}
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
            self.deck.append(Card("Joker", "Twenty"))
        self.shuffle()
        self.startPlayedList()

    def shuffle(self):
        random.shuffle(self.deck)

    def startPlayedList(self):
        while True:
            card: Card = self.deck.pop()
            self.played.append(card)
            self.makeTop(card.suit, card.rank)
            if card.rank in 'Ace Two Five Eight Twenty':
                continue
            else:
                break

    def market(self):
        card: Card = self.deck.pop()
        if len(self.deck) == 0:
            self.reCollect()
        return card

    def play(self, card: Card):
        if self.isValidPlay(card):
            self.played.append(card)
            self.makeTop(card.suit, card.rank)
            return True
        else:
            print('Invalid card')
            return False

    def reCollect(self):
        for piece in self.played:
            self.deck.append(piece)
        self.shuffle()

    def makeTop(self, suit: str, rank: str):
        self.current['suit'] = suit
        self.current['rank'] = rank

    def isValidPlay(self, card: Card):
        return (
                card.suit == 'Joker' or
                card.suit == self.current['suit'] or
                card.rank == self.current['rank']
        )
