def verificaNumero(x):
    if x > 0:
        return "P"
    return "N"

for i in range(10):
    print(i)
print("fim")
numero = int(input("Digite um numero: "))
print(verificaNumero(numero))