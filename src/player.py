# player.py — Player movement and physics

class Player:
    def __init__(self, name):
        self.name = name
        self.position = [0, 0]
        self.health = 100
    
    def move(self, dx, dy):
        self.position[0] += dx
        self.position[1] += dy
    
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.die()
    
    def die(self):
        print(f"{self.name} has fallen.")
