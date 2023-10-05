#WHILE LOOPS

#EXCELENTES PARA LOOPS DEPENDENTES DE UMA CONDIÇÃO

# CRIAR UMA PROMOÇÃO DE UM PRODUTO NO VALOR DE 100$


valor = 100
dia = 0

while valor > 20:
  dia += 1
  print(f' No dia {dia} o produto sera vendido no valor de R${valor},00 ')
  valor -= 5

"""

#Exercício 3:
#Escreva um programa que solicite ao usuário a entrada de três números inteiros. Em seguida, determine e exiba o maior e o menor número entre os três.


num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))

maior = max(num1, num2, num3)
menor = min(num1, num2, num3)

print(f' O maior numero é o {maior} e o menor numero é o {menor}')

num4 = int(input('Digite o quarto numero: '))
if num4 > 100:
           print('Uau, que tamanho de numero')
else:
        print('Ihh que pititico')

while num4 <= 99:
  num4 = (num4 + 4)
  print(f' Estou fazendo seu numero aumentar, estamos em {num4} cm')





nome = input('Digite o nome da pessoa: ')
dias = int(input('Digite a quantidade de dias em haver: '))

print(nome)

while dias <= 20:
  dias = (dias * 0.10) + dias
  print(f' {nome} possui + de 7 dias no banco de horas, portanto tem direito a {dias} de comissão')



valor = int(input('Digite o valor do seu produto em R$:  '))

while valor > 20:
  valor = (valor * 0.10) + valor
  print(f' O valor final do seu produto sera de R${valor} ')
  break

if valor < 20:
  print(f' O valor está abaixo de 20R$')

nome = input('Para continuar a comprar, digite seu nome: ')

dias = int(input('Digite que dia é hoje: '))

while dias <= 10:
  dias + 1
  print(f' Hoje é dia {dias}')
  break 
  

"""


