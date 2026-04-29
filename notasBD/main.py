import pyodbc as db, getpass4 as gp, os
import platform

conexao = None


def limpar_tela():
    sistema = "cls" if platform.system() == "Windows" else "clear"
    os.system(sistema)

def seletor():
    conexao_foi_feita = False
    opcao = -1
    while opcao != 0:
        limpar_tela()
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
                    conexao_foi_feita = conectar_ao_banco()
                except:
                    print("nao foi possivel conectar ao banco!")
            case 2:
                if conexao_foi_feita:
                    selecionar_materia()
                else:
                    print("conecte-se ao banco de dados primeiro!")
                    input("tecle [enter] para continuar")
            case 3:
                if conexao_foi_feita:
                    visualizar_notas()
                else:
                    print("conecte-se ao banco de dados primeiro!")
                    input("tecle [enter] para continuar")
            case _:
                print("Opção inválida. Tente novamente.")
            


def selecionar_materia():
    
    limpar_tela()
    
    
    print("digite qual materia deseja alterar a nota")
    print("====== ==== ======= ====== ======= = ====")
    print("mat_p1")
    print("mat_p2")
    print("geo_p1")
    print("geo_p2")
    print("bio_p1")
    print("bio_p2")
    print("edf_p1")
    print("edf_p2")
    print("fis_p1")
    print("fis_p2")
    print("his_p1")
    print("his_p2")
    print("ing_p1")
    print("ing_p2")
    print("pt_p1")
    print("pt_p2")
    print("qui_p1")
    print("qui_p2")
    print("tp_p1")
    print("tp_p2")
    print("bd_p1")
    print("bd_p2")
    print("desint_p1")
    print("desint_p2")
    print("projog_p1")
    print("projog_p2")
    print("praticas_p1")
    print("praticas_p2")
    print("filosoc_p1")
    print("filosoc_p2")

    materia = str(input("materia: "))
    nota = float(input("nota: "))
    bimestre = int(input("bimestre: "))


    if bimestre <= 4 and bimestre >= 1 and nota >= 0 and nota <= 10 and materia in ["mat_p1", "mat_p2", "geo_p1", "geo_p2", "bio_p1", "bio_p2", "edf_p1", "edf_p2", "fis_p1", "fis_p2", "his_p1", "his_p2", "ing_p1", "ing_p2", "pt_p1", "pt_p2", "qui_p1", "qui_p2", "tp_p1", "tp_p2", "bd_p1", "bd_p2", "desint_p1", "desint_p2", "projog_p1", "projog_p2", "praticas_p1", "praticas_p2", "filosoc_p1", "filosoc_p2"]:
        
        cursor = conexao.cursor()
        
        cursor.execute(f"UPDATE notas SET {materia} = {nota} WHERE bimestre = {bimestre}")
        
        conexao.commit()
        



def conectar_ao_banco():
    global conexao
    limpar_tela()
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
        return True
    except Exception as e:
        print("Erro ao conectar ao banco de dados:", e)
        conexao = None
        return False
    input("tecle [enter] para continuar")



def desconectar_do_banco():
    global conexao
    limpar_tela()
    if conexao:
        conexao.close()
        print("Desconectado do banco de dados.")
    else:
        print("Nenhuma conexão ativa para desconectar.")




if __name__ == "__main__":
    seletor()
    desconectar_do_banco()