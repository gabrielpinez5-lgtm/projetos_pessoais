from Aritimetica import ari as a
from Ponderada import pon as p
import time
import subprocess

def seletor():
    print("\t\t\t\t\t\t\t\t\tcalculadora de media")
    print("\t\t\t\t\t\t\t\t\t=========== == ===== ")
    print("\t\t\t\t\t\t\t\t\t0- sair")
    print("\t\t\t\t\t\t\t\t\t1- media aritimetica")
    print("\t\t\t\t\t\t\t\t\t2- media ponderada")
    print("\t\t\t\t\t\t\t\t\t3- media harmonica")
    opcao = int(input("\t\t\t\t\t\t\t\t\tInsira sua escolha!"))
    return opcao



def aritimetica():
    subprocess.run('cls', shell=True)
    soma = a()
    x = int(input("\t\t\t\t\t\t\t\t\tquantos valores você vai adicionar?\t"))
    numero = 0
    for i in range(x):
        numero += 1
        num = float(input(f"\t\t\t\t\t\t\t\t\tInsira o {numero}° numero:"))
        soma.somar(num)
    media_aritimetica = soma.media_Aritimetica()
    print(f"\t\t\t\t\t\t\t\t\to valor da media aritimetica é {media_aritimetica}")
    input("\t\t\t\t\t\t\t\t\tpressione [enter] para continuar")
    soma.limpar_tela()



def ponderada():
    subprocess.run('cls', shell=True)
    pon = p()
    y = int(input("\t\t\t\t\t\t\t\t\tquantos valores você vai adicionar?\t"))
    subprocess.run('cls', shell=True)
    numero = 0
    for i in range(y):
        numero += 1
        num = float(input(f"\t\t\t\t\t\t\t\t\tInsira o {numero}° numero:"))
        peso = int(input("\t\t\t\t\t\t\t\t\tinsira seu respectivo peso:"))
        subprocess.run('cls', shell=True)
        pon.somar_valor_por_valor(num, peso)
    media_ponderada = pon.media_Ponderada()
    print(f"\t\t\t\t\t\t\t\t\to valor da media aritimetica é {media_ponderada}")
    input("\t\t\t\t\t\t\t\t\tpressione [enter] para continuar")
    subprocess.run('cls', shell=True)



def principal():
    opcao_escolhida = 1111111111111
    while opcao_escolhida != 0:
        opcao_escolhida = seletor()
        if opcao_escolhida != 0:
            match opcao_escolhida:
                case 1: aritimetica()
                case 2: ponderada()


if __name__ == "__main__":
    subprocess.run('cls', shell=True)
    principal()
    print("desligando programa!")
    print("Até breve!")