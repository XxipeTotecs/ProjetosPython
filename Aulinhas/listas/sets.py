
#SETS (LISTAS
    #SIMILAR A LISTAS
    #EVITA ITENS DUPLICADOS)
    #NÃO UTILIZA INDEX

list1 = [10, 20, 30, 40, 50, 70]
list2 = [10, 20, 30, 40, 60]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2)   #Union
print(num1 - num2)   #Difference
print(num1 ^ num2)   #Symmetric Difference
print(num1 & num2)   #And

print(len(num1))




set1 = {1, 2, 3, 5, 7, 8, 9}
set1.update([8, 9, 78, 90, 6335])        #ADICIONA
set1.remove(2)                    #GERA ERRO SE N EXISTIR O NUMERO
set1.discard(42)                #O DISCARD N GERA ERRO SE NAO EXISTIR O NUMERO

print(set1)




