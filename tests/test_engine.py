# tests/test_engine.py — Unit tests for game engine

import sys
sys.path.insert(0, "src")

from engine import GameEngine
from player import Player
from scoring import ScoreBoard
from inventory import Inventory


def test_engine_start_stop():
    engine = GameEngine()
    engine.start()
    assert engine.running
    engine.stop()
    assert not engine.running


def test_player_movement():
    player = Player("Test")
    player.move(3, 4)
    assert player.position == [3, 4]


def test_scoring():
    board = ScoreBoard()
    board.add_score("Alice", 50)
    board.add_score("Bob", 100)
    assert board.get_leader() == "Bob"


def test_inventory():
    inv = Inventory()
    inv.add("Potion")
    assert inv.has("Potion")
    inv.remove("Potion")
    assert not inv.has("Potion")
