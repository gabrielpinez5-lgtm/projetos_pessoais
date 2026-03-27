def principal():
    arquivo = str(input("Insira o caminho do arquivo.txt a ser lido:\n\n"))
    arquivo = open(arquivo)
    linha = arquivo.readline()
    while linha != "":
        pass

if __name__ == "__main__":
    principal()