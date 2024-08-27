# Inicializa as listas
livros = []
pessoas = []

area = "BEM VINDO"

def cabecalho(area):
    print(f"""
       .--.                   .---.   
   .---|__|           .-.     |~~~|   
.--|===|--|_          |_|     |~~~|--.
|  |===|  |'\\     .---!~|  .--|   |--|
|%%|   |  | '\\    |===| |--|%%|   |  |
|%%|   |  |\\ '\\   |   | |__|  |   |  |
|  |   |  | \\  \\  |===| |==|  |   |  |
|  |   |__|  \\ '\\ |   |_|__|  |~~~|__|
|  |===|--|   \\ '\\|===|~|--|%%|~~~|--|
^--^---'--^    `-'`---^-^--^--^---'--'
-------- {area} ---------
-----------------------------------------
""")

def pagina(area):
    while True:
        cabecalho(area)
        print("""      
1) CADASTRAR
2) BUSCAR
3) RELATORIO
4) SAIR
""")

        try:
            navegacao_inicial = int(input("Digite o número da opção desejada: "))
            if navegacao_inicial in [1, 2, 3, 4]:
                return navegacao_inicial
            else:
                print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def cadastrar_pessoa():
    cpf = input("Insira o seu CPF: ")

    # Verifica se o CPF já está cadastrado
    for pessoa in pessoas:
        if pessoa[0] == cpf:
            print(f"Bem-vindo, {pessoa[1]}! Deseja realizar um empréstimo ou devolução?")
            return

    print("Cadastro não encontrado! Por favor, cadastre-se.\n")

    nome = input("Digite seu nome: ")
    telefone = input("Informe seu telefone: ")
    email = input("Digite o seu e-mail: ")

    # Adiciona a nova pessoa à lista de pessoas
    pessoas.append([cpf, nome, telefone, email])

    print("\nDados pessoais armazenados com sucesso:")
    print(f"CPF: {cpf}")
    print(f"Nome: {nome}")
    print(f"Telefone: {telefone}")
    print(f"Email: {email}")

def relatorio_pessoa():
    if len(pessoas) == 0:
        print("Nenhuma pessoa cadastrada.")
    else:
        print("\n-------- RELATÓRIO DE PESSOAS --------")
        for pessoa in pessoas:
            print(f"""
 CPF: {pessoa[0]}
 Nome: {pessoa[1]}
 Telefone: {pessoa[2]}
 Email: {pessoa[3]}
-----------------------------------------
""")

def cadastrar_livro():
    codigo = input("\nDigite o código do livro: ")
    for livro in livros:
        if livro[0] == codigo:
            print("Código já cadastrado.")
            return
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    estado = input("Digite o estado do livro (Novo/Usado/Defeito/Baixado): ")

    # Adicionar o novo livro à lista de livros
    livros.append([codigo, titulo, autor, estado])
    print("\nLivro cadastrado com sucesso!")
    print(f"""---------DADOS DO LIVRO---------
 Código: {codigo}\n Título: {titulo}\n Autor: {autor}\n Estado: {estado}
-------------------------------------""")

def relatorio_livro():
    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
    else:
        print("\n-------- RELATÓRIO DE LIVROS --------")
        for livro in livros:
            print(f"""
 Código: {livro[0]}
 Título: {livro[1]}
 Autor: {livro[2]}
 Estado: {livro[3]}
-----------------------------------------
""")

def menu_principal():
    while True:
        cabecalho("MENU PRINCIPAL")
        print("""      
1) PESSOAS
2) LIVROS
3) SAIR
""")

        try:
            navegacao_inicial = int(input("Digite o número da opção desejada: "))
            if navegacao_inicial in [1, 2, 3]:
                return navegacao_inicial
            else:
                print("Opção inválida. Por favor, escolha uma opção entre 1 e 3.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def navegacao_principal():
    while True:
        valor_nav = menu_principal()
        if valor_nav == 1:
            while True:
                resultado_pagina_pessoa = pagina("PESSOAS")
                if resultado_pagina_pessoa == 4:
                    break  # Sai do loop da página de pessoas e volta para o menu principal
                elif resultado_pagina_pessoa == 1: 
                    cadastrar_pessoa()
                elif resultado_pagina_pessoa == 3:
                    relatorio_pessoa()
        elif valor_nav == 2:
            while True:
                resultado_pagina_livro = pagina("LIVROS")
                if resultado_pagina_livro == 4:
                    break  # Sai do loop da página de livros e volta para o menu principal
                elif resultado_pagina_livro == 1: 
                    cadastrar_livro()
                elif resultado_pagina_livro == 3:
                    relatorio_livro()
        elif valor_nav == 3:
            print("Saindo do programa...")
            break  # Sai do loop principal e encerra o programa

# Chama a função navegacao_principal para iniciar o programa
navegacao_principal()