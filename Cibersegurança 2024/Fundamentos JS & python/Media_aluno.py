# Dicionário: Crie um dicionário para armazenar o nome e a nota 
# de 3 alunos, fazendo a leitura dos valores por meio de uma 
# estrutura de repetição. Depois, crie uma nova estrutura de 
# repetição para somar todas as notas e retornar a média.

alunos = {}

for i in range(1, 4):
    nome = input("Digite o nome: ")
    nota = float(input("Digite a nota: "))
    alunos[nome] = nota

print()
print(alunos)
print()

soma = sum(alunos.values())
# cont = 0
# for nota in alunos.values():
#     soma += nota
#     cont += 1
print(f"Média = {soma/len(alunos)}")