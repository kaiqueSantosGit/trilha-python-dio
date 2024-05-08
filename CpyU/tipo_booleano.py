"""
Tipo Booleano
Algoritimo Booleana, criada por George Boole
2 constantes, verdadeiro ou falso

True -> Verdadeiro
False - Falso

OBS: Sempre com a inicial maiuscula
Errado:
true, false

Certo:

True, False
"""
ativo = True
print(ativo)

"""
Operaçõe básicas 
"""
# Negação (not):
"""
 Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso
 se for falso o resultado será verdadeiro. ou seja, sempre ao contrario
"""

print(not ativo)

logado = False

# Ou (or)
"""
E uma operação binario, ou seja depende de dois valores, 
ou um ou outro deve ser verdadeiro

True or True = True
True or False = True
False or True = True 
False or False = False
"""
print(ativo or logado)

# E (and)
"""
Tambem é uma operação binaria, ou seja, depende de dois valores
ambos os valores devem ser verdadeiro
True and True = True 
True and  False = False
False and True = False
False and False = False
"""
