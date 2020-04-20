# -*- coding: utf-8 -*-
# isso é um teste
var1 = ("olá mundo") #var string
var2 =(22) #var num inteiro
var3 =(11.1) #var num flutuante float
var4 = False #booleana falso
var5 = True #booleane verdadeiro

x = 100000
y = 10000

if x > y: #o comando if é atribuição de uma condição
    print("x é maior que y")

else: # o comando else entra em ação caso o if falhe ou em caso de não há necessidade de criar outra condição
    print("Y é maior que x")

x1 = 1
y1 = 2

if x1 == y1: # nesta situação temos 3 condições estabelecidas nos print's
    print("numeros iguais")
elif x1 < y1: #o programa vai executar a primeir condição verdadeira encontrada
    print("X é menor do que Y")
elif y1 > x1: # a codção  elif deve esstar entre IF e ELSE
    print("Y é maior do que X")

else:
    print ("numeros diferentes")

print("-----" * 10)

# Estruturas de repetição

#while = enquanto

x = 1

while x < 10:
    print(x)
    x = x+3
print("-----" *10)
#laço for

lista = [1,2,3,4,5]
lista2 = ["ola","mundo","!"]
lista3 = [0, "ola","biscoito","bolacha",9.99,True]

# quando o comando "for" é acionado
#ele pode selecionar qual variavel sera executada considerando os itens em seu conteúdo

for u in lista3:
    print(u)
for i in lista2:
    print(i)

print("----" *12)

for i in range(12): #atributo range aliado ao for pode invocar certa quantidade de itens de uma determinada variável.
    print(i)

#comando input

hi = input("Qual seu número favorito?")
print("o número digitado é:")
print(hi)
nome = input("Qual é o seu nome?")
print ("seja bem-vindo!" + nome)