import random
import time

def teste():
    s = 'y'
    while s != 'sair':
        s = str(input("digite [sair] para sair, caso contrario, pressione [enter]"))
        if s != 'sair':
            maria = 0
            gabriel = 0
            ricardo = 0
            n = int(input("selecione o numero de valores da lista:"))
            for i in range(n):
                lista = ['gabriel', 'ricardo', 'maria']
                randomizar = random.choice(lista)
                if randomizar == 'gabriel':
                    gabriel = gabriel + 1
                if randomizar == 'maria':
                    maria = maria + 1
                if randomizar == 'ricardo':
                    ricardo = ricardo + 1
                else:
                    pass
                print(f"\t\n{randomizar}")
                time.sleep(0.001)

            print(f"gabriel é igual a {gabriel}")
            print(f"maria é igual a {maria}")
            print(f"ricardo é igual a {ricardo}")
            print(f"gabriel é {gabriel / n * 100}% da lista")
            print(f"maria é {maria / n * 100}% da lista")
            print(f"ricardo é {ricardo / n * 100}% da lista")


teste()