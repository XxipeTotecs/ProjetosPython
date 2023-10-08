"""
Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede. O usuário deverá fornecer as seguintes informações: rendimento, altura e largura.
O programa deve mostrar na tela a mensagem ' Vc necessita de x latas de tintas'

"""

import math

def calculo_tinta(rendimento, altura, largura):
    area = altura * largura
    total = area / rendimento
    latas_necessarias = math.ceil(total)  
    print(f'Você precisa de {latas_necessarias} latas de tinta')

rendimento = float(input("Informe o rendimento da tinta (em metros quadrados por litro): "))
altura = float(input("Informe a altura da parede (em metros): "))
largura = float(input("Informe a largura da parede (em metros): "))

calculo_tinta(rendimento, altura, largura)

