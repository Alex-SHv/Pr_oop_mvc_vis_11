from Model import ManModel
from View import ManView

class ManController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def letter(self, letter):
        if letter in self.letters:
            return None 

        self.letters.append(letter)

        if letter in self.word:
            for i, ch in enumerate(self.word):
                if ch == letter:
                    self.guessed[i] = letter
            return True
        else:
            self.errors += 1
            return False

    def win(self):
        return "" not in self.guessed

    def lose(self):
        return self.errors >= self.max_errors