nota1 = float(input('primeira prova: '))
nota2 = float(input('segunda prova:'))
media = (nota1 + nota2) / 2
print(media)

if media > 6:
    print('Parabéns, você foi aprovado')

if media < 6:
    print('reprovado')