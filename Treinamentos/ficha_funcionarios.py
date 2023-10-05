
lista_funcionarios = ['eduardo', 'neudia', 'adriana', 'clelia', 'gustavo', 'luiz']

print(lista_funcionarios)

def ficha_funcionario(nome):
    funcionarios = {
        'eduardo': {
            'idade': 30,
            'cargo': 'Gerente',
            'salario': 6000,
        },
        'neudia': {
            'idade': 35,
            'cargo': 'Supervisora',
            'salario': 4500,
        },
        'adriana': {
            'idade': 52,
            'cargo': 'Recepção',
            'salario': 2100
        },
        'clelia': {
            'idade': 68,
            'cargo': 'Cordenadora',
            'salario': 3500
        },
        'gustavo': {
            'idade': 30,
            'cargo': 'Motorista',
            'salario': 7000,
        },
        'luiz': {
            'idade': 12,
            'cargo': 'Estoque',
            'salario': 654
        }
    }

    if nome.lower() in funcionarios:
        return funcionarios[nome.lower()]
    else:
        return None


x = input('Digite o nome do funcionario: ')


if x.lower() in lista_funcionarios:
    print(f'O funcionario {x} está cadastrado')
    ficha = ficha_funcionario(x)
    if ficha:
        print('Ficha do funcionário:')
        for chave, valor in ficha.items():
            print(f'{chave.capitalize()}: {valor}')
else:
    print('Funcionario não localizado')



