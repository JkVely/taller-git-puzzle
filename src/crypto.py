# crypto.py — Encrypted communication channel
# ROT13 cipher for secure messaging

CIPHERS = {
    "channel_1": "Ry frthaqb senzragb rfgn ra yn enzn qr Inyragvan"
}

def decrypt(text):
    result = []
    for c in text:
        if "a" <= c <= "z":
            result.append(chr((ord(c) - ord("a") + 13) % 26 + ord("a")))
        elif "A" <= c <= "Z":
            result.append(chr((ord(c) - ord("A") + 13) % 26 + ord("A")))
        else:
            result.append(c)
    return "".join(result)

class SecureChannel:
    def __init__(self, channel="channel_1"):
        self.encrypted = CIPHERS.get(channel, "")
    
    def read(self):
        return decrypt(self.encrypted)

