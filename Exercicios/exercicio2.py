"""
Leia um numero fornecido pelo usuario, se esse numero for positivo, 
calcule a raiz quadrada do numero. se o numero for negativo,
mostre uma mensagem dizendo que o numero é invalido.
"""
numero_usuario = float(input('Digite um numero: '))

if numero_usuario >= 0:
    raiz_quadrada = numero_usuario ** 0, 5
    print(f'A raiz quadrada de {numero_usuario} é: {raiz_quadrada}')

else:
    print('Numero invalido, não é possivel calcular a raiz quadrada de um numero negativo!')
