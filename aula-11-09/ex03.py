#Desenvolva um programa que verifique e mostre os números entre 1000 e 2000, que quando divididos por 11, produzam o resto igual a 5.
from time import sleep
for numero in range (1000, 2001):
    sleep (0.00005)
    if (numero % 11) == 5:
        print (f"O múmero é {numero}")