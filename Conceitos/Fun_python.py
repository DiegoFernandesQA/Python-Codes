#strings

#Concatenação de strings duas var com somas

a = "Diego"
b = "José"
xx = "O Rato Roeu a Roupa do Rei de Roma"

print (a [0:7] + " " + b [0:4])
concatenar = a + " " + b
print (concatenar)

#metodos: lower, upper, strip, split, find

#ex Lower: deixa a declaração de texto de uma variável em letras minusculas

print (xx.lower())

#ex upper: Deixa todas as letras maiusculas

print(xx.upper())

#ex Strip: esse metodo serve para remover espaços do texto de uma var
print(xx.strip())

#ex stripe: Deixa um texto dividido em listas

print (xx.split())

# case sensitive recurso do python que diferencia termo maiusculo de minuscula

# metodo find: busca a posição numerica da localização do caractere

busca = xx.find("Rei")

print(busca)
print (xx [busca:])

# replace: Substitui uma palavra por outra encontra a primeira e troca pela segunda 1ª Rei 2ª Rainha

xx = xx.replace("Rei","Rainha")
print(xx)
