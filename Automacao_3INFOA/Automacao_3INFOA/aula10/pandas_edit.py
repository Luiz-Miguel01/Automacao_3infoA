#Pandas - Biblioteca para manipular dados tabulares. (Planilha)
#Pandas - Semelhante a Banco de Dados - DML

#Manipulação de dados (Inserir, Atualizar, Excluir e Consultar)

#Instalar a lib: pip install pandas

#uso
import pandas as pd

#criar a quadro de dados (DataFrame) equivalente a tabela no DB
#cria a variavel planilha que vai armazenar a planilha do excel
#que foi lida pelo pandas
planilha = pd.read_excel('aula10\\Planilha.xlsx')

#Visualizar a planilha
print(planilha)

#Inserir um registro na planilha
planilha.loc[len(planilha)] = ['Ivan Paulino', 40, 'M', 85, 1.75]
print(planilha)

#Inserir um registro na planilha
planilha.loc[len(planilha)] = ['Izabel', 17, 'F', 78, 1.85]
print(planilha)

#atualizar a linha inteira
planilha.loc[19] = ['Ivan Paulino', 40, 'M', 85, 1.75]
print(planilha)


#Atualizar apenas uma coluna
planilha.loc[19, 'Idade'] = 45
print(planilha)

#atualizar duas ou mais colunas
planilha.loc[19, ['Idade', 'Peso']] = [25, 200]
print(planilha)    

#Remover um registro da planilha
planilha = planilha.drop(19)
#ou
planilha.drop(19, inplace=True)

print("A planilha tem", len(planilha), "linhas.")