# scoring.py — Score tracking system

class ScoreBoard:
    def __init__(self):
        self.scores = {}

    def add_score(self, player, points):
        if player not in self.scores:
            self.scores[player] = 0
        self.scores[player] += points

    def get_leader(self):
        return max(self.scores, key=self.scores.get) if self.scores else None

