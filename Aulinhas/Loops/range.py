#For Loops (Loping)
# imprimir 1 até 50

#for numero in range(1, 51):
# print(numero)

dado_cliente = True
dado_pagamento = True

for aprovado in range(3):
  if dado_cliente and dado_pagamento:
    print('Sua compra foi aprovado')
    print('Parabénssss')
    break
    
  else:
    print('Erro nos dados, revise-os')
    break
    

"""
compras_confirmadas = True
dados_da_compra = 'Compra realizada no valro de R$74,55'

for enviar in range(10):
  if compras_confirmadas:
    print(dados_da_compra)
    print('cheque seu email')
    break

else:
  print('Erro na compra')

  

cachorro = False

for atoa in range(5):
  if cachorro:
    print('auau')
    print()

"""