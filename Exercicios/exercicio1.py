"""
Faça um programa que receba dois numeros e mostre qual deles é maior 

"""
numero1 = float(input('Digite o primeiro numero: '))
numero2 = float(input('Digite o segundo numero numero: '))

if numero1 > numero2:
    print(f'{numero1} é maior que {numero2}')
elif numero1 < numero2:
    print(f'{numero1} é menor do que {numero2}')
else:
    print('os numeros são iguais')
