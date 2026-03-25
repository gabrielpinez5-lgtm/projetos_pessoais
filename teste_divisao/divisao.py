import subprocess


#def seletor():
#    print("digite 0 para sair e 1 para descobrir os divisores de um numero")
#    opcao_escolhida = int(input("digite aqui\t"))
#    return opcao_escolhida



def divisao():
    numero = -1
    while numero != 0:
        print("insira um numero  ou digite 0 se desejar sair da repetição\n")
        numero = int(input("insira um valor natural não nulo:\t"))
        if numero != 0:
            if numero > 0:
                subprocess.run('cls', shell=True)
                contagem = 0
                divisores = []
                for i in range(numero):
                    contagem += 1
                    if numero % contagem ==  0:
                        divisores.append(contagem)

                if len(divisores) == 2:
                    print(f"numero primo, seus divisores são 1 e {numero}")
                else:
                    print(f"\nos divisores de {numero} sao:{divisores}")
                input("pressione [enter] para continuar")
            else:
                print("\n\nINSIRA UM NUMERO NATURAL NAO NULO\n\n\n")
    print("\n\nsaindo...")
    print("ate breve!")


#def principal():
#    opcao = -1
#    while opcao != 0:
#        opcao = seletor()
#        if opcao != 0:
#            match opcao:
#                case 1: divisao()
#                case _:
#                    print("digite uma oção valida")
#                    input("pressione [enter] para continuar")

if __name__ == "__main__":
    subprocess.run('cls', shell=True)
#    principal()
    divisao()