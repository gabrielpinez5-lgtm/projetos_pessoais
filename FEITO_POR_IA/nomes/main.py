import os

def carregar_pessoas():
    # Pega o diretório onde o arquivo main.py está localizado
    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(diretorio_script, 'texto.txt')
    
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            pessoas = []
            for linha in f.readlines():
                linha = linha.strip()
                if linha:  # Ignorar linhas vazias
                    partes = linha.split(',')
                    if len(partes) == 2:
                        pessoas.append(partes)
            return pessoas
    except FileNotFoundError:
        print(f"Arquivo texto.txt não encontrado em: {caminho_arquivo}")
        return []

def exibir_pessoa(id_pessoa):
    pessoas = carregar_pessoas()
    if 0 <= id_pessoa < len(pessoas):
        nome, cpf = pessoas[id_pessoa]
        print(f"\n{'='*40}")
        print(f"ID: {id_pessoa}")
        print(f"Nome: {nome}")
        print(f"CPF: {cpf}")
        print(f"{'='*40}")
        input("Pressione ENTER para voltar ao menu...")
    else:
        print("ID inválido!")
        input("Pressione ENTER para continuar...")

def exibir_todas():
    pessoas = carregar_pessoas()
    if not pessoas:
        print("\nNenhuma pessoa cadastrada!")
        input("Pressione ENTER para continuar...")
        return
    
    print(f"\n{'='*40}")
    print(f"TOTAL DE PESSOAS: {len(pessoas)}")
    print(f"{'='*40}")
    for i, (nome, cpf) in enumerate(pessoas):
        print(f"ID: {i} | Nome: {nome} | CPF: {cpf}")
    print(f"{'='*40}\n")
    input("Pressione ENTER para voltar ao menu...")

def main():
    while True:
        print("\n--- Menu ---")
        print("1. Ver todas as pessoas")
        print("2. Ver pessoa por ID")
        print("3. Sair")
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == '1':
            exibir_todas()
        elif opcao == '2':
            try:
                id_pessoa = int(input("Digite o ID da pessoa: "))
                exibir_pessoa(id_pessoa)
            except ValueError:
                print("Digite um número válido!")
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()