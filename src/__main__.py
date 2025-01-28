from core.game import Game
from core.player import Player
from core.cards import Card

def main():
    print("Bienvenido al motor de juego de One Piece TCG!")
    
    # Crear jugadores
    player1 = Player("Jugador 1")
    player2 = Player("Jugador 2")
    
    # Crear cartas de ejemplo
    luffy = Card("Monkey D. Luffy", cost=5, power=6000, card_type="Leader")
    zoro = Card("Roronoa Zoro", cost=3, power=5000, card_type="Character")
    nami = Card("Nami", cost=1, power=1000, card_type="Support")
    
    # Asignar cartas a jugadores
    player1.deck = [luffy, zoro, nami]
    player2.deck = [zoro, nami, luffy]
    
    # Iniciar el juego
    game = Game(player1, player2)
    #game.start()

if __name__ == "__main__":
    main()