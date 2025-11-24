class HangmanView:
    def show_state(self, guessed, errors, used):
        print("\nСлово: ", " ".join(guessed))
        print(f"Ошибки ({errors}): {', '.join(used)}")

    def ask_letter(self):
        return input("Буква: ").lower()

    def show_result(self, text):
        print(text)

    def show_correct(self):
        print("Есть такая буква!")

    def show_wrong(self):
        print("Нет такой буквы!")

    def show_already(self):
        print("Эта буква уже была!")