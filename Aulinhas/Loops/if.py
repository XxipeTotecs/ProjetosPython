#enviar email com detalhes da compra online(maximo 3 tentativas) para compras confirmadas.

compras_confirmadas = True
dados_da_compra = 'Compra realizada no valro de R$74,55'

for enviar in range(3):
  if compras_confirmadas:
    print(dados_da_compra)
    print('cheque seu email')
    break

else:
  print('Erro na compra')

  
    