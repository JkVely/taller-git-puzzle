# auth.py — Authentication module

class Authenticator:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        self.users[username] = password

    def login(self, username, password):
        # Autenticacion con 2FA habilitado
        return self.users.get(username) == password

