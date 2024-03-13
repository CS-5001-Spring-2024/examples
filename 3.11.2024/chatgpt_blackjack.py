import random

# prompt: 
# generate an object oriented solution to play blackjack using python

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for value in range(2, 11):
                self.cards.append(Card(suit, str(value)))
            for value in ['J', 'Q', 'K', 'A']:
                self.cards.append(Card(suit, value))
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)
        if card.value.isdigit():
            self.value += int(card.value)
        elif card.value in ['J', 'Q', 'K']:
            self.value += 10
        else:
            if self.value + 11 > 21:
                self.value += 1
            else:
                self.value += 11

    def display(self):
        for card in self.cards:
            print(card)
        print("Total value:", self.value)

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def start_game(self):
        print("Welcome to Blackjack!")
        self.player_hand.add_card(self.deck.deal_card())
        self.player_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        self.player_hand.display()
        self.dealer_hand.display()

        while self.player_hand.value < 21:
            choice = input("Do you want to hit or stand? (h/s): ").lower()
            if choice == 'h':
                self.player_hand.add_card(self.deck.deal_card())
                self.player_hand.display()
            elif choice == 's':
                break

        if self.player_hand.value > 21:
            print("You bust! Dealer wins.")
        else:
            while self.dealer_hand.value < 17:
                self.dealer_hand.add_card(self.deck.deal_card())
            self.dealer_hand.display()

            if self.dealer_hand.value > 21 or self.player_hand.value > self.dealer_hand.value:
                print("Congratulations! You win!")
            elif self.player_hand.value < self.dealer_hand.value:
                print("Dealer wins.")
            else:
                print("It's a tie!")

game = Blackjack()
game.start_game()
