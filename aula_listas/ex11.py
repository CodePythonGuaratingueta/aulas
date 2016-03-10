notas = []
for i in range(4):
  notas.append(float(input("Digite a nota: ")))

soma = 0
for i in notas:
  soma = soma + i
  print("Nota: ", i)


print("média: ", soma / 4)
