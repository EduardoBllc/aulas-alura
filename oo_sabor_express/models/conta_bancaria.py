class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False

    def __str__(self):
        return f'{self.titular} - {self.saldo}'

    def ativar_conta(self):
        self.ativo = True

conta1 = ContaBancaria('João', 200)
conta2 = ContaBancaria('Maria', 400)
print(conta1)
print(conta2)
conta1.ativar_conta()

