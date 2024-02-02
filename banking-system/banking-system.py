menu = """

1 - Depositar
2 - Sacar
3 - Extrato
4 - Sair

"""

print(menu)

saldo = 0
limite = 500
extrato = " "
numero_saques = 0
limite_saques = 3

def depositar(saldo, extrato, valor_deposito):
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
        print("Excedido a quantidade de saque. ")
    numero_saques += 1
    print(" ")
    print(f"Saldo atual: R$ {saldo:.2f}")
    return saldo, extrato

def exibir_extrato(saldo, / , * , extrato):
    if extrato:
        print(extrato)
    else:
        print(" ")
        print("Não foram realizadas movimentações.")
    print(f"Saldo atual: R$ {saldo:.2f}")
    return saldo, extrato

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
        print("""-------- Saque --------""")
        print(" ")
        valor_saque = float(input("Digite o valor do saque? "))
        saldo, extrato = sacar(saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=limite_saques, valor_saque=valor_saque)
        print(" ")
        print("""--------------------------""")
    
 
    elif opcao == "3":
        print("""-------- Extrato --------""")
        saldo, extrato = exibir_extrato(saldo, extrato=extrato)
        print(" ")
        print("""--------------------------""")
        
    elif opcao == "4":
        break
    else:
        print(" ")
        print("Operação inválida, por favor selecione novamente a opção desejada.")