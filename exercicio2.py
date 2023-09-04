#Ler notas 1 e 2
nota1 = float(input("Insira a primeira nota do aluno: "))
nota2 = float(input("Insira a segundaa nota do aluno: "))
media = (nota1 + nota2)/2
if 10 >= media >= 6:
    print(f"Parabéns, o aluno foi aprovado com média {media}")
elif 0 > media > 10:
    print("Acho que você digitou algum valor errado, digite nnovamente")
else:
    print(f"Que pena o aluno teve de média {media}")
