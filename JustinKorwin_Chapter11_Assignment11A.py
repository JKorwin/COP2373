# this program will use the Deck object as shown in 11.5 and present a 5 card hand of poker. The user will then enter a
# series of numbers and those cards will then be replaced

# importing random
import random

# defining Deck class as shown in 11.5

class Deck():
    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        random.shuffle(self.card_list)
        self.current_card = 0
        self.size = size

    def deal(self):
        if self.size - self.current_card < 1:
            random.shuffle(self.card_list)
            self.current_card = 0
            print('Reshuffling...')
        self.current_card += 1
        return self.card_list[self.current_card - 1]

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['clubs', 'diamonds', 'hearts', 'spades']

# creating a function that takes a deck and deals a hand of 5 card poker
def poker_hand(deck):
    cards = [deck.deal() for i in range(5)]
    return cards

# creating a function to display the cards
def display_cards(cards):
    for i , card in enumerate(cards):
        r = card % 13
        s = card // 13
        print(ranks[r], 'of', suits[s])

#creating a function to replace the cards
def replace(cards, deck, cards_to_replace):
    for i in cards_to_replace:
        cards[i] = deck.deal()

def main():
    # creating a shuffled deck
    deck = Deck(52)
    # dealing cards and displaying them
    cards = poker_hand(deck)
    print("Starting hand:")
    display_cards(cards)

    # asking for user to replace some of the cards
    replacement_cards = input("Please enter the numbers of the cards you want to replace (for example: 1, 3, 5):")

    # splitting the numbers from user
    cards_to_replace = [int(i) - 1 for i in replacement_cards.split(',')]

    # replacing cards
    replace(cards, deck, cards_to_replace)

    # displaying new hand
    print("New hand:")
    display_cards(cards)

# calling main function
main()
