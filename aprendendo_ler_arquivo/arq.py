class ARQUIVO():
    def __init__(self) -> None:
        self._soma = 0.0
        self._soma_valor_com_peso = 0.0
        self._soma_peso =0.0
        self._quantos_numero_somados = 0



    def receber_arquivo(self, valor, peso):
        self._soma += valor
        self._soma_peso += peso
        self._soma_valor_com_peso = valor * peso
        self._quantos_numero_somados += 1

    def media_ponderada(self):
        pass