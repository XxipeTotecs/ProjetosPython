"""
Criar um programa que dependendo da temperatura do steak ele retorna o ponto de cozimento em portugues. O usuario deverá fornecer a temperatura.

Temperatura - Cozimento 
48°C - Rare (Selada)
54°C - Medium rare (ao ponto para o mal)
60°C - Medium (ao ponto)
65°C - Medium well (ao ponto para o bem)
71°C - Well done (bem passada)
"""

temperatura = int(input('Qual a temperatura desejada? '))

if temperatura < 48:
    print('Ainda não está pronto. Cozinhe por mais alguns minutos.')

elif temperatura < 54:
    print('Rare (Selada)')

elif temperatura < 60:
    print('Medium rare (ao ponto para o mal)')

elif temperatura < 65:
    print('Medium (ao ponto)')

elif temperatura < 71:
    print('Medium well (ao ponto para o bem)')

else:
    print('Well done (bem passada)')