import random
import subprocess
class jogo():
    def __init__(self, pessoa):
        self.pessoa = pessoa

    def valor_pc(self):
        list = ['pedra', 'papel', 'tesoura']
        return random.choice(list)

    def resultado(self, entrada):
        if self.pc == self.pessoa:
            print("draw!")
        elif entrada == 'pedra' and self.pessoa == 'papel':
            print("Vitoria das pessoas!")
        elif entrada == 'pedra' and self.pessoa == 'tesoura':
            print("Vitoria dos robôs!")
        elif entrada == 'papel' and self.pessoa == 'tesoura':
            print("Vitoria das pessoas!")
        elif entrada == 'papel' and self.pessoa == 'pedra':
            print("Vitoria dos robôs!")
        elif entrada == 'tesoura' and self.pessoa == 'pedra':
            print("Vitoria das pessoas!")
        elif entrada == 'tesoura' and self.pessoa == 'papel':
            print("Vitoria dos robôs!")
        else:
            print("erro")

    def limpar_visor():
        subprocess.run('cls', shell=True)
    