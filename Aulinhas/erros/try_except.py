#Erros 
  # Exceleten para testes # Nao realiza o 'stop' no programa, # Mensagens customizadas quando encontra um erro

try:
  litras = ['a', 'b', 'l']
  print(litras[3])
except IndexError:#EXCEPT É SEMPRE O ERRO QUE APARECE ALI >>>
  print('INdex nao existe')        



try: valor = int(input('DIgite o valor do seu produto: '))
    print(valor)
    except ValueError:
print('Por favor digitar o valor em numeros')

print('mais codigos a baixo')