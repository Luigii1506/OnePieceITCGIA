class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]

    def start(self):
        """ Comienza el juego """
        print("¡El juego de One Piece TCG ha comenzado!")
        for player in self.players:
            player.start_game()

        print("Ambos jugadores han terminado su fase de inicio. ¡Que comience la batalla!")


# class Game:
#     def __init__(self, player1, player2):
#         self.players = [player1, player2]
#         self.turn = 1

#     def check_game_over(self):
#         """ Verifica si el juego debe terminar. """
#         for player in self.players:
#             if len(player.deck) == 0:
#                 print(f"¡El juego ha terminado! {player.name} se quedó sin cartas en el mazo.")
#                 return True
#         return False

#     def start(self):
#         """ Inicia el bucle del juego. """
#         while True:
#             print(f"\n--- Turno {self.turn} ---")
#             current_player = self.players[self.turn % 2]  

#             # Verificamos si el juego debe terminar
#             if self.check_game_over():
#                 print("Fin del juego.")
#                 break  

#             # Robar carta solo si hay en el mazo
#             if current_player.deck:
#                 drawn_card = current_player.deck.pop(0)
#                 current_player.hand.append(drawn_card)
#                 print(f"{current_player.name} roba una carta: {drawn_card.name}")
#             else:
#                 print(f"{current_player.name} no tiene cartas en su mazo.")

#             # Límite de Dawn (10 como en el TCG)
#             if current_player.dawn < 10:
#                 current_player.dawn += 1  

#             print(f"{current_player.name} tiene {current_player.dawn} Dawn y {len(current_player.hand)} cartas en mano.")
#             print(f"{current_player.name} finaliza su turno.")

#             self.turn += 1


# class Game:
#     def __init__(self, player1, player2):
#         """
#         Representa el flujo del juego.

#         :param player1: Instancia del primer jugador.
#         :param player2: Instancia del segundo jugador.
#         """
#         self.player1 = player1
#         self.player2 = player2
#         self.turn = 1

#     def start(self):
#         """
#         Comienza el juego.
#         """
#         print(f"El juego comienza entre {self.player1.name} y {self.player2.name}.")
#         while not self.is_game_over():
#             self.play_turn()

#     def play_turn(self):
#         """
#         Ejecuta un turno completo.
#         """
#         print(f"\n--- Turno {self.turn} ---")
#         current_player = self.player1 if self.turn % 2 != 0 else self.player2
#         opponent = self.player2 if current_player == self.player1 else self.player1
        
#         print(f"Turno de {current_player.name}.")
#         current_player.dawn += 2  # Ganar recursos (ejemplo).
#         current_player.draw_card()  # Robar una carta.
#         self.resolve_turn(current_player, opponent)
        
#         self.turn += 1

#     def resolve_turn(self, player, opponent):
#         """
#         Resuelve las acciones del turno.
#         """
#         print(f"{player.name} tiene {player.dawn} Dawn y {len(player.hand)} cartas en mano.")
#         # Aquí puedes añadir lógica para jugar cartas o atacar.
#         print(f"{player.name} finaliza su turno.")

#     def is_game_over(self):
#         """
#         Comprueba si el juego ha terminado.
#         """
#         if self.player1.life <= 0:
#             print(f"{self.player2.name} gana el juego!")
#             return True
#         elif self.player2.life <= 0:
#             print(f"{self.player1.name} gana el juego!")
#             return True
#         return False

