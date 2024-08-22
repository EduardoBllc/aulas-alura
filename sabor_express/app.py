import os

restaurantes = [{'nome': 'Pizza', 'categoria': 'Italiana', 'ativo': False},
                {'nome': 'Sushi', 'categoria': 'Chinesa', 'ativo': True},
                {'nome': 'Cachorro do Jeca', 'categoria': 'Fast-Food', 'ativo': False}]


def exibir_nome():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)


def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar/Desativar restaurante')
    print('4. Sair')


def finalizar_app():
    exibir_subtitulo('Finalizando o app')
    exit(0)


def voltar_menu_principal():
    print()
    input('Pressione qualquer tecla para retornar ao menu inicial... ')
    main()


def opcao_invalida():
    print('\nA opção escolhida deve ser um dos números listados!')
    voltar_menu_principal()


def exibir_subtitulo(subtitulo):
    os.system('cls')
    linha = '*' * (len(subtitulo))
    print(linha)
    print(subtitulo)
    print(linha)
    print()


def cadastrar_restaurante():
    """
    Função responsável por cadastrar um restaurante
    """

    exibir_subtitulo('Cadastro de restaurante')
    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria_restaurante = input('Digite o categoria do restaurante: ')

    dados_restaurante = {'nome': nome_restaurante,
                         'categoria': categoria_restaurante,
                         'ativo': False}

    restaurantes.append(dados_restaurante)

    print(f'Restaurante {nome_restaurante} cadastrado com sucesso!')
    voltar_menu_principal()


def listar_restaurantes():
    """
    Função responsável por listar todos os restaurantes
    """

    exibir_subtitulo('Listagem de restaurantes')
    print('Restaurantes cadastrados:')
    print()

    cabecalho = f'  {'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'}'

    print(cabecalho)
    print(len(cabecalho) * '_')
    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativo' if restaurante['ativo'] else 'Inativo'
        print(f' {nome.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_menu_principal()


def alternar_estado_restaurante():
    """
    Função responsável por alternar o estado do restaurante
    """

    exibir_subtitulo('Alterando estado do restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja mudar o estado: ')

    restaurantes_filtrados = list(filter(lambda restaurante: restaurante['nome'] == nome_restaurante, restaurantes))

    if len(restaurantes_filtrados) == 1:
        restaurante_escolhido = restaurantes_filtrados[0]
        restaurante_escolhido['ativo'] = not restaurante_escolhido['ativo']
        print()
        print(f'Estado do restaurante {restaurante_escolhido['nome']} '
              f'alterado com sucesso para {"Ativo" if restaurante_escolhido['ativo'] else "Inativo"}')

    elif len(restaurantes_filtrados) == 0:
        print(f'Não foi encontrado restaurante com nome de {nome_restaurante}')

    elif len(restaurantes_filtrados) > 1:
        print(f'Foram encontrados mais de um restaurante com nome {nome_restaurante}, '
              'isso não deveria acontecer! Revise os restaurantes cadastrados')

    voltar_menu_principal()


def escolher_opcao():
    opcao_escolhida = input('\nEscolha uma opção: ')

    try:
        opcao = int(opcao_escolhida)
    except ValueError:
        opcao_invalida()
        return

    match opcao:
        case 1:
            cadastrar_restaurante()
        case 2:
            listar_restaurantes()
        case 3:
            alternar_estado_restaurante()
        case 4:
            finalizar_app()
        case _:
            opcao_invalida()
            return


def main():
    os.system('cls')
    exibir_nome()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
