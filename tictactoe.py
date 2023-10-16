__project__ = "TicTacToe"
__author__ = "Dale Doster"
__version__ = "0.1.0"
__license__ = "MIT"


board = [" " for _ in range(9)]


def create_board(game_board):
    print(f" {game_board[0]} | {game_board[1]} | {game_board[2]}")
    print("---+---+---")
    print(f" {game_board[3]} | {game_board[4]} | {game_board[5]}")
    print("---+---+---")
    print(f" {game_board[6]} | {game_board[7]} | {game_board[8]}\n")


def update_board():
    print()


def init_game():
    create_board(board)


def request_input():
    user_input = input("Select cell 1-9: ");
    print(user_input)


def main():
    print(f"{__project__}\nBy {__author__}\nv{__version__}\n")

    init_game()
    request_input()


if __name__ == "__main__":
    main()