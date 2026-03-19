class pon():
    def __init__(self):
        self._soma_pesos = 0
        self._valor_numero = 0.0
        self._valor_peso = 0
        self._maior = float("-inf")
        self._menor = float("inf")
        self._parte_superior = 0.0

    def somar_valor_por_valor(self, valor : float, peso : int):
        self._valor_numero = valor
        self._valor_peso  = peso

        if self._maior < self._valor_numero:
            self._maior = self._valor_numero

        if self._menor > self._valor_numero:
            self._menor = self._valor_numero

        multiplicacao = self._valor_numero * self._valor_peso

        self._soma_pesos += self._valor_peso
        
        self._parte_superior += multiplicacao

    def media_Ponderada(self):
        if self._soma_pesos == 0:
            raise ZeroDivisionError("Insira ao menos um peso!")
        
        print(f"\t\t\t\t\t\t\t\t\tO maior numero é {self._maior} e o menor é {self._menor}")
        return self._parte_superior / self._soma_pesos
    
    def limpar_tela(self):
        self._soma_pesos = 0
        self._valor_numero = 0.0
        self._valor_peso = 0
        self._parte_superior = 0.0