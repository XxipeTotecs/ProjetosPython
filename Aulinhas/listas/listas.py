#Manipulando listas, sempre inicia com colchete e fica armazenado como index 1, 2 ,3 ,,,


loja = ['cadastro', 'nome', 'usuario']

print(loja)

cidades = ['passos', 'itau', 'gloria', 'jacui']

cidades[0] = 'manaus'

print(cidades)

numeros = [2, 3, 4, 1, 5]
letras = ['s', 's', 'k']

numeros + letras
#mesma coisa que 
numeros.extend(letras)
print(numeros)

#separando as listas

numeros = [1,2,3,3,2,1]
print(numeros[2])

itens =[['item1', 'item2'], ['item3', 'item4']]

print(itens[0][1])


#Loops dentro de listas

valors = [1, 4, 414, 232, 131, 34, 51]

for x in valores:
  print(f'O valor final do produto é de R${x}.')

print(x)