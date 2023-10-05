#unpacking lists
#armazenar mais de uma informação em variavies
#manter a sequencia dos dados em uma variavel

produtos = ['arroz', 'feijao', 'laranja', 'carne']

item1, item2, item3, *outros = produtos

print(item1)
print(item2)
print(item3)
print(outros)
