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

    def __init__(self, money=200, cards = []):
        self.money = money
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

    def __init__(self, money=0, cards = []):
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


def bust(player):
    if player.cards_value() > 21:
        return True
    else:
        return False


deck = Deck()
shuffle(deck.cards)

player = Player()
dealer = Dealer()

print("Let's play blackjack!")
print("The object of the game is to get as close \nto 21 as possible, without going over.")
print("Are you ready?")


while True:
    if len(deck.cards) < 10:
        deck = Deck()
    print("\n")
    print("You have ${}.".format(player.money))

    bet = 0

    while True:
        try:
            bet = int(input("How much will you bet? "))
        except:
            print("Invalid input! Try again.")
        if bet <= player.money:
            break
        else:
            print("You don't have that much! Choose a lower bet.")

    player.cards.append(deck.give_card())
    player.cards.append(deck.give_card())

    dealer.cards.append(deck.give_card())
    dealer.cards.append(deck.give_card())

    while not bust(player):
        print("\nYou have:", player.show_cards())
        print("Your hand is worth {} points.".format(player.cards_value()))
        if player.cards_value() == 21 and len(player.cards) == 2:
            if dealer.cards_value() == 21:
                print("Dealer has:", super(Dealer, dealer).show_cards())
                print("Dealer's hand is worth {} points.".format(dealer.cards_value()))
                print("Blackjack tie. Bets are nullified.")
                break
            else:
                print("BLACKJACK!")
                print("You win!")
                print("You win ${}.".format(bet))
                player.money += bet
                break
        print("Dealer has:", dealer.show_cards())
        action = input("Would you like to: [h]it, [s]tand, or su[r]render? ")

        if action.lower() in ['hit', 'h']:
            player.cards.append(deck.give_card())
        if action.lower() in ['stand', 's']:
            print("\nDealer's hole card:", dealer.show_hole_card())
            print("Dealer's hand is worth {} points.".format(dealer.cards_value()))
            if dealer.cards_value() == 21:
                    print("BLACKJACK!")
            while dealer.cards_value() < 17:
                print("Dealer hits.")
                dealer.cards.append(deck.give_card())
                print("Dealer has:", super(Dealer, dealer).show_cards())
                if dealer.cards_value() == 21:
                    print("BLACKJACK!")
                print("Dealer's hand is worth {} points.".format(dealer.cards_value()))
            if bust(dealer):
                print("Dealer busts! You win!")
                print("You win ${}.".format(bet))
                player.money += bet
                break
            elif player.cards_value() > dealer.cards_value():
                print("You win!")
                print("You win ${}.".format(bet))
                player.money += bet
                break
            elif player.cards_value() < dealer.cards_value():
                print("You lose.")
                print("You lose ${}.".format(bet))
                player.money -= bet
                break
            else:
                print("Push. You keep your bet.")
                break
        if action.lower() in ['surrender', 'r']:
            print("You surrender. You lose half of your bet.")
            print("You lose ${}.".format(bet))
            player.money -= bet/2
            break
    else:
        print("\nYou busted!")
        print("You have:", player.show_cards())
        print("Your hand is worth {} points.".format(player.cards_value()))
        print("You lose ${}.".format(bet))
        player.money -= bet

    if player.money == 0:
        print("Looks like you're out of money. Bye!")
        break

    if input("\nWould you like to play again? ").lower() not in ['yes', 'y', ""]:
        print("OK! Thanks for playing!")
        break
    else:
        player.cards = []
        dealer.cards = []