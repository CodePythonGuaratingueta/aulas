def soma(a, b):
    return a + b + 10

# op = *, +, /, -
def calculadora(op, a, b):
    if op == '+':
        print(soma(a, b))

while True:
    n1 = int(input("Digite um numero:"))
    op = input("Digite uma operação [*,+,-,/]: ")
    n2 = int(input("Digite outro número: "))
    calculadora(op, n1, n2)