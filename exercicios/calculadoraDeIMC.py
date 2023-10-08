altura = float(input('Qual é sua altura em cm: '))
peso = float(input('Qual é o seu peso em KG: '))

# Converter altura de cm para metros
altura = altura / 100

# Calcular o IMC
imc = peso / (altura * altura)

if imc < 18.5:
    print('Você está com Magreza')
elif 18.5 <= imc < 24.9:
    print('Você está Normal')
elif 25.0 <= imc < 29.9:
    print('Você está com Sobrepeso')
elif 30.0 <= imc < 39.9:
    print('Você está com Obesidade')
else:
    print('Você está com Obesidade Grave, preocupe-se com sua saúde')