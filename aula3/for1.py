#Estrutura de repetição For
#Utilizada para repetir um conjunto de instruções por
#um número determinado de vezes (conhecido)

#range -> Comando utilizado para criar intervalos númericos
#exemplo


# (o último valor não entra no conjunto)





#range(5) -> cria o intervalo númerico: 0, 1, 2, 3, 4 
for valor in range(5):
    print(valor, end=" ") 
print("\n")

#range(valor inicial, valor final, passo)
#range(1, 5, 1) -> 1, 2, 3, 4
for valor in range(1, 5, 1):
    print(valor, end=" ") 
print("\n")

#range(valor inicial, valor final, passo)
#range(4, 9, 2) -> 4, 6, 8 
for valor in range(4, 9, 2):
    print(valor, end=" ") 
print("\n")

#range(5, 0 ,-1) -> (5, 4, 3, 2, 1)
for valor in range(5, 0, -1):
    print(valor, end=" ") 
print("\n")