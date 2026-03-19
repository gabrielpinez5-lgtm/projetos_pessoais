from program import jogo as j
import time
def seletor():

    j.limpar_visor()
    print("Vamos jogar pedra, papel e tesoura!!")
    time.sleep(2)
    j.limpar_visor()
    print("selecione uma das opções")
    time.sleep(0.5)
    print("--------- --- --- ------")
    time.sleep(0.5)
    print("<sair> sair do programa")
    time.sleep(0.5)
    print("<pedra> seleciona a pedra")
    time.sleep(0.5)
    print("<papel> seleciona papel")
    time.sleep(0.5)
    print("<tesoura> seleciona tesoura\n")
    time.sleep(0.5)
    return str(input("DIGITE SUA OPÇÃO [SEM <>]:\t"))

def sair():
    j.limpar_visor()
    print("tem certeza que quer sair :/, fica mais um pouquinho por favor...")
    time.sleep(2)
    j.limpar_visor()
    print("selecione sua opção")
    time.sleep(0.5)
    print("--------- --- -----")
    time.sleep(0.5)
    print("<SAIR AGORA> digite isso para sair do programa")
    time.sleep(0.5)
    print("<ficar> digite isso pra ficar :)")
    time.sleep(0.5)
    return str(input("\nDigite aqui:\t"))


def rodar():
    valor_do_pc = j.valor_pc()
    j.limpar_visor()
    j.resultado(valor_do_pc)

def principal():
    quer_sair = False
    while not quer_sair:
        opcao = seletor()
        match opcao:
            case 'sair':
                confirm = sair()
                if confirm == 'SAIR AGORA':
                    quer_sair = True
            case 'pedra':
                j('pedra')
                rodar()
            case 'papel':
                j('papel')
                rodar()
            case 'tesoura':
                j('tesoura')
                rodar()

if __name__ == "__main__":
    principal()