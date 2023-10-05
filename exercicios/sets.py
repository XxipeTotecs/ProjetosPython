"""
Criar um programa que gera 3 listas de acordo com a necessidade abaixo:

#listas 1 = funcionarios que tem carro e trabalham a noite
#listas 2 = funcionarios que tem carro e trabalham de dia
#listas 3 = funcionarios que não tem carro

"""

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
noite = ['Pedro', 'Sophia', 'Bruno']
tem = ['Marcos', 'Alice', 'Bruno', 'Melissa']

#Lista1
lista1 = set(tem).intersection(noite)
print(lista1)

lista2 = set(tem).intersection(dia)
print(lista2)

lista3 = set(funcionarios).difference(tem)
print(lista3)


