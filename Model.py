import random

class HangmanModel:
    def __init__(self):
        self.words = ["laptop", "tablet", "calculator", "smatrphone"]
        self.max_errors = 6
        self.reset()

    def reset(self):
        self.word = random.choice(self.words)
        self.guessed = ["_"] * len(self.word)
        self.errors = 0
        self.used_letters = []