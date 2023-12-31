from random import randint

__project__ = "TicTacToe"
__author__ = "Dale Doster"
__version__ = "0.1.0"
__license__ = "MIT"


board = [" " for _ in range(9)]
win_positions = [[0,1,2], [3,4,5], [6,7,8], # Rows
                 [0,3,6], [1,4,7], [2,5,8], # Columns
                 [0,4,8], [2,4,6]]          # Diagonals


def print_board(game_board):
    print(f" {game_board[0]} | {game_board[1]} | {game_board[2]}")
    print("---+---+---")
    print(f" {game_board[3]} | {game_board[4]} | {game_board[5]}")
    print("---+---+---")
    print(f" {game_board[6]} | {game_board[7]} | {game_board[8]}\n")


def init_game():
    print(f"{__project__}\nBy {__author__}\nv{__version__}\n")
    print_board(board)


def run_game():
    while True:
        print_board(get_user_move())
        if check_for_game_over():
            break
        
        print_board(get_AI_move())
        if check_for_game_over():
            break


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
    print(f"AI placed O in cell {random_value + 1}\n")    
    return board


def check_for_game_over():
    for win_state in win_positions:
        if board[win_state[0]] == "X" and board[win_state[1]] == "X" and board[win_state[2]] == "X":
            print("X - WINNER!!!")
            return True
        elif board[win_state[0]] == "O" and board[win_state[1]] == "O" and board[win_state[2]] == "O":
            print("O - WINNER!!!")
            return True


def main():
    init_game()
    run_game()


if __name__ == "__main__":
    main()