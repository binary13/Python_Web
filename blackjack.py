from random import randint
from random import shuffle
from random import choice


class Card(object):

    def __init__(self, suit="", value=""):
        self.suit = suit
        self.value = value

    def __str__(self):
        return str(self.value) + " of " + str(self.suit)


class Deck(object):

    cards = []

    def __init__(self):
        suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
        faces = ["Ace", "King", "Queen", "Jack"]

        for suit in suits:
            for num in range(2, 11):
                self.cards.append(Card(suit, str(num)))
            for face in faces:
                self.cards.append(Card(suit, face))

    def give_card(self):
        new_card = choice(self.cards)
        self.cards.remove(new_card)
        return new_card

    def __str__(self):
        ret_str = ""
        suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
        for suit in suits:
            ret_str += suit+": "
            for card in self.cards:
                if card.suit == suit:
                    ret_str += card.value + ", "
            ret_str = ret_str[:-2] + "\n"
        return ret_str

    def __len__(self):
        return len(self.cards)


class Player(object):

    def __init__(self, name='Justin', money=2000, cards = []):
        self.money = money
        self.name = name
        self.cards = cards


    def cards_value(self):
        value = 0
        for card in self.cards:
            try:
                value += int(card.value)
            except:
                if card.value in ['King', 'Queen', 'Jack']:
                    value += 10
        for card in self.cards:
            if card.value == 'Ace':
                if value <= 10:
                    value += 11
                else:
                    value += 1
        return value

    def show_cards(self):
        ret_str = ""
        for card in self.cards:
            ret_str += str(card) + ", "
        ret_str = ret_str[:-2]
        return ret_str


class Dealer(Player):

    def __init__(self, name="Dealer", money=1000000, cards = []):
        self.name = name
        self.money = money
        self.cards = cards

    def show_cards(self):
        ret_str = ""
        for card in self.cards[1:]:
            ret_str += str(card) + ", "
        ret_str = ret_str[:-2]
        return ret_str

    def show_hole_card(self):
        return str(self.cards[0])



deck = Deck()
shuffle(deck.cards)
print(deck)

player = Player()
player.cards.append(deck.give_card())
player.cards.append(deck.give_card())
print("Player has:", player.show_cards())
print("The value of player's hand is", player.cards_value())

dealer = Dealer()
dealer.cards.append(deck.give_card())
dealer.cards.append(deck.give_card())
print("Dealer's public cards:", dealer.show_cards())
print("Dealer's hole card:", dealer.show_hole_card())
print("The value of dealer's hand is", dealer.cards_value())

if player.cards_value() > dealer.cards_value():
    print("Player wins!")
elif dealer.cards_value() > player.cards_value():
    print("Dealer wins.")
else:
    print("It was a tie.")
