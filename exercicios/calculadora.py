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
peso = int(input('Qual é o seu peso em KG: '))

resultado = peso / altura

if resultado < 18.5:
  print('Você está com Magreza')

elif resultado in range(18.5, 24.9):
  print('Você está Normal')

elif resultado in range(25.0, 29.9):
  print('Você está com Sobrepeso')

elif resultado in range(30.0, 39.9):
  print('Você está com Obesidade')

elif resultado > 40:
  print('Você está com Obesidade Grave, preocupe-se com sua saúde')
