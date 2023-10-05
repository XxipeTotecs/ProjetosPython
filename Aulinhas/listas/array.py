from array import array

#ARRAY (MATRIZ)
#MELHOR PERFORMANCE PARA LISTAS ACIMA DE 1000 ITENS

letras = ['a', 'b', 'c', 'd']
numeros_i = [1,2,3,4]
numeros_f = [1.2, 2.5, 3.4, 5.2]

print(letras)
print(numeros_i)
print(numeros_f)
print()

letras = array('u', ['a', 'b', 'c', 'd'])
numeros_i = array('i', [1,2,3,4])
numeros_f = array('f', [1.2, 2.5, 3.4, 5.2])



print(letras)
print(numeros_i)
print(numeros_f)

