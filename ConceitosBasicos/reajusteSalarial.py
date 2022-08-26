'''
-----------------------------------------
1º Exercicio

Desenvolva um algoritmo e um programa python que receba o valor do salário 
de um colaborador, calcula e mostra o seu novo salário com um reajuste de 23%.

Algoritmo CalculoSalario
inicio
  Declarar
    SalarioAtual inteiro;

  //Entrada de dados e o processamento dos dados
  escrever("Digite seu salário: "); //essa mensagem aparece na tela do usuário
  ler(SalarioAtual); // o que o usuário digitar, é armazenado na variável Nome 

  //Processamento de dados
  SalarioAtual * 23%

  //Saída dos resultados
  escrever ("O seu salario atual" + SalarioAtual + ", com o reajuste irá para " + Resultado);

fim
-----------------------------------------
'''

import decimal

SalarioAtual = decimal.Decimal(input("Digite o seu salario: "))

Por = SalarioAtual / 100
Reajuste = Por * 23;
Resultado = SalarioAtual + Reajuste;
print (f"\nO seu salario atual {SalarioAtual} com o reajuste irá para {Resultado}.")