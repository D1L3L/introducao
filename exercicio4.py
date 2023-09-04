
valor1 = float(input("Insira o primeiro número: "))
valor2 = float(input("Insira o segundo número: "))
if valor1 == valor2:
    print("Os valores são iguais, tente novamente.")
elif valor1 > valor2:
    print(f"A ordem crescente é {valor2} e {valor1}.")
else:
    print(f"A ordem crescente é {valor1} e {valor2}.")