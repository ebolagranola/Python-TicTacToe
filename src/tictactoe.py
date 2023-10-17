from board import Board
from player import Player
from markings import Mark

__project__ = "TicTacToe"
__author__ = "Dale Doster"
__version__ = "0.1.0"
__license__ = "MIT"


game_board = Board()


def init_game():
    print(f"{__project__}\nBy {__author__}\nv{__version__}\n")

    player_mark = input("Player1 select X or O: ")
    while (player_mark != "X" and player_mark != "O"):
        player_mark = input("Player1 select X or O: ")

    player1 = Player(Mark(player_mark), "Player1")
    print(f"{player1.name} playing as: {player1.get_player_mark()}\n")

    set_player2 = input("Player2 as (1)Human or (2)AI: ")
    while (set_player2 != "1" and set_player2 != "2"):
        set_player2 = input("Set Player2 as (1)Human or (2)AI: ")


def game_loop():
    while True:
        game_board.print_board()


def main():
    init_game()
    game_loop()


if __name__ == "__main__":
    main()