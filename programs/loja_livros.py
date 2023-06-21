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

        count = int(input(''))

        if count == 1:
            os.system('cls')

            print('====== Adicione um novo livro =====\n')
            nomeLivro = input('Nome do livro: ')
            autor = input('Nome do autor: ')
            status = input('Já leu ou não?')
            livros.append([nomeLivro, autor, status])

        elif count == 2:
            os.system('cls')

            escolha = input('Pesquisa: ')
            for livro in livros:
                if escolha in livro:
                    print(livro)

        elif count == 3:
            os.system('cls')
            print('===== Aqui estão todos os seus livros =====')
            lib = open('Books.txt', 'r')
            for livro in livros:
                print(lib.read(livro))
            lib.close()

        elif count == 4:
            os.system('cls')
            print('Até a próxima! ')

    # Salvando em arquivo externo

    escrita = open('Books.txt', 'w')
    for livro in livros:
        escrita.write(','.join(livro) + '\n')
    escrita.close()


main()
