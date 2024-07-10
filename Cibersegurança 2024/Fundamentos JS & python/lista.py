n = int(input("Quantos produtos deseja cadastrar? "))

nome_produto = []
preco_produto = []

for i in range(0, n):
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto (R$): "))

    nome_produto.append(nome)
    preco_produto.append(preco)

for j in range(0, n):
    print(f"Nome: {nome_produto[j]} e Preço: R$ {preco_produto[j]}")