'''
Altere o código abaixo para que a condição
 que está dentro do else mude de lugar e fique dentro do if,
 mantendo a mesma funcionalidade.

media = float(input("Digite a média do aluno: "))

if media >= 6:
    print("Aprovado!")

elif media > 3:
    print("Em exame final!")

else:
    print("Reprovada!")

'''

media = float(input("Digite a média do aluno: "))

if media <= 10 and media >= 0:

    if media > 6:
     print("Aprovado!")
    
    elif media > 3:
     print("Em exame final!")

    else:
        print("reprovado!")

else:
    print("Coloque uma numero de nota entre 0 e 10!")


''' -----------------------------------------------------------------------------'''

media = float(input("Digite a média do aluno: "))

if media < 6:
    if media > 3:
        print("Em exame final!")
    else:
        print("Reprovado!")

else:
    print("Aprovado!")

