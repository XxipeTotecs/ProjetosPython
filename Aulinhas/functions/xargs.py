#FUNÇÕES


#Varios argumentos xargs


#Criar uma função que soma varios numeros
#criar uma funcao que armazena varias numeros e strings em um parametro
"""
def soma(*numeros):
  resultado = 1 
  for num in numeros:
    resultado *= num
  return resultado


x = soma(2,3,4,5,6,8,7,8,9,4)

print(x)
"""

def agencia(**carro):
  return carro

print(agencia(marca='Gol', cor='Vermelho', motor=2.41, placa='32144214'))