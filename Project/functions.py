import random as rd


class game:
    def __init__(self):
        self.ChooserGame()

    def ChooserGame(self):
        print('Welcome to HUB GAMING')
        count = 0

        while True:
            count += 1

            game = int(
                input('1- Guessing Game, 2 - how many times i played?, 3 - exit'))

            if game == 1:
                self.GuessingGame()
            elif game == 2:
                print(count)
                break
            elif game == 3:
                print('Exit')
                break
            else:
                print('Bye')
                break

    def GuessingGame(self):
        count = 0
        print('Try your luck hitting the right number between 1-10')
        random = rd.randint(0, 10)

        while True:
            count += 1
            num = int(input('Choose a number'))

            if num == random:
                print('Congratulations!! Luck day')
                self.game = 0
                self.ChooserGame()
                break
            elif num != random and count < 10:
                print('Errou')
