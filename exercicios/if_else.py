"""
Criar um programa que dependendo da temperatura do steak ele retorna o ponto de cozimento em portugues. O usuario deverá fornecer a temperatura.

Temperatura - Cozimento 
48°C - Rare (Selada)
54°C - Medium rare (ao ponto para o mal)
60°C - Medium (ao ponto)
65°C - Medium well (ao ponto para o bem)
71°C - Well done (bem passada)
"""

temperatura = int(input('Qual a temperatura desejada ? '))

if temperatura < 48:
  print('Cozinhar por mais alguns minutos')

elif temperatura in range(48, 53):
  print('Selada')

elif temperatura in range(54, 59):
  print('Ao ponto para ao mal')

elif temperatura in range(60, 64):
  print('ao ponto')

elif temperatura in range(65, 70):
  print('Ao ponto para o bem')

elif temperatura >= 71:
  print('Bem passada')

