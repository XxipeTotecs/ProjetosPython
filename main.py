# Calculo de IMC - Indice de Massa Corporal

"""
Qual é a sua Altura em cm:
Qual é o seu peso em kg:
"""

# Menor que 18,5     MAGREZA
# Entre 18,5 e 24,9  NORMAL
# Entre 25,0 e 29,9  SOBREPESO
# Entre 30,0 e 39.9  OBESIDADE
# Maior que 40,0     OBESIDADE GRAVE

altura = float(input('Qual é sua altura em cm: '))
peso = float(input('Qual é o seu peso em KG: '))

IMC = peso / (altura/100)**2

if IMC < 18.5:
  print('Magreza')

elif IMC >= 18.5 and IMC < 24.9:
  print('Normal')

elif IMC >= 25.0 and IMC < 29.9:
  print('Sobrepeso')

elif IMC >= 30.0 and IMC < 39.9:
  print('Obesidade')

else:
  print('Obesidade Grave')




