from markings import Mark

class Player():
    def __init__(self, player_mark, name):
        self = self
        self.player_mark = player_mark
        self.name = name

    def get_player_mark(self):
        return self.player_mark.value
    
    def get_move(self):
        player_input = input("chose spot")