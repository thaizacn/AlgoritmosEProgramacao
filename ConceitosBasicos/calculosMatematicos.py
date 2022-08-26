"""
-----------------------------------------
Desenvolva um algoritmo que receba os valores dos catetos de um triângulo 
retângulo, calcula e mostra o valor da hipotenusa desse triângulo. 
Fórumula: hipotenusa ao quadrado = cateto 1 ao quadrado + catedo 2 ao quadrado
-----------------------------------------
"""
import math

Cateto1 = float(input('Qual o valor do cateto oposto? '))
Cateto2 = float(input('Qual o valor do cateto adjacente? '))

Hipotenusa = math.sqrt(Cateto2 ** 2 + Cateto1 ** 2) 

print(f"\nO valor da hipotenusa é: {Hipotenusa}.")



"""
-----------------------------------------
Desenvolva um algoritmo e um programa python que receba a base e a altura de
um triângulo, calcula e mostra a sua área. Lembrando que A = (base * altura)/2.
-----------------------------------------
"""

import decimal

Base = decimal.Decimal(input("Digite a base do triângulo: "))
Altura = decimal.Decimal(input("Digite a altura do triângulo: "))

Area = (Base * Altura)/2;

print (f"\nA área do triângulo é de {Area}.")