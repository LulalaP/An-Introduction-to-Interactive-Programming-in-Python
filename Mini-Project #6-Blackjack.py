# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        st = ''
        for card in self.hand:
            st = st + str(card) + ' '
        return 'Hand contains ' + st
    
    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        hand_value = 0
        has_A = False
        for card in self.hand:
            if card.rank == 'A':
                has_A = True
            hand_value = hand_value + VALUES.get(card.rank)
        if has_A:
            if hand_value + 10 <= 21:
                hand_value += 10
        return hand_value
   
    def draw(self, canvas, pos):
        i = 0
        for card in self.hand:
            i += 1
            card.draw(canvas, [500, i * 90])
            
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.deck.append(card)
                
    def shuffle(self): 
        random.shuffle(self.deck)

    def deal_card(self):
        deal = self.deck.pop()
        return deal
        
    def __str__(self):
        st = ''
        for card in self.deck:
            st = st + str(card) + ' '
        return 'Deck contains ' + st


#define event handlers for buttons
def deal():
    global outcome, score, in_play, deck, player_hand, dealer_hand
    deck = Deck()
    
    if not in_play:
        deck.shuffle()
        dealer_hand = Hand()
        player_hand = Hand()  
        dealer_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        outcome = 'Hit or stand?'
        in_play = True
    else:
        outcome = 'You lost.  New deal?'
        score -=1
    
    
# if the hand is in play, hit the player
def hit():
    global in_play, outcome, score, deck, player_hand, dealer_hand
    # if busted, assign a message to outcome, update in_play and score   
    if in_play:
        player_hand.add_card(deck.deal_card())
        if player_hand.get_value()>21:
            outcome = 'You have busted.  New deal?'
            score -= 1
            in_play = False
        
        
def stand():
    global in_play, outcome, score, dealer_hand, player_hand 
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
            if dealer_hand.get_value() >21:
                outcome = 'The dealer is busted.  New deal?'
                score += 1
                in_play = False
    # assign a message to outcome, update in_play and score
        if in_play:
            if player_hand.get_value() <= dealer_hand.get_value():
                outcome = 'The dealer wins. New deal?'
                score -= 1
                in_play = False
            else:
                outcome = 'Player wins.  New deal?'
                score += 1
                in_play = False
        
    
# draw handler    
def draw(canvas):
    global outcome, score, player_hand, dealer_hand, in_play
    canvas.draw_text(outcome, [200, 370], 25, 'White')
    canvas.draw_text('Blackjack', [120,100], 80, 'Black')
    canvas.draw_text('score ' + str(score), [400,150], 40, 'White')
    canvas.draw_text('Dealer', [80,200], 30, 'Black')
    canvas.draw_text('Player', [80,370], 30, 'Black')
    count = 0
    for card in dealer_hand.hand:
        card.draw(canvas, [80 + count* 85, 220])
        count +=1
    count = 0
    if in_play:
        card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [80 + CARD_BACK_CENTER[0], 220 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    for card in player_hand.hand:
        card.draw(canvas, [80 + count* 85, 390])
        count+=1
    if not in_play:
        canvas.draw_text(str(dealer_hand.get_value()), [50,200], 20, 'White')
        canvas.draw_text(str(player_hand.get_value()), [50,370], 20, 'White')

        
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
