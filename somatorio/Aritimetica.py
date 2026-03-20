import subprocess


class ari():
    def __init__(self):
        self._soma_numeros = 0.0
        self._quantidade_numeros = 0
        self._maior = float("-inf")
        self._menor = float("inf")




    def somar(self, _x : float):
        self._soma_numeros += _x
        self._quantidade_numeros += 1

        if self._maior < _x:
            self._maior = _x
        if self._menor > _x:
            self._menor = _x

    def media_Aritimetica(self):
        if self._quantidade_numeros == 0:
            raise ZeroDivisionError("Você não inseriu nenhum número!")
        
        print(f"\t\t\t\t\t\t\t\t\tO maior numero é {self._maior} e o menor é {self._menor}")
        return self._soma_numeros / self._quantidade_numeros
    
    def limpar_tela(self):
        subprocess.run('cls', shell=True)
        self._soma_numeros = 0.0