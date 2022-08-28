'''
---------------------------------------
Desenvolva um algoritmo que recebe dois valores numérico_real, calcula e mostra o quadrado da diferença desses dois números.

Algoritmo QuadradoDaDiferenca
inicio
  Declarar
    NumerosReais inteiro;

  //Entrada de dados e o processamento dos dados
  escrever("Digite dois numeros reais: "); //essa mensagem aparece na tela do usuário
  ler(NumerosReais); // o que o usuário digitar, é armazenado na variável NumeroReal 

  //Processamento de dados
  A, B = NumerosReais.split(A, B)
  Quadrado = (A ** 2) + 2 * A * B + (B ** 2)

  //Saída dos resultados
  escrever ("O quadrado da diferença dos números é de: " + Resultado);

fim
---------------------------------------
'''

NumerosReais = input("Digite dois numeros reais separados por vírgula: ")

A, B = NumerosReais.split(",")
A, B = int(A), int(B)

Quadrado = (A ** 2) + (2 * A * B) + (B ** 2)

print(f"O quadrado da diferença dos números é de: {Quadrado}")
