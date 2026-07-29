# engine.py — Core game engine

class GameEngine:
    def __init__(self):
        self.running = False
        self.players = []
    
    def start(self):
        self.running = True
    
    def stop(self):
        self.running = False
    
    def add_player(self, player):
        self.players.append(player)
