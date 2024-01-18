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

while True:

    opcao = input(menu)

    if opcao == "1":
        print("""-------- Depósito --------""")
        print(" ")
        print("Qual o valor do depósito?")
        deposito = float(input())
        if deposito > 0:
           print(" ")
           print("Depósito realizado com sucesso!")
           saldo += deposito
           print(" ")
           extrato += f"""Depósito: R$ {deposito: .2f} \n"""
        else:
           print("Valor inválido!")
        print(" ")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print(" ")
        print("""--------------------------""")

    elif opcao == "2":
        print("""-------- Saque --------""")
        print(" ")
        print("Qual o valor do saque?")
        saque = float(input())
        if numero_saques < limite_saques:
            if saque <= limite:
                if saque <= saldo:
                    print(" ")
                    print("Saque realizado com sucesso!")
                    saldo -= saque
                    extrato += f"""Saque: R$ -{saque: .2f}\n"""
                else: 
                    print(" ")
                    print("Não será possível sacar o dinheiro por falta de saldo.")
            else:
                print("Valor do saque excede o limite disponível para saque. Valor disponível parab saque di: R$ 500.00")
        else:
            print(" ")
            print("Excedido a quantidade de saque. ")
        numero_saques += 1
        print(" ")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print(" ")
        print("""--------------------------""")
    elif opcao == "3":
        print("extrato")
        