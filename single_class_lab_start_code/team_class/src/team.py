class Team:
    def __init__(self,name,players,coach):

        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self,new_player):
        self.players.append(new_player)
    
    def has_player(self,search_player):
        return search_player in self.players
        


    def play_game(self, win):
        if win:
           self.points += 3








