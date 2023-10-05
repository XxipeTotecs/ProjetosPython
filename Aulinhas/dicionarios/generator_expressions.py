from sys import getsizeof

# Generator Express
  #Uma forma mais rapida para listas, dicionarios, etc
  #menos memoria alocada
  #valores em bytes


numeros = [x * 20 for x in range(100)]
print(list(numeros))
print(type(numeros))
print(getsizeof(numeros))

print('---------------------')

numeros = (x * 20 for x in range(100))
print(list(numeros))
print(type(numeros))
print(getsizeof(numeros))


