

import pyodbc as db, getpass4 as gp, os, platform, time

conexao = None

def limpar_tela():
    
    # sistema = "cls" if platform.system() == "Windows" else "clear"
    # os.system(sistema)
    print("\033[H\033[J", end="") # metodo do gemini para limpar a 'tela' do terminal, funciona em qualquer sistema operacional e é mais rapido que o metodo tradicional

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
    print("mat")
    print("geo")
    print("bio")
    print("edf")
    print("fis")
    print("his")
    print("ing")
    print("pt")
    print("qui")
    print("tp")
    print("bd")
    print("desint")
    print("projog")
    print("praticas")
    print("filosoc")
    

    materia = str(input("materia: "))
    bimestre = int(input("bimestre: "))
    nota_p1 = float(input("nota([enter] se não deseja inserir nota): "))
    nota_p2 = float(input("nota([enter] se não deseja inserir nota): "))


    if (bimestre >= 1 and bimestre <= 4) and (nota_p1 >= 0 and nota_p1 <= 10 or nota_p1 == None) and (nota_p2 >= 0 and nota_p2 <= 10 or nota_p2 == None) and materia in ["mat", "geo", "bio", "edf", "fis", "his", "ing", "pt", "qui", "tp", "bd", "desint", "projog", "praticas", "filosoc"]:
        
        try:
            adicionar_nota(materia, nota_p1, nota_p2, bimestre)
            print("\033[32m[✓] Nota adicionada com sucesso!\033[0m")
            time.sleep(1.5)
        except Exception as e:
            print("\033[31m[!] Erro ao adicionar nota\033[0m")
            time.sleep(1.5)
    else:
        print("\033[31m[!] Dados inválidos, tente novamente!\033[0m")
        time.sleep(1.5)
        
def adicionar_nota(materia, nota_1,nota_2, bimestre):
    global conexao
    cursor = conexao.cursor()
    if nota_1 != None:
        cursor.execute(f"UPDATE nota_bruta SET {materia} = {nota_1} WHERE bimestre = {bimestre}")
        conexao.commit()
        cursor.close()
    if nota_2 != None:
        cursor.execute(f"UPDATE nota_bruta SET {materia} = {nota_2} WHERE bimestre = {bimestre}")
        conexao.commit()
        cursor.close()
    
def visualizar_notas():
    try:
        global conexao
        cursor = conexao.cursor()
        tabela = cursor.execute("SELECT * FROM nota_bruta").fetchall()

#todo o codigio abaixo é feito por ia, devo testar e revisar para ver se funciona,
#  mas a ideia é pegar os nomes das colunas da tabela e printar eles em formato de tabela,
#  depois printar os dados da tabela em formato de tabela,
#  tudo isso usando o cursor.description para pegar os nomes das colunas e
#  o fetchall para pegar os dados da tabela, e depois fechar o cursor, caso haja algum erro,
#  printar uma mensagem de erro e esperar 1.5 segundos antes de continuar
####################
        columns = [column[0] for column in cursor.description] 
        print(" | ".join(columns)) 
        print(" | ".join(["=" * len(col) for col in columns])) 
        for row in tabela: #
            print(" | ".join(str(item) for item in row)) 
        cursor.close() 
    except Exception: 
        print("\033[31m[!] Erro ao buscar notas\033[0m") 
        time.sleep(1.5) 
######################

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

        # \033[32m deixa o texto verde
        print("\033[32m[✓] Conexão feita com sucesso!\033[0m")
        time.sleep(1.5)
        return True
    except Exception as e:
        print("\033[31m[!] Não foi possível conectar\033[0m")
        time.sleep(1.5)
        conexao = None
        return False



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