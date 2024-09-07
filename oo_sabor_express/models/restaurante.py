from models.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome: str, categoria: str):
        """
        Construtor de Restaurante
        :param nome: Nome do restaurante
        :param categoria: Categoria do restaurante
        """
        self._nome = nome if nome.istitle() else nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        linha_exterior = f'*{'-' * 92}*'

        print(linha_exterior)
        print(f'| {'Nome'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | Status |')
        print(f'|{'-' * 27}|{'-' * 27}|{'-' * 27}|{'-' * 8}|')

        for restaurante in cls.restaurantes:
            print(f'| {restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.avaliacao_media).ljust(25)} | {restaurante.ativo.center(6)} |')

        print(linha_exterior)

    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'

    @property
    def avaliacao_media(self):
        if not self._avaliacoes:
            return 'Sem avaliações'

        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        qtd_notas = len(self._avaliacoes)
        media = round(soma_notas / qtd_notas, 1)
        return media

    def alternar_estados(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        nova_avaliacao = Avaliacao(cliente, nota)
        self._avaliacoes.append(nova_avaliacao)
