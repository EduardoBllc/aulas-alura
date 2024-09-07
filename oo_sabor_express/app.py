from models.restaurante import Restaurante

restaurante_lanches = Restaurante('Big Joe', 'Lanches')
restaurante_lanches.receber_avaliacao('José', 2)
restaurante_lanches.receber_avaliacao('Carlos', 4)
restaurante_lanches.receber_avaliacao('Julia', 5)
restaurante_italiano = Restaurante('Trattoria di Mangiare', 'Italiana')
restaurante_americano = Restaurante('InFront', 'SteakHouse')
restaurante_americano.alternar_estados()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()