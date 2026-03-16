#Entrada de dados
titulo = input("Digite o título do filme: ")
diarias = int(input("Por quantos dias alugou o filme? "))
tempo = int(input("Por quantas dias ficou com o filme? "))

valor = tempo * 5
multa = 0

if tempo - diarias > 0:
    multa = 15

total = valor + multa

print("O total a pagar é: ", total) 