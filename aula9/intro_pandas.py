import pandas

#Pandas biblioteca para manipular dados tabulares.
#No Pandas uma planilha/tabela é chamada de DataFrame (Quadro de Dados)
#Um DataFrame é formado por um conjunto de Series (Colunas)

#Vamos ler uma planilha do Excel e criar um DataFrame
df = pandas.read_excel("aula9\\Planilha.xlsx")

#Imprime a planilha Inteira
print(df)
#Imprime a linha que possui o indice 10
print(df.loc[10])
#Imprime apenas o valor que está na Linha 10 - Coluna Nome
print(df.loc[10, "Nome"])

#Imprime apenas os valores que estão na Linha 10 nas Colunas:  
# Nome e Peso
print(df.loc[10, ["Nome", "Peso"]])

print(df.loc[:, "Nome"])

#Atualiza uma celula da tabela
df.loc[10, "Nome"] = "Outro Nome"

print(df)


