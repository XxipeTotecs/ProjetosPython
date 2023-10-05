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

  def nome_completo(self):
    return self.nome, self.sobrenome, self.data_nascimento
  

#CRIANDO O OBJETO
usuario1 = Funcionarios('Carlin', 'Matheus', '10/05/1997')
usuario2 = Funcionarios('Rosilda', 'Jasmira', '10/10/1028')


print(Funcionarios.nome_completo(usuario1))
print(Funcionarios.nome_completo(usuario2))

