#Filter Function
  #MUito utilizadocom listas
  #Aplicar uma função a um Iterable, filtrando os items. (list, tuple, dic etc)


valores = [10, 20, 41, 6126, 64, 23, 1]

def remover20(x):
  return x > 20

print(list(filter(lambda x: x > 20, valores)))


