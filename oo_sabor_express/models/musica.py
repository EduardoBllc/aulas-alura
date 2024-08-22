

class Musica:

    def __init__(self,
                 nome: str,
                 artista: str,
                 album: str,
                 duracao: int,
                 categoria: str):
        """
        :param nome: Nome da música
        :type nome: str
        :param artista: Autor/compositor/banda da música
        :type artista: str
        :param album: Album da música
        :type album: str
        :param duracao: Duração da música em segundos
        :type duracao: int
        :param categoria: Categoria da música
        :type categoria: str
        """
        self.nome = nome
        self.artista = artista
        self.album = album
        self.duracao = duracao
        self.categoria = categoria

    def __str__(self):
        return f'{self.nome} de {self.artista}, álbum {self.album}'
