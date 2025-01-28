class Card:
    def __init__(self, name: str, cost: int, power: int, card_type: str):
        """
        Representa una carta del juego.

        :param name: Nombre de la carta.
        :param cost: Coste de la carta (Dawn necesario para jugarla).
        :param power: Poder de ataque de la carta.
        :param card_type: Tipo de carta ('Leader', 'Character', 'Support', etc.).
        """
        self.name = name
        self.cost = cost
        self.power = power
        self.card_type = card_type

    def __str__(self):
        return f"{self.name} (Coste: {self.cost}, Poder: {self.power}, Tipo: {self.card_type})"
