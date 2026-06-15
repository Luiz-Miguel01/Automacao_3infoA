'''
1) Considere que a tabela abaixo representa uma planilha do Excel 
chamada estudantes.xlsx. Crie o código para importar a biblioteca 
pandas e para ler a planilha do Excel para um DataFrame 
chamado tabela.
'''

import pandas as pd
tabela = pd.read_excel("aula11\\dados.xlsx", sheet_name="alunos")

'''
2) Crie o código para exibir os 5 primeiros registros do DataFrame.
'''
print(tabela.head(5))

'''
3) Crie o código para Inserir um novo aluno no DataFrame com os seguintes dados:
● RA: 0008
● Nome: Enzo Moreira
● Curso: Técnico em Jogos
● Turma: 1GMA
'''
tabela.loc[len(tabela)] = [8, 'Enzo Moreira', 'Técnico em Jogos', '1GMA']
print(tabela)

'''
4) Crie o código para atualizar os dados do estudante Enzo Moreira para:
● Curso: Técnico em Informática
● Turma: 3TE
'''
tabela.loc[tabela['Nome'] == 'Enzo Moreira',['Curso', 'Turma']] = ['Técnico em Informática', '3TE']
print(tabela)

'''
5) Crie o código para excluir o estudante que está na linha de índice 1 do
DataFrame.
'''
#Apaga a linha 1
tabela.drop(1, inplace=True)
print(tabela)

#Apaga a Coluna Nome
#tabela.drop(columns="Nome", inplace=True)
#print(tabela)

'''
7) Exibir apenas os alunos matriculados no curso "Técnico em Informática".
'''
resultado = tabela.loc[tabela['Curso'] == 'Técnico em Informática']
print(resultado)

#7a) Mostrar os alunos que são do 1INFOA
resultado = tabela.loc[tabela['Turma'] == '1INFOA']
print(resultado)

#5a) Remover pelo RA, primeiro faz consulta, depois pega o index do
#resultado para fazer a exclusão com drop
#resultado = tabela.loc[tabela['RA'] == 5]
#tabela.drop(resultado.index, inplace=True)
print(tabela)

print("\n \n \n \n")

#8) Classificar os registros em ordem alfabetica
#sort - tradução => classificar
#ascending -> ascender - ascensão - do Menor para o Maior
classificados = tabela.sort_values('Nome', ascending=False)
print(classificados)

#Agrupamento - agrupar e contar
#Conte quantos estudantes existe por curso
#posso usar também (max, min, mean, sum, count)
resp = tabela.groupby('Curso').count()
print(resp)

#semelhante a agrupar e contar
resp = tabela.value_counts("Turma")
print(resp)

'''
6) Exportar o DataFrame atualizado para uma nova planilha do Excel.
'''
classificados.to_excel("aula11\\classificados.xlsx")
