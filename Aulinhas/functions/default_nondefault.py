#DEFAULT - AQUELE DEFINE O VALOR DO PARÂMETRO
#NON-DEFAULT = AQUELE QUE VC NÃO DEFINE O VALOR DO PARÂMETRO


def boas_vindas(nome, quantidade=5):        #<DEFAULT QUANTIDADE PARAMETRO
  print(f'Ola {nome} ')
  print(f'Temos no momento {str(quantidade)} de laptops disponiveis')


boas_vindas('Carlim')        #SÓ COLOCA A NON-DEFAULT ARGUMENTO

