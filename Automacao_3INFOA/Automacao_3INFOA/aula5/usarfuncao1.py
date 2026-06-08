import funcao

#Como usar essas funções
funcao.imprimir('digite um número 1: ')
n1 = funcao.lerInteiro()

funcao.imprimir('digite um número 2: ')
n2 = funcao.lerInteiro()

r = funcao.somar(n1, n2)

'\n'
funcao.imprimir(f"o valor da soma de {n1} e {n2} é: {r}")
'\n'