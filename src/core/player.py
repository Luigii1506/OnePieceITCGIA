class Player:
    def __init__(self, name: str):
        """
        Representa un jugador en el juego.

        :param name: Nombre del jugador.
        """
        self.name = name
        self.deck = []  # Lista de cartas en el mazo.
        self.hand = []  # Cartas en la mano.
        self.life = 5   # Vida inicial estándar.
        self.dawn = 0   # Recursos disponibles para jugar cartas.

    def draw_card(self):
        """
        Roba una carta del mazo y la añade a la mano.
        """
        if self.deck:
            card = self.deck.pop(0)
            self.hand.append(card)
            print(f"{self.name} roba una carta: {card.name}")
        else:
            print(f"{self.name} no tiene cartas en su mazo.")

    def __str__(self):
        return f"{self.name} (Vida: {self.life}, Dawn: {self.dawn}, Mano: {len(self.hand)} cartas)"
