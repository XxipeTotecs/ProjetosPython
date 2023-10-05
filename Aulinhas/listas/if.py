cor_cliente = input('Digite a cor desejada: ')

cores = ['azul', 'vermelho', 'amarelo', 'rosa', 'caju', 'uva']

if cor_cliente.lower() in cores:
  print('Cor em estoque')

else:
  print('Nao temos em estoque')

