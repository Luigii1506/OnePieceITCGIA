from core.card import Card
from core.leader import Leader
from core.deck import Deck
from core.player import Player
from core.game import Game

# Crear un líder para cada jugador
luffy = Leader("Monkey D. Luffy", 5, "Otorga Rush a un aliado una vez por turno")
zoro = Leader("Roronoa Zoro", 5, "Aumenta el poder de todos los aliados en +1000")

# Crear 50 cartas aleatorias para cada jugador
cards_p1 = [Card(f"Carta {i+1}", "Character", 5000) for i in range(50)]
cards_p2 = [Card(f"Carta {i+1}", "Character", 5000) for i in range(50)]

# Crear mazos
deck_p1 = Deck(luffy, cards_p1)
deck_p2 = Deck(zoro, cards_p2)

# Barajar mazos
deck_p1.shuffle()
deck_p2.shuffle()

# Crear jugadores
player1 = Player("Jugador 1", deck_p1)
player2 = Player("Jugador 2", deck_p2)

# Iniciar juego
game = Game(player1, player2)
game.start()
