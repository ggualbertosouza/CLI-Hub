import os


def main():
    os.system('cls')
    count = 0

    livros = []

    while count != 4:
        print('===== Minha estante de livros =====')
        print('\nAqui você guarda alguns livros que já leu e mostra para o mundo.\n')
        print('1 - Adicionar Livro')
        print('2 - Pesquisa livro')
        print('3 - Ver toda a estante')
        print('4 - Sair\n')

        escolha = int(input(''))

        if escolha == 1:
            os.system('cls')

            print('====== Adicione um novo livro =====\n')
            nomeLivro = input('Nome do livro: ')
            autor = input('Nome do autor: ')
            status = input('Já leu ou não?')

            livros.append([nomeLivro, autor, status])

        elif escolha == 2:
            os.system('cls')

            i = input('Pesquisa: ')
            for livro in livros:
                if i in livro:
                    print(livro)
        elif escolha == 3:
            pass


main()
