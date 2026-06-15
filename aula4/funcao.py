
def nome_funcao(entrada1, entrada2):
    #corpo da funcao
    return "saída da função"

def somar(n1, n2):
    resultado = n1 + n2
    return resultado

def imprimir(texto):
    print(texto)

def lerInteiro():
    return int(input())



imprimir('Digite um número 1: ')
n1 = lerInteiro()

imprimir('Digite um número 2: ')
n2 = lerInteiro()

r = somar(n1, n2)

imprimir(r)