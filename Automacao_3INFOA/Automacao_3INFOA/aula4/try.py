'''
Crie um script que solicita que o usuário digite dois números 
inteiro. Após o programa deve realizar a divisão do primeiro
número pelo segundo número. Por fim, deve mostrar o resultado
da divisão
'''
while True:
     try:    
        numero1= int(input(f"Digite o primeiro número: "))
        numero2= int(input(f"Digite o segundo número: "))
        resultado = (numero1 / numero2)
        print("O resultado da divisão é: ",resultado)
        break
     except ValueError:
        print("O valor digitado é inválido, digite novamente: ")
     except ZeroDivisionError:
         print("Não é possível dividir por 0. Tente novamente: ")
     except Exception as bolinha:
         print("Ocorreu um erro: ",)