numero = int(input("insira um valor"))
contagem = 0
divisores = []
for i in range(numero):
    contagem += 1
    if numero % contagem ==  0:
        divisores.append(contagem)

print(f"\nseus divisores sao:{divisores}")