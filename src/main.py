# main.py — Project Phoenix entry point

from engine import GameEngine
from player import Player
from scoring import ScoreBoard
from inventory import Inventory

def main():
    engine = GameEngine()
    engine.start()
    print("Project Phoenix initialized.")
    
    player = Player("Hero")
    engine.add_player(player)
    
    scoreboard = ScoreBoard()
    scoreboard.add_score("Hero", 100)
    
    inventory = Inventory()
    inventory.add("Sword")
    inventory.add("Shield")
    
    print(f"Player: {player.name}")
    print(f"Position: {player.position}")
    print(f"Score: {scoreboard.get_leader()}")
    print(f"Inventory: {inventory.items}")
    
    engine.stop()

if __name__ == "__main__":
    main()
