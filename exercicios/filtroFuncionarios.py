# Lista de todos os funcionários
funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']

# Dicionário que armazena se cada funcionário tem carro ('tem_carro') e se trabalha de dia ('trabalha_dia')
info_funcionarios = {
    'Ana': {'tem_carro': True, 'trabalha_dia': True},
    'Marcos': {'tem_carro': True, 'trabalha_dia': True},
    'Alice': {'tem_carro': True, 'trabalha_dia': True},
    'Pedro': {'tem_carro': False, 'trabalha_dia': False},
    'Sophia': {'tem_carro': False, 'trabalha_dia': False},
    'Bruno': {'tem_carro': True, 'trabalha_dia': False},
    'Melissa': {'tem_carro': True, 'trabalha_dia': True}
}

# Separação dos funcionários em listas com base nas condições
funcionarios_carro_noite = [funcionario for funcionario, info in info_funcionarios.items() if info['tem_carro'] and not info['trabalha_dia']]
funcionarios_carro_dia = [funcionario for funcionario, info in info_funcionarios.items() if info['tem_carro'] and info['trabalha_dia']]
funcionarios_sem_carro = [funcionario for funcionario, info in info_funcionarios.items() if not info['tem_carro']]

# Exibição das listas
print("Funcionários que têm carro e trabalham à noite:", funcionarios_carro_noite)
print("Funcionários que têm carro e trabalham de dia:", funcionarios_carro_dia)
print("Funcionários que não têm carro:", funcionarios_sem_carro)