from markings import Mark
import os

class Board():
    def __init__(self):
        self.board = [Mark(" ") for _ in range(9)]
        self.win_positions = [[0,1,2], [3,4,5], [6,7,8], # Rows
                              [0,3,6], [1,4,7], [2,5,8], # Columns
                              [0,4,8], [2,4,6]]          # Diagonals

    def print_board(self):
        print(f" {self.board[0].value} | {self.board[1].value} | {self.board[2].value}")
        print("---+---+---")
        print(f" {self.board[3].value} | {self.board[4].value} | {self.board[5].value}")
        print("---+---+---")
        print(f" {self.board[6].value} | {self.board[7].value} | {self.board[8].value}\n")

