suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

import random
suits
ranks
values

playing = True


class Card:
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

  def __str__(self):
    return f'{self.rank} of {self.suit}'


class Deck:  
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.deck.append(card)

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
          deck_comp += '\n' +card.__str__()
        return f"The deck has: {deck_comp}"

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
      single_card = self.deck.pop()
      return single_card

# test_deck = Deck()
# print(test_deck)


class Hand:
  def __init__(self):
    self.cards = []
    self.value = 0
    self.aces = 0

  def add_card(self,card): 
    self.cards.append(card)
    self.value += values[card.rank]

    if card.rank == 'Ace':
      self.aces += 1

# if total value is greater than 21 and still have an ace
# change ace to 1 instead of 11
  def adjust_for_ace(self):
    while self.value > 21 and self.aces:
      self.value -=1
      self.aces -= 1

class Chip:
  def __init__(self):
    self.total = 100
    self.bet = 0 

  def win_bet(self):
    self.total += self.bet

  def lose_bet(self):
    self.total -= self.bet

test_deck = Deck()
test_deck.shuffle()
test_player = Hand()
test_player.add_card(test_deck.deal())
print(test_player.value)