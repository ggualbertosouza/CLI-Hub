from programs import adivinha
import os
# Hub de programas

# inicializando hub


def main():
    os.system('cls')
    count = 0
    while count != 4:
        print('\n===== Bem vindo ao Hub de programas =====')
        print('\nEscolha o que quer experimentar hoje:\n')
        print('1 - Jogo da adivinha')
        print('2 - Loja de livros')
        print('3 - Regras dos jogos')
        print('4 - Sair \n')

        count = int(input(''))

        if count == 1:
            adivinha.jogar()

    print('tchau')


if __name__ == '__main__':
    main()
1
