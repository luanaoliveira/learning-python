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
        print("saque")
    elif opcao == "3":
        print("extrato")
        