class Pessoa:
    def __init__(self, nome, idade, profissao):
        self._nome = nome.title()
        self._idade = idade
        self._profissao = profissao.title()

    def __str__(self):
        return f'{self._nome} | {self._idade}'

    def aniversario(self):
        self._idade += 1

    def saudacao(self):
        print(f'Olá! Me chamo {self._nome}, tenho {self._idade} e sou {self._profissao}')