# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 06:13:35 2019

@author: Kevin Izuchukwu
"""

from .Deck import Deck
from .Card import Card
from .Player import Player

suits = "Club Diamond Heart Spade".split()
ranks = "Ace Two Three Four Five Six Seven Eight Nine Ten Jack Queen King".split()


class Game:
    def __init__(self):
        self.players: list = []
        self.current: int = 0
        self.deck: Deck = Deck(suits, ranks)
        while True:
            try:
                x: int = int(input("How many players are playing? >> "))
                if x < 2:
                    print("At least 2 players are required!")
                    continue
                else:
                    for num in range(1, x + 1):
                        name: str = input("Input player " + str(num) + "'s name >> ")
                        self.players.append(Player(self.deck, name))
                    break
            except ValueError:
                print("Invalid input. Try again")
                continue

    def play(self):
        while True:
            current_player: Player = self.players[self.current]
            print('\nCurrent play is', self.deck.current['rank'], 'of', self.deck.current['suit'])
            print('\n' + current_player.name + '\'s turn')
            while True:
                special: Card = current_player.play(self.deck)
                if special:
                    if special.suit == 'Joker':
                        while True:
                            suit = input(
                                '\nInput suit to change to!! c for Clubs, d for Diamond, h for Hearts '
                                'or s for Spades >> ').lower()[0]
                            if suit in 'c d h s'.split():
                                self.changeSuit(suit)
                                break
                            else:
                                print('Retry! Invalid input')
                                continue
                        break
                    else:
                        self.checkIfToPick(special)
                        if self.isDoublePlayers():
                            continue
                        else:
                            break
                else:
                    break
            if current_player.howMany() == 0:
                print(current_player.name, 'wins!!!')
                break
            else:
                if current_player.howMany() == 1:
                    print('\n' + current_player.name, 'on Last Card!')
                self.setNextTurn()

    def getNextTurn(self):
        if self.current >= len(self.players) - 1:
            return 0
        else:
            return self.current + 1

    def setNextTurn(self):
        self.current = self.getNextTurn()

    def addToNext(self, times: int):
        next_player: Player = self.players[self.getNextTurn()]
        print(next_player.name, 'picks', str(times))
        for _ in range(times):
            next_player.market(self.deck)

    def checkIfToPick(self, special: Card):
        if special.rank == 'Two':
            self.addToNext(2)
        elif special.rank == 'Five':
            self.addToNext(3)

    def isDoublePlayers(self):
        if len(self.players) == 2:
            print('\nWaiting for continue!')
            return True
        elif len(self.players) > 2:
            self.setNextTurn()
            return False

    def changeSuit(self, suit: str):
        if suit == 'c':
            self.deck.makeTop('Club', 'Joker')
        elif suit == 'd':
            self.deck.makeTop('Diamond', 'Joker')
        elif suit == 'h':
            self.deck.makeTop('Heart', 'Joker')
        elif suit == 's':
            self.deck.makeTop('Spade', 'Joker')
        return
