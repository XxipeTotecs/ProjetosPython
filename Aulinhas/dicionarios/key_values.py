
#Dicionários
  #Utiliza index no formato de keys e values
  #aceita string, integer, float e boleam


alunos = {'nome': 'Ana', 'idade': 23, 'aprovado': True}


      

print(alunos['nome'])


alunos.update({'nome': 'Kevin', 'aprovado': False})          #ele troca ou adiciona uma key e value

print(alunos)


print(alunos.get('edenreço', 'Não Existe'))

del alunos['aprovado']
print(alunos)
