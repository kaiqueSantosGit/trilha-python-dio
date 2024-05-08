"""
  Conhecer as estruturs de repetição for e while e quando utilizá-las.
  
  O que são as estruturas de repetição?
São estruturas utilizadas para repetir um trecho de código um
determinado número de vezes. Esse número pode ser 
conhecido previamente ou determinado através de uma espressão lógica.

 Comando for e a função built-in range

 Comando for
O comando for é usado para percorrer um objeto iterável. faz
sentido usar for quando sabemos o número exato de vezes que 
nosso bloco de código deve ser execultado, ou quando 
queremos percorrer um objeto iteravel.
"""
texto = input("insira um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()
