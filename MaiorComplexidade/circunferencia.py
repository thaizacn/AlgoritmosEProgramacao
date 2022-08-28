'''
-------------------------------------
Desenvolva um algoritmo que recebe o raio (R) de uma circunferência, calcula e mostra o comprimento desta circunferência. 
Fórmula do comprimento da circunferência: C = 2 .  . R.

Algoritmo ComprimentoCircunferencia
inicio
    Declarar
        Raio inteiro;
    
  //Entrada de dados e o processamento dos dados
  escrever("Digite o raio da circunferência: "); //essa mensagem aparece na tela do usuário
  ler(Raio); // o que o usuário digitar, é armazenado na variável NumeroReal 

  //Processamento de dados
  Resultado = 2 * math.pi * Raio

  //Saída dos resultados
  escrever ("O comprimento da circunferência é: " + Resultado);

fim
-------------------------------------
'''
import math

Raio = float(input("Digite o valor do raio da circunferência: "))

Resultado = 2 * math.pi * Raio

print(f"O comprimento da circunferência é: {Resultado}")


'''
---------------------------------------
Desenvolva um algoritmo que recebe o raio (R) de uma circunferência, calcula e mostra a área desta circunferência. 
Fórmula da área: A =  . R^2.

Algoritmo AreaCircunferencia
inicio
    Declarar
        Raio inteiro;
    
  //Entrada de dados e o processamento dos dados
  escrever("Digite o raio da circunferência: "); //essa mensagem aparece na tela do usuário
  ler(Raio); // o que o usuário digitar, é armazenado na variável NumeroReal 

  //Processamento de dados
  Resultado = math.pi * (Raio ** 2)

  //Saída dos resultados
  escrever ("A área da circunferência é: " + Resultado);

fim
-------------------------------------
'''

import math

Raio = float(input("Digite o valor do raio da circunferência: "))

Resultado = math.pi * (Raio ** 2)

print(f"A área da circunferência é: {Resultado}")