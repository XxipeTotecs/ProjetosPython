# Meu Repositório Python

Este repositório contém vários arquivos e pastas relacionados ao meu aprendizado em Python. Abaixo, descrevo a estrutura do projeto e os exercícios presentes na pasta "Exercicios".













<p><img align="right" src="https://user-images.githubusercontent.com/29899042/209016241-ed8f02ec-daaa-4ee3-95b9-b7c7075074b8.gif" alt="adam-pw" /></p>


## Estrutura do Projeto

- 📘 **Aulinhas**: Esta pasta contém arquivos relacionados aos conceitos básicos da linguagem Python. Aqui estão os arquivos presentes nesta pasta:

    - 📖 `dicionarios`: Contém exemplos de uso de dicionários em Python.
        - `filter.py`: Demonstração do uso da função `filter`.
        - `forloops.py`: Exemplos de loops `for`.
        - `generetaor_expressions.py`: Introdução a expressões geradoras.
        - `key_values.py`: Exemplos de manipulação de chaves em dicionários.
        - `lambda.py`: Uso de funções lambda em Python.
        - `list_comprehension.py`: Demonstração de list comprehensions.
        - `maps.py`: Exemplos de uso da função `map`.

    - 🛠️ `erros/`: Contém exemplos de tratamento de erros em Python.
        - `else_finally.py`: Uso das cláusulas `else` e `finally` com exceções.
        - `try_except.py`: Demonstração de tratamento de exceções com `try` e `except`.





    - 🧩 `functions/`: Contém exemplos relacionados a funções em Python.
        - `default_nondefault.py`: Uso de argumentos padrão e não padrão em funções.
        - `functions.py`: Exemplos de criação e chamada de funções.
        - `modulo.py`: Importação de módulos e funções.
        - `return.py`: Uso de `return` em funções.
        - `xargs.py`: Exemplos de uso de *args em funções.

    - 📃 `listas/`: Contém exemplos relacionados a listas em Python.
        - `array.py`: Demonstração de arrays em Python.
        - `if.py`: Uso de estruturas condicionais com listas.
        - `listas.py`: Operações básicas em listas.
        - `manipulando.py`: Manipulação de listas.
        - `sets.py`: Introdução a conjuntos em Python.
        - `split.py`: Uso da função `split`.
        - `tuples_list.py`: Exemplos de tuplas e listas.
        - `unpacking.py`: Demonstração do desempacotamento de listas e tuplas.
        - `zip.py`: Uso da função `zip`.

    - 🔄 `loops/`: Contém exemplos relacionados a loops em Python.
        - `if.py`: Uso de estruturas condicionais em loops.
        - `nested_loops.py`: Exemplos de loops aninhados.
        - `range.py`: Demonstração do uso da função `range`.
        - `simbolo_loop.py`: Uso do símbolo `for` em loops.
        - `strings.py`: Manipulação de strings em loops.
        - `treinamento.py`: Exemplos de treinamento com loops.
        - `while.py`: Uso da estrutura de repetição `while`.

    - 🧬 `OOP/`: Contém exemplos relacionados a Programação Orientada a Objetos (OOP).
        - `classes.py`: Criação de classes em Python.
        - `contrutores_self.py`: Uso de construtores e a referência `self`.
        - `date_time.py`: Manipulação de datas e horas.
        - `parametros_objetos.py`: Exemplos de passagem de parâmetros entre objetos.
        - `self.py`: Uso da palavra-chave `self` em classes.

    - 🚀 `primeiros_passos/`: Contém exemplos iniciais de programação em Python.
        - `formated_string.py`: Formatação de strings.
        - `if_else.py`: Uso de estruturas condicionais `if-else`.
        - `logical_operator.py`: Exemplos de operadores lógicos.
        - `multiplos_operadores.py`: Demonstração de múltiplos operadores.
        - `numeros.py`: Manipulação de números em Python.
        - `operador_de_atribuição.py`: Uso de operadores de atribuição.
        - `operador_ternario.py`: Utilização de operadores ternários.
        - `slice.py`: Exemplos de fatiamento de sequências.
        - `variaveis_e_input.py`: Trabalhando com variáveis e entrada de dados.
     
 <br>

 - ### **Exercicios**: Nesta pasta estão exercícios relacionados ao aprendizado em Python. Abaixo, descrevo cada um deles:

 



 
   ## 📊 Calculadora.py - Cálculo de IMC (Índice de Massa Corporal)
   
	Este programa calcula o Índice de Massa Corporal (IMC) com base na altura (em centímetros) e no peso (em quilogramas) fornecidos pelo usuário.
	O IMC é uma métrica comumente usada para avaliar a saúde com 	base no peso corporal. O programa segue as diretrizes a seguir:

	O usuário é solicitado a inserir sua altura em centímetros e seu peso em quilogramas.

	O IMC é calculado usando a fórmula: IMC = peso / (altura / 100)^2.

	O resultado do IMC é classificado em uma das categorias de saúde, incluindo "MAGREZA," "NORMAL," "SOBREPESO," "OBESIDADE," e "OBESIDADE GRAVE," de acordo com os valores de referência.



    ## 🎨 CalcularRendimentoTinta.py - Cálculo da Quantidade de Tinta
   
	Este programa é projetado para calcular a quantidade de tinta necessária para pintar uma parede com base nas informações fornecidas pelo usuário. O programa segue as seguintes etapas:

	O usuário é solicitado a inserir o rendimento da tinta em metros quadrados por litro,
	 a altura da parede em metros e a largura da parede em metros.
	A área da parede é calculada multiplicando a altura pela largura.

	O programa então determina a quantidade total de latas de tinta necessárias para cobrir a parede e exibe a resposta.



    ## 🚗 FiltroFuncionario.py - Filtragem de Funcionários por Critérios
   
	Neste exercício, o objetivo é gerar três listas de funcionários com base em critérios específicos:

	lista1: Funcionários que têm carro e trabalham à noite.

	lista2: Funcionários que têm carro e trabalham durante o dia.

	lista3: Funcionários que não têm carro.

	Os nomes dos funcionários estão predefinidos na lista funcionarios, e as listas resultantes são geradas usando operações de conjunto em Python.



    ## 🍖 Temperatura_da_carne.py - Determinação do Ponto de Cozimento da Carne
   
	Este programa recebe a temperatura fornecida pelo usuário e determina o ponto de cozimento da carne em português com base na seguinte tabela:

	48°C: Rare (Selada)
   
	54°C: Medium rare (ao ponto para o mal)
   
	60°C: Medium (ao ponto)
   
	65°C: Medium well (ao ponto para o bem)
   
	71°C ou mais: Well done (bem passada)
   
	O programa compara a temperatura inserida pelo usuário com os valores da tabela e retorna o ponto de cozimento correspondente.
