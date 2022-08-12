""" this module will hold our Card class """

class CardValueException(Exception):
    pass

class Card:
    #suits = ['hearts', 'diamonds', 'clubs', 'spades']
    #values = [str(num) for num in range(2,11)]
    #values.extend('JQKA')

    def __init__(self, value="", suit=""):
        self.value = value
        self.suit = suit
        self.check_parameters()

    def __repr__(self):
        return f"Card('{self.value}', '{self.suit}')"

    def __str__(self):
        return f'{self.value} of {self.suit}'

    def check_parameters(self):
        """ check to see if the input parameters make sense """
        if self.value not in self.values:
            raise CardValueError('Card value not recognized')
        if self.suit not in self.suits:
            print('bad suit!')

    def points(self):
        return int(self.value)


class FrenchCard(Card):
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    values = [str(num) for num in range(2,11)]
    values.extend('JQKA')


class SwissCard(Card):
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    values = [str(num) for num in range(6,11)]
    values.extend('JQKA')


class NerdCard(Card):
    values = [str(num) for num in range(32)]

    def check_parameters(self):
        if self.value not in self.values:
            raise CardValueError('Card value not recognized')
