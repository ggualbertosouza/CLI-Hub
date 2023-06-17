import functions

class game:
    def __init__(self):
        num = int(input(('1 - Play, 2 - Exit')))
        if num == 1:
            functions.game()
        elif num == 2:
            print('Sair')


game()
