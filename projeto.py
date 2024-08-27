
pessoa = []

print("====================================\n")
print("|     Bem-vindo à Área de Login    |\n")
print("====================================\n")


cpf = input("Insira o seu CPF: ")


if cpf in pessoa:
    print(f"Bem-vindo, {pessoa[pessoa.index(cpf) + 1]}!")
else:
    print("Cadastro não encontrado! Por favor, cadastre-se.\n")

    
    nome = input("Digite seu nome: ")
    telefone = input("Informe seu telefone: ")
    email = input("Digite o seu e-mail: ")

   
    pessoa.append(cpf)
    pessoa.append(nome)
    pessoa.append(telefone)
    pessoa.append(email)

    
    print("\nDados pessoais armazenados com sucesso:")
    print(f"CPF: {pessoa[0]}")
    print(f"Nome: {pessoa[1]}")
    print(f"Telefone: {pessoa[2]}")
    print(f"Email: {pessoa[3]}")
