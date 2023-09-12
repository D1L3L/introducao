#faça um programa que mostre as tabuadas dos números de 1 a 10
mult = int(input("Digite um valor para saber a tabuada dele: "))
contador = 0
while contador < 10:
    contador += 1
    print ( f" {contador} x {mult} = {contador * mult}")
