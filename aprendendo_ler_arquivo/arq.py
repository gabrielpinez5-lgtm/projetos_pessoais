import subprocess

class ARQUIVO():
    def __init__(self) -> None:
        self._soma = 0.0
        self._soma_valor_com_peso = 0.0
        self._soma_peso =0.0
        self._quantos_numero_somados = 0
        self._soma_inversos = 0.0
        self._produto_valores = 1
        self._soma_de_quadrados = 0.0



    def receber_arquivo(self, valor, peso):
        self._soma += valor
        self._soma_inversos += 1 / valor
        self._produto_valores *= valor
        self._soma_peso += peso
        self._soma_valor_com_peso += valor * peso
        self._quantos_numero_somados += 1
        self._soma_de_quadrados += valor ** 2

    def limpar_visor(self):
        subprocess.run('cls', shell=True)
        self._soma = 0.0
        self._soma_valor_com_peso = 0.0
        self._soma_peso =0.0
        self._quantos_numero_somados = 0
        self._soma_inversos = 0.0
        self._produto_valores = 1


    @property

    def media_ponderada(self):
        return self._soma_valor_com_peso / self._soma_peso
    
    @property

    def rmq(self):
        return (self._soma_de_quadrados / self._quantos_numero_somados) ** 0.5
    
    @property

    def media_harmonica(self):
        return self._quantos_numero_somados /  self._soma_inversos
    
    @property
    
    def media_geometrica(self):
        return self._produto_valores ** (1 / self._quantos_numero_somados)