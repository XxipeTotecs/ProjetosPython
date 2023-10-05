#Python Object-Oreiented Programming

#Classes
  #Utilizadas para criar Objetos (instances)
  #Objetos são partes dentro de uma CLass (instancias)
  #Classes são utilizadas para agrupar dados e funções, podendo reutilizar


class Funcionarios:

  def __init__(self, nome, sobrenome, data_nascimento):
    self.nome = nome
    self.sobrenome = sobrenome
    self.data_nascimento = data_nascimento
  

#CRIANDO O OBJETO
usuario1 = Funcionarios('Carlin', 'Matheus', '10/05/1997')

usuario2 = Funcionarios('Rosilda', 'Jasmira', '10/10/1028')


print(usuario1)
print(usuario2.nome)



"""
#CRIANDO OS PARAMETROS DO USUARIO 1

usuario1.nome = 'Elena'
usuario1.sobrenome = 'Chagas'
usuario1.nascimento = '10/05/2020'

#CRIANDO OS PARAMETROS DO USUARIO 2 

usuario2.nome = 'Elena'
usuario2.sobrenome = 'Chagas'
usuario2.nascimento = '10/05/2020'

#print

print(usuario1)
print(usuario2.nome)
"""



