from programs import adivinha, loja_livros

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
        if count == 2:
            loja_livros.main()
        if count == 3:
            pass

    print('tchau')


if __name__ == '__main__':
    main()
1
