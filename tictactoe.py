from random import randint

__project__ = "TicTacToe"
__author__ = "Dale Doster"
__version__ = "0.1.0"
__license__ = "MIT"


board = [" " for _ in range(9)]


def print_board(game_board):
    print(f" {game_board[0]} | {game_board[1]} | {game_board[2]}")
    print("---+---+---")
    print(f" {game_board[3]} | {game_board[4]} | {game_board[5]}")
    print("---+---+---")
    print(f" {game_board[6]} | {game_board[7]} | {game_board[8]}\n")


def init_game():
    print_board(board)


def run_game():
    while True:
        print_board(get_user_move())
        print_board(get_AI_move())
        check_for_win()


def is_valid_position(position):
    return True if (position >= 0 and position <= 8) and (board[position] == " ") else False


def get_user_move():
    user_input = int(input("Player X - Select cell 1-9: "))
    
    while not is_valid_position(user_input - 1):
        user_input = int(input("Oops, that is not a valid position - Select cell 1-9: "))

    print("")
    board[user_input - 1] = "X"
    return board


def get_AI_move():
    random_value = randint(0, 8)

    while not is_valid_position(random_value):
        random_value = randint(0, 8)

    board[random_value] = "O"
    return board


def check_for_win():
    return True


def main():
    print(f"{__project__}\nBy {__author__}\nv{__version__}\n")

    init_game()
    run_game()


if __name__ == "__main__":
    main()