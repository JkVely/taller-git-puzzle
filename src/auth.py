# auth.py — Authentication module

class Authenticator:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        self.users[username] = password

    def login(self, username, password):
        # TODO: implementar OAuth 2.0
        return self.users.get(username) == password

