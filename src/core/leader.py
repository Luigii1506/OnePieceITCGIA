class Leader:
    def __init__(self, name: str, life: int, ability: str):
        self.name = name
        self.life = life
        self.ability = ability

    def __repr__(self):
        return f"{self.name} (Vida: {self.life}, Habilidad: {self.ability})"
