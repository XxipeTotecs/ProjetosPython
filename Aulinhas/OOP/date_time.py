from datetime import datetime

#Python Object-Oreiented Programming

#Classes
  #Utilizadas para criar Objetos (instances)
  #Objetos são partes dentro de uma CLass (instancias)
  #Classes são utilizadas para agrupar dados e funções, podendo reutilizar


class Funcionarios:

  def __init__(self, nome, sobrenome, ano_nascimento):
    self.nome = nome
    self.sobrenome = sobrenome
    self.ano_nascimento = ano_nascimento

  def nome_completo(self):
    return self.nome, self.sobrenome, self.ano_nascimento

  def idade_funcionario(self):
    ano_atual = datetime.now().year
    self.ano_nascimento = int(ano_atual - self.ano_nascimento)
    return self.ano_nascimento
  

#CRIANDO O OBJETO
usuario1 = Funcionarios('Carlin', 'Matheus', 1654)
usuario2 = Funcionarios('Rosilda', 'Jasmira', 1994)


print(Funcionarios.idade_funcionario(usuario1))
print(Funcionarios.idade_funcionario(usuario2))

