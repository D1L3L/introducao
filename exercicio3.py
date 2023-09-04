#ler 2 valored e comparar qual o maior, n podem ser iguais.
valor1 = float(input("Insira o primeiro número: "))
valor2 = float(input("Insira o segundo número: "))
if valor1 == valor2:
    print("Os valores são iguais, tente novamente.")
elif valor1 > valor2:
    print(f"O número {valor1} é maior do que o número {valor2}.")
else:
    print(f"O número {valor2} é maior do que o número {valor1}.")
