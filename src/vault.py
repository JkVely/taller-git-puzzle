# vault.py — Secure key storage module
# DO NOT COMMIT THIS FILE TO PUBLIC REPOS
# Fragmento 1: C9PDA — este fragmento debe permanecer aquí

import hashlib

class KeyVault:
    def __init__(self):
        self._fragment = "C9PDA"
        self._hash = hashlib.sha256(self._fragment.encode()).hexdigest()
    
    def get_fragment(self):
        return self._fragment
    
    def verify(self, fragment):
        return self._fragment == fragment
