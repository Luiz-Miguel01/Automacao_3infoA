#estrutura de condição
#if e else

print("Uma pequena história interativa.")
print("Você encontra uma porta antiga no meio da estrada.")
choice1 = input("Deseja abrir a porta? (abrir / não): ")            .strip().lower()

if choice1 == "abrir":
    print("A porta range e revela um corredor iluminado.")

    choice2 = input("Segue pelo corredor ou volta? (seguir / voltar): ")            .strip().lower()
    if choice2 == "seguir":

        print("Você segue e encontra uma sala com um livro brilhante.")
        choice3 = input("Lê o livro ou guarda para depois? (ler / guardar): ")            .strip().lower()

        if choice3 == "ler":
            print("As palavras do livro mostram mapas de mundos novos. Você decide partir em uma jornada.")

        else:
            print("Você guarda o livro. Às vezes, o mistério vale mais do que a resposta.")

    else:
        print("Você volta para a estrada. O sol está se pondo; talvez amanhã seja dia de aventura.")

else:
    print("Você ignora a porta e continua. O vento conta histórias de quem teve coragem.")
    choice4 = input("Seguir viagem ou descansar sob uma árvore? (seguir / descansar): ")          .strip().lower()

    if choice4 == "seguir":
        print("Caminhando, você encontra novas pessoas e aprende algo sobre si mesmo.")

    else:
        print("Ao descansar, você sonha com portas e corredores. A aventura fica para outro dia.")
#----------------------------------------------------------------------------------------------------------------------------

#entrada
#Variavel + conversão de tiplo (float) + entrada de dados (input)
media = float(input("Digite a média do aluno: "))

#Processamento
if media >= 6:
    print("Aprovado!")


elif media >= 5.9 or media < 0:
    print("Reprovado!")


else:
    print("Coloque uma numero de nota entre 0 e 10!")

