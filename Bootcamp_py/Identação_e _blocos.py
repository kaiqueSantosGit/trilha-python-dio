"""
  Identação e blocos de comandos:
  A estetica: 
  Identar código é uma forma de manter o código fonte mais
  leg´vel e manutenível. mas em Python ela exerce um segundo papel,
  através da indentação o interpretador consegue determinar onde um bloco de comando
  inicia e onde ele termina. 

  Bloco de comando:
  As linguagens de programação costumam utilizar caracteres ou palavras reservadas 
  para terminar o inicio e o fim do bloco. Em Java e C por exemplo, utilizavamos chaves.

  Utilizando espaços:
  Existe uma convenção em python, que define as boas práticas para escrita de codigo na linguagem.
  Nesse documento é indicado utilizar 4 espaços em branco por nivel de identação, ou seja, a cada novo bloco adicionamos 
  4 novos espaços em branco.
"""


def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa")

    print("obrigado por ser nosso cliente, tenha um bom dia")


def depositar(valor):
    saldo = 500
    saldo += valor


sacar(100)
