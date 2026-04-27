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


#Como usar essas funções
imprimir('digite um número 1: ')
n1 = lerInteiro()

imprimir('digite um número 2: ')
n2 = lerInteiro()

r = somar(n1, n2)

'\n'
imprimir(f"o valor da soma de {n1} e {n2} é: {r}")
'\n'