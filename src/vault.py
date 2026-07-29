# vault.py — Secure key storage module
# DO NOT COMMIT THIS FILE TO PUBLIC REPOS
# Fragmento 1: C9PDA

class KeyVault:
    def __init__(self):
        self._fragment = "C9PDA"
    
    def get_fragment(self):
        return self._fragment
