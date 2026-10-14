

n = int(input("Digite o numero de linhas: "))

for i in range(n):
    numero = 1
    print(" " * (n - i), end="")

    for j in range(i + 1):
        print(numero, end=" ")
        numero = numero * (i - j) // (j + 1)

    print()
