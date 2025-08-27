velocidade = float(input('Digite a velocidade que ultrapassou o radar: Km: '))
multa = (velocidade - 90) * 7
if velocidade > 90:
    print('Você ultrapassou o limite de velocidade de 90km por hora\n Você será multado em R${:.2f}'.format(multa))
else:
    print('PARABÉNS...\n Você respeitou o limite da via')