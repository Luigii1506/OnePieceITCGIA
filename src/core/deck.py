import random
from core.card import Card
from core.leader import Leader

class Deck:
    def __init__(self, leader: Leader, cards: list):
        if len(cards) != 50:
            raise ValueError("El mazo debe tener exactamente 50 cartas.")
        self.leader = leader
        self.cards = cards

    def shuffle(self):
        """ Baraja el mazo """
        random.shuffle(self.cards)

    def draw(self, num=1):
        """ Roba una cantidad específica de cartas """
        drawn_cards = [self.cards.pop(0) for _ in range(min(num, len(self.cards)))]
        return drawn_cards

    def __repr__(self):
        return f"Líder: {self.leader.name} | Cartas restantes: {len(self.cards)}"
