def cadastrar_cliente(clientes):
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")

    cliente = {"nome": nome, "cpf": cpf}
    clientes.append(cliente)

    print("Cliente cadastrado com sucesso!")

