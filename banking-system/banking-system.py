menu = """

1 - Depositar
2 - Sacar
3 - Extrato
4 - Cadastrar cliente
5 - Nova conta
6 - Listar contas
7 - Logout

"""

AGENCIA = "0001"
saldo = 0
limite = 500
extrato = " "
numero_saques = 0
limite_saques = 3
usuarios = []
contas = []

def depositar(saldo, extrato, valor_deposito, /):
    if valor_deposito > 0:
        print(" ")
        print("Depósito realizado com sucesso!")
        saldo += valor_deposito
        print(" ")
        extrato += f"""Depósito: R$ {valor_deposito: .2f} \n"""
    else:
        print("Valor inválido!")
    print(" ")
    print(f"Saldo atual: R$ {saldo:.2f}")
    return saldo, extrato
    
def sacar(*, saldo, extrato, limite, numero_saques, limite_saques, valor_saque):
    if numero_saques < limite_saques:
        if valor_saque <= limite:
            if valor_saque <= saldo:
                print(" ")
                print("Saque realizado com sucesso!")
                saldo -= valor_saque
                extrato += f"""Saque: R$ -{valor_saque: .2f}\n"""
            else: 
                print(" ")
                print("Não será possível sacar o dinheiro por falta de saldo.")
        else:
            print("Valor do saque excede o limite disponível. Valor disponível: R$ 500.00")
    else:
        print(" ")
        print("Excedido a quantidade de saque. " )
    numero_saques += 1
    print(" ")
    print(f"Saldo atual: R$ {saldo:.2f}")
    return saldo, extrato

def exibir_extrato(saldo, / , * , extrato):
    if extrato == ' ':
        print("Não foram realizadas movimentações.") 
    else:
        print(extrato)   
      
    print(f"Saldo atual: R$ {saldo:.2f}")

def criar_usuario(usuarios):
    nome = input("Digite seu nome completo: ")
    data_de_nascimento = input("Digite sua data de nascimento no formato (dd-mm-aaaa): ")
    cpf = input("Digite seu cpf com somente números: ")
    endereco = input("Digite seu endereço no formato (logradouro, nro - bairro - cidade/sigla estado): ")
    
    usuario = filtrar_cpf(cpf, usuarios)

    if usuario:
        print("Usuário já existente!")
        return
    else:
        usuarios.append({"nome":nome, "data_de_nascimento":data_de_nascimento, "cpf":cpf, "endereco":endereco})
        print("Cadastro feito com sucesso!")

def criar_contas(agencia, numero_da_conta, usuarios, contas):
    cpf = input("Digite seu cpf: ")

    usuario = filtrar_cpf(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        contas.append({"agencia":agencia, "numero_da_conta":numero_da_conta, "usuario":usuario })
        return contas
    else:    
        print("CPF não encontrado!")

def filtrar_cpf(cpf, usuarios):
    filtrar_cpf = []
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            filtrar_cpf.append(usuario)
    return filtrar_cpf[0] if filtrar_cpf else None

def listar_contas(contas): 
    for conta in contas:
        print(f"Agência: {conta["agencia"]}")
        print(f"Conta: {conta["numero_da_conta"]}")
        print(f"Titular da conta: {conta["usuario"]["nome"]}")
    
while True:

    opcao = input(menu)

    if opcao == "1":
        print("""-------- Depósito --------""")
        print(" ")
        valor_deposito = float(input("Digite o valor do depósito? "))
        saldo, extrato = depositar(saldo, extrato, valor_deposito)
        print(" ")
        print("""--------------------------""")
           

    elif opcao == "2":
        print("""--------- Saque ----------""")
        print(" ")
        valor_saque = float(input("Digite o valor do saque? "))
        saldo, extrato = sacar(saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=limite_saques, valor_saque=valor_saque)
        print(" ")
        print("""--------------------------""")
    
 
    elif opcao == "3":
        print("""-------- Extrato ---------""")
        exibir_extrato(saldo, extrato=extrato)
        print(" ")
        print("""--------------------------""")  

    elif opcao == "4":
        print("""--- Cadastrar cliente ----""")
        criar_usuario(usuarios)
        print(" ")
        print("""--------------------------""")

    elif opcao == "5":
        print("""------- Nova conta -------""")
        numero_da_conta = len(contas) + 1
        conta = criar_contas(AGENCIA, numero_da_conta, usuarios, contas)
        print(" ")
        print("""--------------------------""")  
    
    elif opcao == "6":
        print("""----- Lista de contas ----""")
        listar_contas(contas)
        print(" ")
        print("""--------------------------""") 

    elif opcao == "7":
        break 
        
    else:
        print(" ")
        print("Operação inválida, por favor selecione novamente a opção desejada.")