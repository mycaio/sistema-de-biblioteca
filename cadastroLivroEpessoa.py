# Listas para armazenar dados
livros = []
pessoas = []
emprestimos = []
multas = []

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

def criar_multa():
    cpf = input("Digite o CPF da pessoa para aplicar a multa: ")
    for pessoa in pessoas:
        if pessoa[0] == cpf:
            valor_multa = float(input("Digite o valor da multa: "))
            motivo = input("Digite o motivo da multa: ")
            multas.append([cpf, valor_multa, motivo])
            print("Multa aplicada com sucesso!")
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
                    aplicar_multa = input("Aplicar multa? (S/N): ").upper()
                    if aplicar_multa == "S":
                        criar_multa()
                    
                    registrar_avaria = input("Registrar avaria? (S/N): ").upper()
                    if registrar_avaria == "S":
                        alterar_estado_livro()

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
    print("2) Empréstimos passados")
    print("3) Livros da Biblioteca")
    opcao = input("Opção: ")

    if opcao == "1":
        print("\n-------- RELATÓRIO DE EMPRÉSTIMOS VIGENTES --------")
        for emprestimo in emprestimos:
            for livro in livros:
                if emprestimo[1] == livro[0]:
                    print(f"\nLivro: {livro[1]}\n ID: {livro[0]}\n Emprestado por: {emprestimo[0]}\n")
        print("-----------------------------------------")
    elif opcao == "3":
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
-------- MENU DA BIBLIOTECA ---------
1) Livro
2) Pessoa
3) Multas
4) Empréstimo
5) Relatório
6) Sair  
""")
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            print(""" 
1) Cadastrar Livro
2) Alterar Situação do Livro
3) Alterar Estado do Livro
""")
            escolha = input("Digite o número da opção desejada: ")

            if escolha == "1":
                cadastrar_livro()
            elif escolha == "2":
                alterar_situacao_livro()
            elif escolha == "3":
                alterar_estado_livro()

        elif opcao == "2":
            print("""
1) Cadastrar Pessoa
2) Alterar Cadastro de Pessoa
""")
            escolha = input("Digite o número da opção desejada: ")

            if escolha == "1":
                cadastro_pessoa()
            elif escolha == "2":
                alterar_cadastro_pessoa()

        elif opcao == "3":
            criar_multa()

        elif opcao == "4":
            print("""
1) Criar Empréstimo
2) Baixar Empréstimo
3) Adiar Empréstimo
""")
            escolha = input("Digite o número da opção desejada: ")

            if escolha == "1":
                criar_emprestimo()
            elif escolha == "2":
                baixar_emprestimo()
            elif escolha == "3":
                adiar_emprestimo()

        elif opcao == "5":
            gerar_relatorio()

        elif opcao == "6":
            print("Volte sempre!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o programa
menu_principal()
