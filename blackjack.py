# Blackjack game
# Created by Jay
# 5/1/2019
import card
import deck
import hand
import chips

def take_bet(chips):
    '''
    Ask player for taking bet at the beginning of the game
    '''
    while True:
        try:
            chips.bet = int(input("Enter your bet: "))
        except:
            print("Sorry, please input the number")
        else:
            if chips.bet > chips.total:
                print("You can't bet more than your available chips")
                continue
            else:
                print("You have bet {}".format(chips.bet))
                break


def hit(deck, hand):
    '''
    Hit the card
    '''
    hit_card = deck.deal()
    print("\n'{}' was hit by {}".format(hit_card, hand.name))
    hand.add_card(hit_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    '''
    Ask player to hit or stand
    '''
    global playing
    while hand.values <= 21:
        try:
            request = input("\nHit or Stand? ('H'/'S'): ")
        except:
            print("Sorry, please enter only 'H' or 'S'")
        else:
            if not request == 'H' and not request == 'S':
                print("Sorry, please enter only 'H' or 'S'")
            else:
                if request == 'H':
                    hit(deck, hand)
                    print("Total value: {}".format(hand.values))
                else:
                    playing = False
                    break


def show_some(player,dealer):
    '''
    Show all the cards for player but some for dealer
    '''
    print('\n=======================================================================')
    print("{}'s Hand:".format(dealer.name))
    print("<card hidden>, {}".format(dealer.cards[1])) 
    print("\n{}'s Hand:".format(player.name))
    print(*player.cards, sep=', ')
    print("Total value: {}".format(player.values))
    print('=======================================================================')
    

def show_all(player,dealer):
    '''
    Show all the cards for both sides
    '''
    print('\n=======================================================================')
    print("{}'s Hand:".format(dealer.name))
    print(*dealer.cards, sep=', ')
    print("Total value: {}".format(dealer.values))
    print("\n{}'s Hand:".format(player.name))
    print(*player.cards, sep=', ')
    print("Total value: {}".format(player.values))
    print('=======================================================================')


def re_game():
    '''
    Ask player to play again
    '''
    global playing
    global new_chips
    while True:
        try:
            re = input("Do you want to play it again (Y/N): ")
        except:
            print("Sorry, please enter only 'Y' or 'N'")
        else:
            if not re == 'Y' and not re == 'N':
                print("Sorry, please enter only 'Y' or 'N'")
            else:
                if re == 'Y':
                    print("\nLet's start new round")
                    playing = True
                    new_chips = False
                    return True
                else:
                    print("Thanks for playing!\n")
                    return False


def blackjack():
    '''
    Main
    '''

    still_play = True
    count_win = 0

    # display an opening statement
    print('\n***********************************************************************')
    print('\t\t\t      BlackJack')
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    print('***********************************************************************\n')

    # ask user for name
    while True:
        try:
            name = input("Please enter your name: ")
        except:
            print("Sorry!, there is something wrong, please try again!")
        else:
            break

    # if player decides to continue playing, the game keeps playing
    while still_play:
        
        # create hands for player and dealer
        player = hand.Hand(name)
        dealer = hand.Hand()

        # chips will be from the previous round  
        if new_chips == True:
            chip = chips.Chips()
            print("Hi! {} let's begin with {} chip(s)".format(name, chip.total))
        else:
            chip = chip
            print("Let's begin with your remainning chip(s) form previos round which is {}".format(chip.total))

        # create and shuffle deck and also distribute the card to player and dealer
        deck_card = deck.Deck()
        deck_card.shuffle()
        player.add_card(deck_card.deal())
        player.add_card(deck_card.deal())
        dealer.add_card(deck_card.deal())
        dealer.add_card(deck_card.deal())

        # ask user for taking bet
        take_bet(chip)

        # display cards
        show_some(player,dealer)

        # keep playing if player would like to keep hitting or the value is less than 21
        while playing:
            
            hit_or_stand(deck_card, player)
            show_some(player, dealer)

            # dealer wins, if player's value is more than 21
            if player.values > 21:
                print("\nYou bust!, winner is Dealer")
                count_win = 0
                chip.lose_bet()
                break

        # dealer decide to hit or stand
        if player.values <= 21:
            
            # dealer will hit until she reaches 17
            while dealer.values < 17:
                hit(deck_card, dealer)    

            # show all cards
            show_all(player, dealer)

            # player wins, if dealer's value is more than 21
            if dealer.values > 21:
                print("\nDealer busts!, winner is {}".format(name))
                count_win += 1
                chip.win_bet()
            else:
                # tie
                if player.values == dealer.values:
                    print("\nDealer and you tie! It's a push.")
                # player wins
                elif player.values > dealer.values:
                    print("\n{} wins!".format(name))
                    count_win += 1
                    chip.win_bet()
                # dealer wins
                else:
                    print("\nDealer wins!")
                    count_win = 0
                    chip.lose_bet()

        # inform Player of their chips total and winning steak
        print("\n{}'s winnings stand at {}".format(name, chip.total))
        if chip.total == 0:
            print("You are out of chips, thank you for playing\n")
            break
        else:     
            if not count_win == 0:
                print("{}'s Winning Steak is {}\n".format(name, count_win))
            else:
                print("\n")

            # ask player to re game
            still_play = re_game()



playing = True
new_chips = True                           

blackjack()