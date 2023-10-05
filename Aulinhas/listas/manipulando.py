#Manipulando listas, sempre inicia com colchete e fica armazenado como index 1, 2 ,3 ,,,



cidades = ['passos', 'itau', 'gloria', 'jacui']

cidades[0] = 'manaus'                              #troquei passos por manaus
cidades.append('passos')                           #passei o passos para o final
cidades.pop(1)                                     #remove o itau
cidades.insert(1, 'paraiso')                       #adiciona no index 1 o paraiso
cidades.sort()                                     #coloca em ordem alfabetica

print(cidades)