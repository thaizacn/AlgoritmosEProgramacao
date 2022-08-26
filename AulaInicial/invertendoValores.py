"""
Desenvolva um algoritmo e um programa python que receba dois números inteiros
para as variáveis x e y, efetua a troca dos valores, ou seja, x para a ter o valor
de y e y passa a ter o valor de x. E mostra os valores trocados.

Algoritmo TrocaDeValores
inicio
  Declarar
    X inteiro;
    Y inteiro;

  //Entrada de dados
  escrever("Digite o valor de X:  "); 
  ler(ValorY); 
  escrever("Digite o valor de Y:  "); 
  ler(ValorX); 

  //Processamento de dados
  X = ValorY;
  Y = ValorX;

  //Saída dos resultados
  escrever ("O novo valor de X é" + X + "e o novo valor de Y é": + Y);

fim
-----------------------------------------
"""

import decimal

ValorX = decimal.Decimal(input("Digite o valor de X: "))
ValorY = decimal.Decimal(input("Digite o valor de Y: "))

X = ValorY;
Y = ValorX;

print (f"\nO novo valor de X é {X} e o novo valor de Y é {Y}.")