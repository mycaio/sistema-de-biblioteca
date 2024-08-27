# Lista de livros e lista de pessoas
livros = []
pessoas = []

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

def relatorio():
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
            
def cadastro_pessoa():
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

# Menu inicial
def menu_principal():
    while True:
        print("""
       .--.                   .---.   
   .---|__|           .-.     |~~~|   
.--|===|--|_          |_|     |~~~|--.
|  |===|  |'\     .---!~|  .--|   |--|
|%%|   |  | '\    |===| |--|%%|   |  |
|%%|   |  |\ '\   |   | |__|  |   |  |
|  |   |  | \  \  |===| |==|  |   |  |
|  |   |__|  \ '\ |   |_|__|  |~~~|__|
|  |===|--|   \ '\|===|~|--|%%|~~~|--|
^--^---'--^    `-'`---^-^--^--^---'--'
-------- MENU DA BIBLIOTECA ---------
-----------------------------------------
1) Cadastrar
2) Empréstimo
3) Relatório
4) Sair  
""")

        navegacao_inicial = int(input("Digite o número da opção desejada: "))

        if navegacao_inicial == 1:
            print(""" 
1) Livro
2) Pessoa
          """)
            escolha_cadastro = int(input("Digite o número da opção desejada: "))

            if escolha_cadastro == 1:
                while True:
                    cadastrar_livro()
                    novo_cadastro = input("Deseja cadastrar outro livro? (S/N): ").upper()
                    if novo_cadastro == "N":
                        break
            elif escolha_cadastro == 2:
                while True:
                    cadastro_pessoa()
                    novo_cadastro = input("Deseja cadastrar outra pessoa? (S/N): ").upper()
                    if novo_cadastro == "N":
                        break

        elif navegacao_inicial == 3:
            relatorio()

        elif navegacao_inicial == 4:
            print("Volte sempre!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o programa
menu_principal()
