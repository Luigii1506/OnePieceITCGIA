import random

class Card:
    def __init__(self, name: str, type_: str, power: int):
        self.name = name
        self.type = type_  # "Character", "Event", "Stage"
        self.power = power

    def __repr__(self):
        return f"{self.name} ({self.type}, {self.power} Power)"
