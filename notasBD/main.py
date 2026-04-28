import pyodbc as db, getpass4 as gp, os
import platform

conexao = None

sistema = "cls" if platform.system() == "Windows" else "clear"

def seletor():
    opcao = -1
    while opcao != 0:
        os.system(sistema)
        print("Selecione uma opção:")
        print("========= === ======")
        print("0. sair")
        print("1. conectar ao banco")
        print("2. adicionar nota")
        print("3. visualizar notas")
        opcao = int(input("Opção: "))
        match opcao:
            case 1: 
                try:
                    conectar_ao_banco()
                except:
                    print("nao foi possivel conectar ao banco!")
            case 2:
                selecionar_materia()
            case 3:
                visualizar_notas()
            case _:
                print("Opção inválida. Tente novamente.")
            

def conectar_ao_banco():
    global conexao
    os.system(sistema)
    banco_nome = input("insira o nome do banco:  ")
    usuario = input("insira seu username: ")
    senha = gp.getpass("insira sua senha: ")
    try:
        conexao = db.connect(driver="{SQL Server}",
                            server="regulus.cotuca.unicamp.br",
                            database=f"{banco_nome}",
                            user=f"{usuario}", 
                            password=f"{senha}")

        print("Conectado ao banco de dados!")
    except Exception as e:
        print("Erro ao conectar ao banco de dados:", e)
        conexao = None
    input("tecle [enter] para continuar")



def desconectar_do_banco():
    global conexao
    os.system(sistema)
    if conexao:
        conexao.close()
        print("Desconectado do banco de dados.")
    else:
        print("Nenhuma conexão ativa para desconectar.")




if __name__ == "__main__":
    seletor()
    desconectar_do_banco()