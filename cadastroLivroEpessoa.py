import os #biblioteca para limapar terminal

# Listas para armazenar dados
livros = []
pessoas = []
emprestimos = []
multas = []


def limpar_terminal():
    os.system('cls')

def cadastrar_livro():
    codigo = input("\nDigite o código do livro: ")
    for livro in livros:
        if livro[0] == codigo:
            print("Código já cadastrado.")
            return
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    estado = input("Digite o estado do livro (Novo/Usado/Defeito/Baixado): ")
    situacao = "Disponível"  # Estado inicial do livro é "Disponível"
    
    livros.append([codigo, titulo, autor, estado, situacao])
    print("\nLivro cadastrado com sucesso!")
    print(f"""---------DADOS DO LIVRO---------
 Código: {codigo}\n Título: {titulo}\n Autor: {autor}\n Estado: {estado}\n Situação: {situacao}
-------------------------------------""")

def alterar_situacao_livro():
    codigo = input("\nDigite o código do livro: ")
    for livro in livros:
        if livro[0] == codigo:
            nova_situacao = input("Digite a nova situação do livro (Disponível/Emprestado/Reservado): ")
            livro[4] = nova_situacao
            print("Situação alterada com sucesso!")
            return
    print("Livro não encontrado.")

def alterar_estado_livro():
    codigo = input("\nDigite o código do livro: ")
    for livro in livros:
        if livro[0] == codigo:
            novo_estado = input("Digite o novo estado do livro (Novo/Usado/Defeito/Baixado): ")
            livro[3] = novo_estado
            print("Estado alterado com sucesso!")
            return
    print("Livro não encontrado.")

def cadastro_pessoa():
    cpf = input("Insira o seu CPF: ")
    for pessoa in pessoas:
        if pessoa[0] == cpf:
            print("CPF já cadastrado.")
            return

    nome = input("Digite seu nome: ")
    telefone = input("Informe seu telefone: ")
    email = input("Digite o seu e-mail: ")
    pessoas.append([cpf, nome, telefone, email])
    print("\nDados pessoais armazenados com sucesso!")

def alterar_cadastro_pessoa():
    cpf = input("Digite o CPF da pessoa a ser alterada: ")
    for pessoa in pessoas:
        if pessoa[0] == cpf:
            print(f"Dados atuais: Nome: {pessoa[1]}, Telefone: {pessoa[2]}, Email: {pessoa[3]}")
            pessoa[1] = input("Digite o novo nome: ")
            pessoa[2] = input("Digite o novo telefone: ")
            pessoa[3] = input("Digite o novo email: ")
            print("Cadastro alterado com sucesso!")
            return
    print("Pessoa não encontrada.")

def criar_emprestimo():
    cpf = input("Digite o CPF da pessoa que vai realizar o empréstimo: ")
    pessoa = None
    for p in pessoas:
        if p[0] == cpf:
            pessoa = p
            break
    if not pessoa:
        print("Pessoa não encontrada. Cadastre a pessoa primeiro.")
        return

    codigo_livro = input("Digite o código do livro a ser emprestado: ")
    for livro in livros:
        if livro[0] == codigo_livro:
            if livro[4] == "Disponível":
                emprestimos.append([cpf, codigo_livro])
                livro[4] = f"Emprestado por {pessoa[1]}"
                print(f"Empréstimo realizado com sucesso! {pessoa[1]} emprestou '{livro[1]}'.")
                return
            else:
                print("Livro não disponível para empréstimo.")
                return
    print("Livro não encontrado.")

def baixar_emprestimo():
    cpf = input("Digite o CPF da pessoa que realizou o empréstimo: ")
    codigo_livro = input("Digite o código do livro a ser devolvido: ")

    for i, emprestimo in enumerate(emprestimos):
        if emprestimo[0] == cpf and emprestimo[1] == codigo_livro:
            emprestimos.pop(i)

            for livro in livros:
                if livro[0] == codigo_livro:
                    alterar_situacao_livro()
                    print("Empréstimo baixado com sucesso!")
                    return
    print("Empréstimo não encontrado.")

