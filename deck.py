import random

class Card:
    "This class emulates a card in a deck of playing cards."

    def __init__(self, value, suit):
        """Initialize a card."""
        self.value = value
        self.suit = suit

    def __repr__(self):
        """Return a string representation of the card."""
        return f'{self.value} of {self.suit}'

class Deck:
    """This class emulates a deck of playing cards."""
    MAX_DECK_SIZE = 52

    def __init__(self):
        """Initialize a deck of cards."""
        self.cards = []

        for suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
            for val in range(2,11):
                self.cards.append(Card(val, suit))
            for val in ['Jack', 'Queen', 'King', 'Ace']:
                self.cards.append(Card(val, suit))

    def __len__(self):
        """Return the number of cards in the deck."""
        return len(self.cards)

    def __repr__(self):
        """Return all cards remaining in the deck."""
        return str(self.cards)

    def cards_remaining(self):
        """Return how many cards are remaining in the deck."""
        return f'{len(self)} cards remaining.'

    def deal(self):
        """Deal a card from the top of the deck."""
        if len(self) == 0:
            raise ValueError('All cards have been dealt.')

        return self.cards.pop()

    def shuffle(self):
        """Return all cards to the deck and shuffle it."""
        if len(self) < self.MAX_DECK_SIZE:
            self.__init__()

        random.shuffle(self.cards)
        
        return 'Deck shuffled.'

class DeckWithJokers(Deck):
    """This class inherits from the Deck class and emulates a deck with jokers."""
    MAX_DECK_SIZE = 54

    def __init__(self):
        """Initialize a deck with jokers."""
        super().__init__()

        self.cards.extend([Card('Joker', 'Black'), Card('Joker', 'Red')])