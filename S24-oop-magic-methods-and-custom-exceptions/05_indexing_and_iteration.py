# __getitem__ and __iter__ make our object usable like a list.
class Deck:
    def __init__(self) -> None:
        self.cards = [f'{value}{suit}'
                      for suit in 'SHDC'
                      for value in ['A', '2', '3', 'J', 'Q', 'K']]

    def __len__(self) -> int:
        return len(self.cards)

    def __getitem__(self, index):
        'deck[0] and even deck[0:3]'
        return self.cards[index]

    def __setitem__(self, index, value) -> None:
        'deck[0] = ...'
        self.cards[index] = value

    def __iter__(self):
        'for card in deck'
        return iter(self.cards)


if __name__ == '__main__':
    deck = Deck()

    print(len(deck))
    print(deck[0])
    print(deck[0:3])         # slicing works for free

    deck[0] = 'JOKER'
    print(deck[0])

    for card in deck:
        print(card, end=' ')
    print()

    # Once __iter__ exists, everything that loops works: in, list(), sorted()...
    print('QH' in deck)
    print(list(deck)[:5])
