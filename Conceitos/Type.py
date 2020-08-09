# crie um programa que leia dois números e mostre a soma entre eles.
# -*- coding: utf-8 -*-
"""""
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro número para somar: "))
r = n1 + n2
print("O resultado da soma de {} com {} é igual à {} ".format(n1, n2, r))

"""

#que leia algo pelo teclado e mostre na tela o seu tipo primitivo
#e todas as informações possíveis sobre ela.
a = 1
b = "a"
p = input("Digite algo: ")
print (type(p))
print (p.isnumeric(), 'é numerico')
print (p.isalnum(), 'é  alfa númerico')
print (p.isdigit(), 'É um digito')
print (p.isupper(), 'Tem letra maiuscula')
print (p.isprintable(), 'É impresso')
print (p.isdecimal(), 'é decimal')

print (f'era {a} uma {b} e {p}')