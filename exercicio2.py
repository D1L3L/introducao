#Ler notas 1 e 2
nota1 = float(input("Insira a primeira nota do aluno: "))
nota2 = float(input("Insira a segundaa nota do aluno: "))
media = (nota1 + nota2)/2
if media >= 7:
    print("Parabéns, o aluno foi aprovado com média",media)
else:
    print("Que pena o aluno teve de média", media)
