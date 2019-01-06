# Blackjack game
# Created by Jay
# 5/1/2019
import random

import card

suits = ('\u2663', '\u2666', '\u2665', '\u2660')    # club, diamond, heart, spade
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(card.Card(suit,rank))

    def __str__(self):
        all_card_name = ""
        i = 0
        for card in self.deck:
            if not i == len(self.deck)-1:   
                all_card_name += str(card) + ", " 
            else:
                all_card_name += str(card)
        return "The deck has: {}".format(all_card_name)

    def shuffle(self):
        random.shuffle(self.deck)
        print('Deck has been shuffled\n')

    def deal(self):
        return self.deck.pop()