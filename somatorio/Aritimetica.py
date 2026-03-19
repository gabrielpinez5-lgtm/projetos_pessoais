import subprocess


class ari():
    def __init__(self):
        self._soma_numeros = 0.0
        self._quantidade_numeros = 0
        self.maior = float("-inf")
        self.menor = float("inf")




    def somar(self, _x : float):
        self._soma_numeros += _x
        self._quantidade_numeros += 1

        if self.maior < _x:
            self.maior = _x
        if self.menor > _x:
            self.menor = _x

    def media_Aritimetica(self):
        if self._quantidade_numeros == 0:
            raise ZeroDivisionError("Você não inseriu nenhum número!")
        return self._soma_numeros / self._quantidade_numeros
    
    def limpar_tela(self):
        subprocess.run('cls', shell=True)
        self._soma_numeros = 0.0