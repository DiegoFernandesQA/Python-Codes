nome = input('Olá, qual o seu nome?')
print('Cotação do dolar hoje: U$1,00 vale R$3.27')
print('-' * 10,'||BEM VINDO AO CONVERSOR DE MOEDAS||', '-'*10)
print()
real = float(input('Quanto dinheiro você tem na sua carteira? R$'))
dolar = real/3.27
euro = real/4.10
yenes = real/2.00
print('Conversão de R${:.2f}, com isso você pode comprar U${:.3f}'.format(real, dolar))
print('Conversão de R${:.2f}, com isso você pode comprar EUR${:.3f}'.format(real, euro))
print('Conversão de R${:.2f}, com isso você pode comprar Y${:.3f}'.format(real, yenes))
print()
print(nome, ', muito obrigado por utilizar o conversor de moedas o AlRight Bank agradece!')