#!/usr/bin/env python
# coding: utf-8

# In[28]:


import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


# In[2]:


'''
CLASSES

Card
Deck
Player


FUNCTIONS

place_bet(player)
deal_cards(deck)
show_player_hand(hand)
show_dealer_hand (hand)
hit_card(hand, deck)
check_points(hand)
check_win(player_hand, dealer_hand)

'''


# In[3]:


class Card:
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
        
    def __str__(self):
        return (f'{self.rank} of {self.suit}')


# In[81]:


class Deck:
    
    def __init__(self):
        self.all_cards = []
        
        # Create a new deck with all 52 cards
        for rank in ranks:
            for suit in suits:
                self.all_cards.append(Card(rank,suit))
        
    def shuffle(self):  # Shuffle the deck
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        # Remove de first card of the deck (first of the list)
        return self.all_cards.pop(0)
        
    def __len__(self):
        return len(self.all_cards)
    
    def __str__(self):
        return f'There are {len(self.all_cards)} cards left on the deck'


# In[5]:


class Player:
    
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
        
    def win_balance(self, new_value):
        self.balance += new_value
        
    def lose_balance(self, new_value):
        self.balance -= new_value
        
    def __str__(self):
        return f'The player {self.name} has a balance of ${self.balance}'


# In[98]:


def place_bet(player):
    # The user will place its bet through this function
     
    while True:  # Checks for valid input
        try:
            bet = int(input('Place your bet: '))
            break
        except:
            print('Invalid. Please try again \n')
    
    while bet > new_player.balance:  # Checks if player has enough funds for the bet
        print('Not enough funds. Please try again \n')
        bet = int(input('Place your bet: '))
        
    player.lose_balance(bet)
    return bet
                            


# In[7]:


def deal_cards(deck):
    
    hand = [deck.deal_one(), deck.deal_one()]
    
    return hand


# In[8]:


def show_player_hand(hand):
    
    points = 0
    aces = 0
    blackjack = False
        
    print('Your hand is: ')
    for card in hand:
        if card.rank == 'Ace':
            aces += 1
        points += card.value
        print(card)
        
    while aces > 0 and points > 21:
        points -= 10
        aces -= 1
        
    if points == 21:
        blackjack = True
    
    print('')
    print(f'You have {points} points')
    return blackjack
    

    


# In[9]:


def show_dealer_hand(hand):
    
    points = 0
        
    print('Dealer hand is: ')
    for card in hand:
        points += card.value
        
    print(f'{hand[0]} and *****')
    
    # Checks for a Dealer chance of Blackjack
    if hand[0].rank == 'Ten' or hand[0].rank == 'Jack' or hand[0].rank == 'Queen' or hand[0].rank == 'King' or hand[0].rank == 'Ace':
        print('Chance of Blackjack!')


# In[56]:


def show_dealer_hand_final(hand):
    
    points = 0
    aces = 0
            
    print('Dealer hand is: ')
    for card in hand:
        if card.rank == 'Ace':
            aces += 1
        points += card.value
        print(card)
        
    while aces > 0 and points > 21:
        points -= 10
        aces -= 1
        
    print('')
    print(f'Dealer has {points} points')


# In[10]:


def hit_card(hand, deck):
    card = deck.deal_one()
    hand.append(card)
    
    return hand
    


# In[11]:


def check_points(hand):
    
    points = 0
    aces = 0
        
    for card in hand:
        if card.rank == 'Ace':
            aces += 1
        points += card.value
    
    while points > 21 and aces > 0:
        points -= 10
        aces -= 1
        
    return points
        


# In[ ]:


def check_win(player_hand, dealer_hand):
    # Returns TRUE if the player won the game. Otherwise, the dealer won and the function returns FALSE
    
    player_win = False
    
    player_points = check_points(player_hand)
    dealer_points = check_points(dealer_hand)
    
    if dealer_points == player_points:
        return player_win
    
    elif player_points > 21:
        print('BUSTED! You lose.')
        return player_win
    
    elif dealer_points > 21:
        # Dealer busted
        player_win = True
        return player_win
    
    elif dealer_points > player_points:
        print('Dealer wins')
        return player_win
    
    elif dealer_points < player_points:
        print('You win')
        player_win = True
        return player_win 
    
        


# In[159]:


def dealer_play(player_hand, dealer_hand, deck):
    # Define the actions (HIT or STAND) of the Dealer
    
    player_points = check_points(player_hand)
    dealer_points = check_points(dealer_hand)
    
    while dealer_points < player_points and dealer_points < 21:
        dealer_hand.append(deck.deal_one())
        dealer_points = check_points(dealer_hand)
        
    if dealer_points > 21:
        print('Dealer BUSTED! You win!')
        
    return dealer_hand


# In[163]:


print('Welcome to BLACKJACK!!!\n')
print('First, I need to know your name and your balace to play.\n')
player_name = input('Please, enter your name: ')
while True:
    try:
        player_balance = int(input('Please, enter your balance: '))
        break
    except:
        print('Not a valid entry. Try a number.\n')

