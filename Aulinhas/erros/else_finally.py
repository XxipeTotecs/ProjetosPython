#Erros 
  # Exceleten para testes # Nao realiza o 'stop' no programa, # Mensagens customizadas quando encontra um erro

try:
  litras = ['a', 'b', 'l']
  print(litras[3])
except IndexError:#EXCEPT É SEMPRE O ERRO QUE APARECE ALI >>>
  print('INdex nao existe')        



try: 
  valor = int(input('DIgite o valor do seu produto: '))
  print(valor)    
except ValueError:                          # EXCEPT SO APARECE SE TRY NAO FOR OK
  print('Por favor digitar o valor em numeros')

finally:
  print('codigo ok')                        #APARECE DE QUALQUER JORMA

"""
else:                                      #ELSE APARECE SE TRY ESTIVER OK
  print('Usuario digitou um valor correto')
  resultado = valor * 2
  print(resultado)


print('mais codigos a baixo')
"""