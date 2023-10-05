#Logical Operatos (Operadores Logicos)


recebe_acima_5mil = False
nome_limpo = True

if recebe_acima_5mil and nome_limpo:                #os dois
  print('Financiamento Aprovado')

else:
  print('Financiamento Reprovado')


if recebe_acima_5mil or nome_limpo:                  #um ou o outro
  print('Financiamento Aprovado')

else:
  print('Financiamento Reprovado')


