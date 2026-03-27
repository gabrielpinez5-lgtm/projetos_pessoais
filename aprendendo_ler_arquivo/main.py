from arq import ARQUIVO
import subprocess 


def principal():
    leitura = ARQUIVO()
    arquivo = str(input("Insira o caminho do arquivo.txt a ser lido:\n\n"))
    arquivo = open(arquivo)
    linha = "-"
    
    while linha != "":
        linha = arquivo.readline()
        if linha != "":
            valor_str, peso_str = linha.strip().split(';')
            valor_float = float(valor_str)
            peso_float = float(peso_str)
            leitura.receber_arquivo(valor_float, peso_float)
    subprocess.run('cls', shell=True)
    print(f"a media ponderada é aproximadamente {leitura.media_ponderada}")
    print(f"a media harmonica é aproximadamente {leitura.media_harmonica}")
    print(f"a media geometrica é aproximadamente {leitura.media_geometrica}")
    print(f"a raiz media quadratica é aproximadamente {leitura.rmq}")
    input("pressione [enter] para continuar!")
    



if __name__ == "__main__":
    principal()