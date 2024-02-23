class Client:
    def __init__(self, address, accounts):
        self._address = address
        self._accounts = []

    def realizar_transacao(self):
        self.account = account
        self.transaction = Transaction
    
    def add_account(self):
        self.account = account

class PhysicalPerson(Client):
    def __init__(self, cpf=str, name=str, date_of_birth=str):
        self.cpf = cpf
        self.name = name
        self._date_of_birth = date_of_birth

        super().__init__(address=str, accounts=list)

# Interface
class Transaction():
    def register(self):
        self.account = account

class deposit(Transaction):
    def __init__(self, value=float):
        self.value = value

class withdraw(Transaction):
    def __init__(self, value=float):
        self.value = value

class account:
    def __init__(self, balance=float, number=int, agency=str):
        self._balance = balance
        self._number = number,
        self._agency = agency
        self._client = Client
        self._historic = Historic

    def balance(self):
        # Não recebe argumento e retorna float
        if self.balance:
            return f"{self.balance}"

    def nova_account(self, number=int):
        self.client = Client
        self.number = number #Number da account
        # Método de fábrica - retorna o objeto account

    def to_withdraw(self, value=float):
        # Recebe um value float e retorna booleano
        if value <= self.balance:
            print("Saque realizado com sucesso!")
            self.balance -= value
            return True
        else: 
            print("Não será possível realizar o saque o dinheiro por falta de saldo.")
            return False    

    def deposit(self, value=float):
        # # Recebe um value float e retorna booleano
        if value > 0:
            print("Depósito realizado com sucesso!")
            self.balance += value
            return True
        else:
            print("Valor inválido!")
            return False
    
class accountCorrente(account):
    def __init__(self, limit=float, withdrawal_limit=int):
        self.limit = limit
        self.withdrawal_limit = withdrawal_limit
        super().__init__(balance=float, number=int, agency=str)
    # Tem todos os atributos que a account tem, mais limit e limits_saques

class Historic():
    # def adicionar_transaction(transaction=Transaction):
        pass