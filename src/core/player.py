from core.deck import Deck

class Player:
    def __init__(self, name: str, deck: Deck):
        self.name = name
        self.deck = deck
        self.hand = []
        self.life_zone = []

    def mulligan(self):
        """ Devuelve la mano, baraja y roba de nuevo """
        print(f"{self.name} decide hacer mulligan.")
        self.deck.cards.extend(self.hand)  # Devuelve las cartas al mazo
        self.deck.shuffle()
        self.hand = self.deck.draw(5)  # Roba una nueva mano

    def start_game(self):
        """ Fase de inicio: Mulligan y distribución de vidas """
        self.hand = self.deck.draw(5)
        print(f"{self.name} ha robado su mano inicial: {self.hand}")

        mulligan_choice = input(f"{self.name}, ¿quieres hacer Mulligan? (s/n): ").strip().lower()
        if mulligan_choice == 's':
            self.mulligan()

        # Configurar la vida con cartas del mazo
        self.life_zone = self.deck.draw(self.deck.leader.life)
        print(f"{self.name} ha colocado {len(self.life_zone)} cartas en su zona de vida.")

    def __repr__(self):
        return f"Jugador: {self.name} | Vida: {len(self.life_zone)} | Mano: {len(self.hand)} cartas"
