import random
import os
# Jogo da adivinha


class jogar:

    # Inicializador do menu interativo
    def __init__(self):
        os.system('cls')

        count = 0

        while count != 4:
            print('\n##### Jogo da adivinha #####\n')
            print('1 - Jogar')
            print('2 - Estatísticas')
            print('3 - Regras')
            print('4 - Sair\n')

            count = int(input(''))

            if count == 1:
                self.jogo()
            if count == 2:
                self.estatistica(self.tentativas)
            if count == 3:
                self.regras()

        print('voltar pra tela inicial')

    def jogo(self):
        os.system('cls')

        count = 0
        num = random.randint(0, 10)

        while True:
            count += 1
            escolha = int(input('Escolha um número de 1 a 10: '))

            if escolha == num:
                print('Parabéns, acertou! Seu dia de sorte')
                break
            elif escolha != num and count < 10:
                print('Errou, tente novamente, você consegue!!')
                print(f'Tentativa {count}')

        self.tentativas = count

    def estatistica(self, tentativas):
        os.system('cls')

        if tentativas is None:
            print('Você ainda não teve nenhuma tentativa.')

        print(f'Você errou {tentativas - 1} até acertar!')
        print('Continue tentando, você consegue acertar de primeira!')

    def regras(self):
        os.system('cls')

        print('===== Regras ======')
        print('É simples, apenas tente suas sorte.\n Use os números indicados para navegar pelos menos.')
