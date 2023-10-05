"""
Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede. O usuário deverá fornecer as seguintes informações: rendimento, altura e largura.
O programa deve mostrar na tela a mensagem ' Vc necessita de x latas de tintas'

"""



rendimento = int(input("Informe o rendimento da tinta (em metros quadrados por litro): "))
altura = int(input("Informe a altura da parede (em metros): "))
largura = int(input("Informe a largura da parede (em metros): "))


def calculo_tinta():
  area = altura * largura
  total = area / rendimento
  print(f'Vc precisa de {total} latas de tintas')

calculo_tinta()

