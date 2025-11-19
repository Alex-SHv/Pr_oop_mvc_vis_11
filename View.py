class ManView:
    def show(self, guess, error, used):
        print("\nWord: ", "".join(guess))
        print(f"Errors ({error}): {','.join(used)}")

    def inp_letter(self):
        return input("Letter: ").lower()

    def show(self, text):
        print("There is such a letter")