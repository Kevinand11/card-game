# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 06:00:19 2019

@author: Kevin Izuchukwu
"""

from .Deck import Deck
from .Card import Card


def inputValidator(limit: int):
    msg = "Input number attached to card you want to play. Input 0 to go to market"
    while True:
        try:
            x: int = int(input(msg + " >> "))
            if x in range(limit + 1):
                return x
            else:
                print("Number not in range. Try again")
                continue
        except ValueError:
            print("Invalid input. Try again")
            continue


def checkIfSpecial(card: Card):
    if card.rank in "Ace Two Five Eight Twenty".split():
        return card
    return None


class Player:
    def __init__(self, deck: Deck, name: str):
        self.name: str = name
        self.cards: list = []
        for _ in range(4):
            self.market(deck)

    def hand(self):
        for i in range(len(self.cards)):
            print(i + 1, "-", self.cards[i])
        return self.howMany()

    def howMany(self):
        return len(self.cards)

    def play(self, deck: Deck):
        while True:
            length: int = self.hand()
            result: int = inputValidator(length)
            if result == 0:
                self.market(deck)
                return None
            else:
                position: int = result - 1
                if deck.isValidPlay(self.cards[position]):
                    card: Card = self.cards.pop(position)
                    if deck.play(card):
                        return checkIfSpecial(card)
                    else:
                        print("Suits doesn't match with current play card")
                        continue
                else:
                    print("Suits doesn't match with current play card")
                    continue

    def market(self, deck: Deck):
        self.cards.append(deck.market())

