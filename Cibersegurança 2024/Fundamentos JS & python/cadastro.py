#Minha resolução 

# Crie um programa em Python que cadastre pessoas. Ele receberá nome, CPF e endereço.
#Faça uma lista para cada dado (ex: l1 para nome, l2 para CPF).
#Imprima todos os dados juntos.
#Solicite ao usuário se ele quer remover alguma pessoa ou cadastrar uma nova pessoa. 
# Caso sim, adicione ou remova. Caso não, encerre o programa.

# Nome das listas
nomes = []
cpfs = []
enderecos = []

def menu():
    while True:
        print("Menu:")
        print("1. Cadastrar pessoa")
        print("2. Remover pessoa cadastrada")
        print("3. Imprimir lista de cadastro")
        print("4. Encerar")
        
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == '1':
            cadastrar_pessoa()
        elif opcao == '2':
            remover_pessoa()
        elif opcao == '3':
            imprimir_pessoas()
        elif opcao == '4':
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__menu_":
    menu()

def cadastrar_pessoa():
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    endereco = input("Digite o endereço: ")
    
    nomes.append(nome)
    cpfs.append(cpf)
    enderecos.append(endereco)
    print("Pessoa cadastrada com sucesso!\n")

def imprimir_pessoas():
    if len(nomes) == 0:
        print("Nenhuma pessoa cadastrada.\n")
    else:
        print("Lista de Pessoas Cadastradas:")
        for i in range(len(nomes)):
            print(f"{i+1}. Nome: {nomes[i]}, CPF: {cpfs[i]}, Endereço: {enderecos[i]}")
        print()

def remover_pessoa():
    if len(nomes) == 0:
        print("Nenhuma pessoa cadastrada para remover.\n")
    else:
        imprimir_pessoas()
        indice = int(input("Digite o número da pessoa que deseja remover: ")) - 1
        if 0 <= indice < len(nomes):
            nomes.pop(indice)
            cpfs.pop(indice)
            enderecos.pop(indice)
            print("Pessoa removida com sucesso!\n")
        else:
            print("Índice inválido.\n")



    # resolução do instrutor