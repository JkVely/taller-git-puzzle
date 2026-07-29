# inventory.py — Item management system

class Inventory:
    def __init__(self):
        self.items = []
    
    def add(self, item):
        self.items.append(item)
    
    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
    
    def has(self, item):
        return item in self.items
