"""
-----------------------------------------
Desenvolva um algoritmo e um programa python que receba o ano atual e o ano de
nascimento de uma pessoa e mostre a idade dela no ano atual.

Algoritmo IdadeAtual
inicio
  Declarar
    AnoAtual inteiro;
    AnoNascimento inteiro;

  //Entrada de dados
  escrever("Digite o ano em que estamos:  "); 
  ler(AnoAtual); 
  escrever("Digite o ano em que você nasceu:  "); 
  ler(AnoNascimento); 

  //Processamento de dados
  Idade = AnoAtual - AnoNascimento

  //Saída dos resultados
  escrever ("Sua idade após seu aniversário desse ano será" + Idade);

fim
-----------------------------------------
"""

import decimal 

AnoAtual = decimal.Decimal(input("Digite o ano em que estamos: "))
AnoNascimento = decimal.Decimal(input("Digite o ano em que você nasceu: "))

Idade = AnoAtual - AnoNascimento;

print (f"\nSua idade após seu aniversário desse ano será: {Idade}.")