from random import randint

class Card(object):

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        re_str = ""
        re_str += self.suit[0]
        try: re_str += int(self.value)
        except:
            if


class Deck(object):


class Player(object):

    def __init__(self, name='Justin', money=2000):
        self.money = money
        self.name = name

    def bet(self):
        return

    def hit(self):
        return

    def stand(self):
        return


class Dealer(Player):

    def __init__(self):
        return


