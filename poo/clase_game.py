class Game():
    def __init__(self, name, rank): 
        self.name = name
        self.rank = rank


player1 = Game("Alpha", 1)
player2 = Game("Delta", 2)

print(player1.name, player1.rank)
print(player2.name, player2.rank)

