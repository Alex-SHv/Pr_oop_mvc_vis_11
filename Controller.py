from Model import HangmanModel
from View import HangmanView

class HangmanController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    
    def check_letter(self, letter):
        if letter in self.model.used_letters:
            return None 

        self.model.used_letters.append(letter)

        if letter in self.model.word:
            for i, ch in enumerate(self.model.word):
                if ch == letter:
                    self.model.guessed[i] = letter
            return True
        else:
            self.model.errors += 1
            return False

    def is_win(self):
        return "_" not in self.model.guessed

    def is_lose(self):
        return self.model.errors >= self.model.max_errors

    def game_loop(self):
        while True:
            self.view.show_state(self.model.guessed, self.model.errors, self.model.used_letters)

            letter = self.view.ask_letter()

            result = self.check_letter(letter)

            if result is None:
                self.view.show_already()
                continue
            elif result:
                self.view.show_correct()
            else:
                self.view.show_wrong()

            if self.is_win():
                self.view.show_state(self.model.guessed, self.model.errors, self.model.used_letters)
                self.view.show_result("\n Ура !!!  Вы угадали слово!")
                break

            if self.is_lose():
                self.view.show_result(f"\n Висилица @ загадоное слово: {self.model.word}")
                break


model = HangmanModel()
view = HangmanView()
controller = HangmanController(model, view)

controller.game_loop()