# Blackjack game
# Created by Jay
# 5/1/2019

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Hand:
    def __init__(self, name="Dealer"):
        self.cards = []
        self.values = 0
        self.aces = 0
        self.name = name
    
    def add_card(self, card):
        self.cards.append(card)
        self.values += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.values > 21 and self.aces > 0:
            self.values -= 10
            self.aces -= 1