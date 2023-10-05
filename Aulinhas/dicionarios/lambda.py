# Lambda Function
    # É uma função (pequena) sem nome
    #Pode ter vários argumentos mas somente 1 expressão
    # Muito utilizada dentro de outras funções
    #Código mais 'clean'


#mesma coisa que : 
#   def somar(x):
#      return x + 10

# print(somar(2))

somar10 = lambda x, y: x + y + 23

print(somar10(54, 86))



#lambda dentro de função

def somar(x):
  fun2 = lambda x: x + 54
  return fun2(x) * 4


print(somar(80))