def adiar_emprestimo():
    cpf = input("Digite o CPF da pessoa que realizou o empréstimo: ")
    codigo_livro = input("Digite o código do livro: ")

    for emprestimo in emprestimos:
        if emprestimo[0] == cpf and emprestimo[1] == codigo_livro:
            nova_data = input("Digite a nova data de devolução: ")
            print("Empréstimo adiado com sucesso!")
            return
    print("Empréstimo não encontrado.")

def gerar_relatorio():
    print("\nEscolha o tipo de relatório:")
    print("1) Empréstimos vigentes")
    print("2) Livros da Biblioteca")
    opcao = input("Opção: ")

    if opcao == "1":
        print("\n-------- RELATÓRIO DE EMPRÉSTIMOS VIGENTES --------")
        for emprestimo in emprestimos:
            for livro in livros:
                if emprestimo[1] == livro[0]:
                    print(f"\nLivro: {livro[1]}\n ID: {livro[0]}\n Emprestado por: CPF: {emprestimo[0]}\n")
        print("-----------------------------------------")
    elif opcao == "2":
        print("\n-------- RELATÓRIO DE LIVROS --------")
        for livro in livros:
            print(f"""
 Código: {livro[0]}
 Título: {livro[1]}
 Autor: {livro[2]}
 Estado: {livro[3]}
 Situação: {livro[4]}
-----------------------------------------
""")
    else:
        print("Opção inválida.")

# Menu inicial
def menu_principal():
    while True:
        print("""
       .--.                   .---.           
   .---|__|           .-.     |~~~|   
.--|===|--|_          |_|     |~~~|--.
|  |===|  |'\     .---!~|  .--|   |--|
|%%|   |  |.'\    |===| |--|%%|   |  |
|%%|   |  |\.'\   |   | |__|  |   |  |
|  |   |  | \  \  |===| |==|  |   |  |
|  |   |__|  \.'\ |   |_|__|  |~~~|__|
|  |===|--|   \.'\|===|~|--|%%|~~~|--|
^--^---'--^    `-'`---^-^--^--^---'--'
-------- MENU DA BIBLIOTECA ---------
1) Livro
2) Pessoa
3) Empréstimo
4) Relatório
5) Sair  
""")
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            limpar_terminal()
            print(""" 
1) Cadastrar Livro
2) Alterar Situação do Livro
3) Alterar Estado do Livro
""")
            escolha = input("Digite o número da opção desejada: ")

            if escolha == "1":
                limpar_terminal()
                cadastrar_livro()
            elif escolha == "2":
                limpar_terminal()
                alterar_situacao_livro()
            elif escolha == "3":
                limpar_terminal()
                alterar_estado_livro()

        elif opcao == "2":
            limpar_terminal()
            print("""
1) Cadastrar Pessoa
2) Alterar Cadastro de Pessoa
""")
            escolha = input("Digite o número da opção desejada: ")

            if escolha == "1":
                limpar_terminal()
                cadastro_pessoa()
            elif escolha == "2":
                limpar_terminal()
                alterar_cadastro_pessoa()

        elif opcao == "3":
            limpar_terminal()
            print("""
1) Criar Empréstimo
2) Baixar Empréstimo
""")
            escolha = input("Digite o número da opção desejada: ")

            if escolha == "1":
                limpar_terminal()
                criar_emprestimo()
            elif escolha == "2":
                limpar_terminal()
                baixar_emprestimo()
            elif escolha == "3":
                limpar_terminal()
                adiar_emprestimo()

        elif opcao == "4":
            limpar_terminal()
            gerar_relatorio()

        elif opcao == "5":
            limpar_terminal()
            print("Volte sempre!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o programa
menu_principal()