new_player = Player(player_name,player_balance)

print('')
print(f'Welcome {new_player.name}! You have ${new_player.balance} to play.\n')

start_play = input("Press ENTER when you're ready: ")

keep_playing = True

# This variable will check if the user won at a Double Down
double_down = False

while keep_playing:
    # Take the player bet
    bet = place_bet(new_player)
    print('')

    # Create and shuffle a new deck
    new_deck = Deck()
    new_deck.shuffle()

    # Deal the player and dealer cards
    player_hand = deal_cards(new_deck)
    dealer_hand = deal_cards(new_deck)

    # Show cards
    show_dealer_hand(dealer_hand)
    print('')
    player_blackjack = show_player_hand(player_hand)
    print('')

    # Check for player Blackjack
    if player_blackjack == True:
        player_win = True
        print('BLACKJACK!!!')

    else:
        # Player turn. Hit, stand or Double Down?
        while check_points(player_hand)<=21:
            print('Do you want to hit a new card, stand or go for a double down? Press H, S or D')
            hit_stand = input('')
            print('')

            if hit_stand.lower() == 's':
                print(f'You have {check_points(player_hand)} points')
                print('')
                
                double_down = False

                # Dealer turn
                dealer_play(player_hand, dealer_hand, new_deck)
                show_dealer_hand_final(dealer_hand)

                # Check for winner
                player_win = check_win(player_hand, dealer_hand)
                break

            elif hit_stand.lower() == 'h':
                hit_card(player_hand, new_deck)
                show_player_hand(player_hand)
                
                double_down = False
                
                print('')
                
                while check_points(player_hand)<=21:
                    print('Do you want to hit a new card or stand? Press H or S')
                    hit_stand = input('')
                    print('')
                    
                    if hit_stand.lower() == 's':
                        print(f'You have {check_points(player_hand)} points')
                        print('')

                        # Dealer turn
                        dealer_play(player_hand, dealer_hand, new_deck)
                        show_dealer_hand_final(dealer_hand)

                        # Check for winner
                        player_win = check_win(player_hand, dealer_hand)
                        break

                    elif hit_stand.lower() == 'h':
                        hit_card(player_hand, new_deck)
                        show_player_hand(player_hand)
                        print('')
                        
                else:
                    print('BUSTED! You lose!\n')
                    player_win = False
                    
                break
                
            elif hit_stand.lower() == 'd':
                double_down = True
                hit_card(player_hand, new_deck)
                show_player_hand(player_hand)
                print('')
                new_player.lose_balance(bet)
                
                # Check if the player busted 21
                if check_points(player_hand) > 21:
                    player_win = False
                    print('BUSTED! You lose!\n')
                    break
                else:
                    # Dealer turn
                    dealer_play(player_hand, dealer_hand, new_deck)
                    show_dealer_hand_final(dealer_hand)

                    # Check for winner
                    player_win = check_win(player_hand, dealer_hand)
                    break


        else:
            print('BUSTED! You lose!\n')
            player_win = False

    if check_points(player_hand) == check_points(dealer_hand):
        if double_down == True:
            new_player.win_balance(2*bet)
        else:
            new_player.win_balance(bet)
            
        print('')
        print("It's a tie")
        print(f'Your new balance is ${new_player.balance}')
        
    else:
        if player_win == False:
            print('')
            print(f'Your new balance is ${new_player.balance}')

        elif player_win == True:

            # Blackjack wins returns 50% extra
            if player_blackjack == True:
                new_player.win_balance(int(bet*2.5))
                print('')
                print('You won a Blackjack! You get 50% extra over your bet')
                print(f'Your new balance is ${new_player.balance}')

            # Double Down wins returns 4 times the original bet
            elif double_down == True:
                new_player.win_balance(bet*4)
                print('')
                print('You won a Double Down!')
                print(f'Your new balance is ${new_player.balance}')

            # Regular win returns 2 times the original bet
            else:
                new_player.win_balance(bet*2)
                print('')
                print(f'Your new balance is ${new_player.balance}')

    # Check for replay
    if new_player.balance == 0:
        print('')
        print(f'Sorry {player_name}, you have lost all your money')
        keep_playing = False
        break
    
    while True:
        print('')
        play_again = input('Do you want to play again? Y or N')
        print('')
        print('')
        if play_again.lower() == 'y':
            print('\n')
            break
            
        elif play_again.lower() == 'n':
            keep_playing = False
            if new_player.balance > player_balance:
                print(f'Congrats {player_name}! Your final balance is {new_player.balance}. You won ${new_player.balance - player_balance}.')
            elif new_player.balance < player_balance:
                print(f'Sorry {player_name}, your final balance is {new_player.balance}. You lost ${player_balance - new_player.balance}.')
            else:
                print(f"Hey {player_name}, your final balance is {new_player.balance}. You didn't lose nor win anything!")
            break
    


    


# In[ ]:




