# Blackjack game
# Created by Jay
# 5/1/2019
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)