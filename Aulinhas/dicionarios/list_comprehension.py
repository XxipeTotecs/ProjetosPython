#List Comprehension
  #Mais simples de se escrever
  #Utilizado quando vc precisa criar uma nova lista a partir de uma existente
  #[expressao for iten in itens]

frutas = ['mamao', 'abacate', 'pera', 'morango', 'xuxu', 'palmito', 'azeitona']

"""
Jeito mais extenso de escrever

frutas2 = []

for iten in frutas1:
  if 'n' in iten:
    frutas2.append(iten)

"""

frutas2 = [iten for iten in frutas if 'x' in iten]

print(frutas2)


valores = [x * 10 for x in range(6)]



#o x * 10 - o primeiro X é o item - e dps o loop na frente
print(valores)