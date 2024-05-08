"""
  Conhecer métodos úteis para manipular objetos do tipo string, como
  interpolar de variáveis e entender como funciona o fatiamento.

  Etapa 1: Conhecendo métodos úteis da clase string 
A classe string do python é famosa por ser rica em metodos e
possuir uma interface muito facil de trabalhar
Em algumas linguagens manipular sequências de caracteres 
não é um trabalho trivia, porem em python esse trabalho é muito simples

Alguns utilitarios e metodos:
Maiúscula, munúscula e título: EX: Variavel.uper()
.uper() -> para deixar todas as letras maiúsculas 
.lower() -> para deixar todas minusculas
.title() -> converte tudo para minuscula exeto o primeiro caracter

Eliminando espaços em branco: EX: Curso = "   Python "
.strip() -> elimina todos os espaços da variavel
.lstrip() -> elimina os espacos da esqueda
.rstrip() -> elimina todos os espaços do lado direito

Junções e centralização: 
.center(10, "#") -> deve se indicar o numero total de caracteres e o caracter que quer adicionar ou 
deixe em branco que ficara vazio centralizado
"." .join(variavel) -> ele ira passar letra por letra da variavel e adicionara 
a caracter que for selecionada P.y.t.h.o.n

  Etapa 2: Interpolação de variaveis

  Etapa 3: Fatiamento de string
  etapa 4: String múltipla linhas 
"""
nome = "kAiQue"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  Olá mundo!    "

print(texto)
print(texto.strip())
print(texto.rstrip())
print(texto.lstrip())

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("-".join(menu))