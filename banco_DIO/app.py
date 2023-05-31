print("+++++++++ Saudações bancárias, cliente! +++++++")

def valorPositivo():
    a = int(input('### informe o valor de depósito ### '))
    if a >= 1:
        print('depósito realizado com sucesso! você pode vê-lo no extrato!') 
    if a <= 0:
        print('você precisa depositar um valor positivo')
    return a

a = valorPositivo()

def operacaoSaque(a):
    qntSaque = 3
    saque = int(input('Digite o valor a ser Sacado: '))
    if saque >= 500:
        qntSaque -= 1
        a -= saque
        print("você realizou um saque de", saque)
    else:
        print('operação inválida')
    if qntSaque > 0 and qntSaque == 2:
        print('você ainda possui', qntSaque, 'saque(S)')
    else:
        print('você não possui mais saques')
    return a

a = operacaoSaque(a)

def extrato(a):
    v_extrato = a
    if a == 0:
        print('não foram realizadas movimentações')
    print('deseja imprimir o valor do extrato? Se sim, digite "S". Se não, digite "N"')
    resposta = input('')
    if resposta == "S":
        print(a)
    elif resposta == "N":
        a = valorPositivo()
        extrato(a)
    else:
        print("obrigado por usar o sistema bancário")

extrato(a)
