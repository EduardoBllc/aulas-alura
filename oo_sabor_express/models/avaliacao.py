class Avaliacao:
    def __init__(self, cliente, nota):
        self._cliente = cliente

        assert 5 >= nota >= 0, 'A nota deve ser de 0 a 5'
        self._nota = nota