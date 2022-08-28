'''
-------------------------------------------
Desenvolva um algoritmo que recebe o nome e o sobrenome de uma pessoa e mostra o nome inteiro dessa pessoa.

Algoritmo NomeSobrenome
inicio
    Declarar
        Nome alfanumerico;
        Sobrenome alfanumerico;
    
  //Entrada de dados e o processamento dos dados
  escrever("Digite seu nome: "); //essa mensagem aparece na tela do usuário
  ler(Nome); // o que o usuário digitar, é armazenado na variável Nome 
  escrever("Digite seu sobrenome: "); //essa mensagem aparece na tela do usuário
  ler(Sobrenome); // o que o usuário digitar, é armazenado na variável Sobrenome 

  //Processamento de dados
  Irei exibir direto no resultado, sem processar antes

  //Saída dos resultados
  escrever ("Prazer, " + Nome + Sobrenome);

fim
-----------------------------------------------
'''

Nome = input("Digite seu nome: ")
Sobrenome = input("Digite seu sobrenome: ")

print(f"Prazer, {Nome} {Sobrenome}")

'''
-------------------------------------------
Desenvolva um algoritmo que recebe o nome, a idade e o sexo de uma pessoa e mostra essas informações na tela.

Algoritmo Informacoes
inicio
    Declarar
        Nome alfanumerico;
        Idade inteiro;
        Genero alfanumerico;
    
  //Entrada de dados e o processamento dos dados
  escrever("Digite seu nome: "); //essa mensagem aparece na tela do usuário
  ler(Nome); // o que o usuário digitar, é armazenado na variável Nome 
  escrever("Digite sua idade: "); //essa mensagem aparece na tela do usuário
  ler(Idade); // o que o usuário digitar, é armazenado na variável Idade 
  escrever("Digite seu genêro: "); //essa mensagem aparece na tela do usuário
  ler(Genero); // o que o usuário digitar, é armazenado na variável Sexo 

  //Processamento de dados
  Irei exibir direto no resultado, sem processar antes

  //Saída dos resultados
  escrever (Nome + Idade + Genero);

fim
-----------------------------------------------
'''

Nome = input("Digite seu nome: ")
Idade = input("Digite sua idade: ")
Genero = input("Digite seu genero: ")

print(f"Prazer, {Nome}, sua idade é {Idade} e o genêro que você se identifica é {Genero}")