import random

class HangmanModel:
    def __init__(self):
        self.words = ["компьютер", "телефон", "машина", "программа", "карандаш", "дерево"]
        self.max_errors = 6
        self.reset_game()

    def reset_game(self):
        self.word = random.choice(self.words)
        self.guessed = ["_"] * len(self.word)
        self.errors = 0
        self.used_letters = []