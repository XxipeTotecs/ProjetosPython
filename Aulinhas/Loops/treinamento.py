

#Exercício: Crie um programa que solicite ao usuário a entrada de dois números inteiros. Em seguida, calcule e exiba a soma, a subtração, a multiplicação e a divisão desses números.


num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))


print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

  





"""
cpf_cliente = True
cel_cliente = True
end_cliente = True

for dados in range(5):
  if cpf_cliente and cel_cliente and end_cliente:
    print('Parabéns, sua compra foi efetuada com sucesso')
    break

  elif cpf_cliente != True:
    print('Erro no seu cpf')
    break

  elif cel_cliente != True:
    print('Erro no celular')
    break

  elif end_cliente != True:
    print('Erro no seu endereço')
    break

print('Para continuar a compra, siga com os dados')

pai = input('Digite o nome do seu pai:  ')
mae = input('Digite o nome da sua mãe: ')

print(f'O nome {pai} está correto ?')
if pai == True:
  print('Proseguir')
else:
  print('Nome invalido')
  
print(f' O nome {mae} está correto ?')
if mae == True:
  print('Proseguir')

anos = int(input('Digite sua idade'))

if anos >= 18:
  print('Você pode seguir')

else:
  print('Acesso Negado')


------------------------------------------------------------------------

nome_cliente = input('Digite seu nome por favor:')
cpf_cliente = int(input('Digite seu cpf: '))

cpf_cliente == False
nome_cliente == True

for dados in range(3):
  if nome_cliente and cpf_cliente == True:
    print('Parabens, dados corretos')
    break

  elif nome_cliente != True:
    print(f'Erro no {nome_cliente}, corrija:  ')
    break
    
  elif cpf_cliente != cpf_cliente:
    print(f' Erro no seu {cpf_cliente}, corrija: ')
    break
    
  else:
    print(f'Erro no {cpf_cliente} e no {nome_cliente}')
    break


"""




