
"""
Tipo float
Tipo real, decimal
Casas decimais
OBS: O Separador de casas decimais na programação é o . e não a ,
"""

# Errado do ponto de vista do float, mas gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))

# Certo do ponto de vista float
valor = 1.44
print(valor)
print(type(valor))


# É possivel fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para um int
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com nùmeros complexos
variavel = 5j
