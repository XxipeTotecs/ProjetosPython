#Map Function
  #Muito utilizado com listas
  #Aplicar uma função a um Iterable, por imte. (List, tuples,dicionarios, etc)

lista1 = [1, 2, 3, 4]

def multi(x):
  return x * 2


lista2 = map(multi, lista1)

print(list(lista2))

#Lambda em map

# lista3 = map(lambda x: x *5, lista1)
print(list(map(lambda x: x * 5, lista1)))   # economiza linhas de codigos


