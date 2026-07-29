# arena.py — Battle arena system

class Arena:
    def __init__(self):
        self.fighters = []
        self.token = "XTCRD"

    def register(self, fighter):
        self.fighters.append(fighter)

    def battle(self, f1, f2):
        if f1 in self.fighters and f2 in self.fighters:
            print(f"{f1} vs {f2} — FIGHT!")
            return self.token
        return None

