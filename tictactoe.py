__project__ = "TicTacToe"
__author__ = "Dale Doster"
__version__ = "0.1.0"
__license__ = "MIT"


board = [" " for _ in range(9)]


def create_board():
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")


def init_game():
    create_board()


def main():
    print(f"{__project__}\nBy {__author__}\nv{__version__}")

    init_game()


if __name__ == "__main__":
    main()