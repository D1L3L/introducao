# Solicite ao usuário um número inteiro ou real, e verifique se ele é maior ou menor que 10.
valor = int(input("Digite um valor: "))
if valor > 10:
    print("o valor é maior que 10")
elif valor == 10:
    print("valor = 10")
else:
    print("valor menor que 10")