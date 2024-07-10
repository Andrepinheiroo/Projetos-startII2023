decisao = "s"

while decisao == "s":
    n = int(input("Digite um número: "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
    decisao = input("Deseja continuar (s/n)? ")
print("Acabou e largou!")