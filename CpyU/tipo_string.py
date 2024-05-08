"""
Tipo string

Já vimos que em python um dado é considerado do tipo string, sempre que 
- Estiver entre aspas simples -> 'uma string' '234, 'a', 'True', '42,3'
- Estiver entre áspas duplas -> "uma string" ...
- Estiver entre aspas simples triplas '''uma string''' ...
- Estiver entre aspas duplas triplas  ...

nome = 'Geek Universit'
print(nome)
print(type(nome))

# Para que as varios tipos de áspas? Exemplo

nome = "Gina's Bar"  # A áspas simples foi usada para escrever a palavra "Gina's" então a possibilidade de formar a string com as "áspas duplas"
print(nome)
print(type(nome))

nome = 'Angelina \n Jolie'
print(nome)
print(type(nome))

nome = ...Angelina 
Jolie...
print(nome) # Funciona as aspas triplas para permitir a palavra ser dividida em linhas 
print(type(nome))

"""
nome = 'Geek Universit'
print(nome.upper())
