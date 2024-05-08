"""
Escopo de varìaveis

Dois casos de escopo
1- Variaveis globais:
são reconhecidas, ou seja, seu escopo compreende todo o programa
2- Variaveis locais:
são reconhecidas apenas no bloco onde foram declaradas, 
ou seja seu escopo esta limitado ao bloco onde foi declarada

Para declarar variaveis em python fazemos:
nome_da_variavel = valor_da_variavel

pyton é uma linguagem de tipagem dinamica, significa que ao declararmos uma variavel,
nós não colocamos o tipo de dado dela
este tipo é inferido ao atribuirmos o valor a mesma.

exemplo em C:
int numero = 42

exemplo em java:
int numero = 42

"""
numero = 42  # Exemplo de variavel global
print(numero)
print(type(numero))

numero = "Geek"
print(numero)
print(type(numero))

numero = 42
# novo = 0
if numero > 10:  # Exemplo de variavel local, pois 'novo' esta declarado dentro de 'if'
    novo = numero + 10
    print(novo)

print(novo)
