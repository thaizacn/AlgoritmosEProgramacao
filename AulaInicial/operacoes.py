import decimal

Valor1 = decimal.Decimal(input("Digite o primeiro valor: "))
Valor2 = decimal.Decimal(input("Digite o segundo valor: "))

Resultado = Valor1 + Valor2;
print (f"\nA adição de {Valor1} com {Valor2} resulta em {Resultado}.")

Resultado = Valor1 - Valor2;
print (f"A subtração de {Valor1} com {Valor2} resulta em {Resultado}.")

Resultado = Valor1 * Valor2;
print (f"A multiplicação de {Valor1} com {Valor2} resulta em {Resultado}.")

Resultado = Valor1 / Valor2;
print (f"A divisão de {Valor1} com {Valor2} resulta em {Resultado}.")