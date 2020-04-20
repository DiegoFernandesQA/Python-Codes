import random

p = random.randrange(0, 1000)
while p % 5 and p % 7 == 0:
    break

import random

q = random.randrange(0, 1000)
while q % 5 and q % 7 == 0 and q != p:
    break

chave = p * q


def cifra(mensagem, chave, p, q):
    global listacifra
    scale = len(mensagem)
    listacifra = []
    for t in range(0, scale):
        letra = mensagem[t]
        s = ord(letra)
        o = s * q
        r = o / p
        j = r * (2 * chave)
        j = int(j)
        listacifra.append(j)
    return listacifra


def decifrar(cifra, chave, p, q):
    listadecifra = []
    scale = len(listacifra)
    for t in range(0, scale):
        deci = listacifra[t] / q
        tex = deci * p
        j = tex / (2 * chave)
        letter = int(j)
        letter = chr(letter)
        listadecifra.append(letter)
    return listadecifra


def prin():
    mensagem = input('escreva uma mensagem qualquer: ')

    print('sua mensagem cifrada será: ', cifra(mensagem, chave, p, q))

    print('suamensagem')
    decifrada
    será: ('decifrar(cifra, chave, p, q))

    print('chave publica : ', chave)
