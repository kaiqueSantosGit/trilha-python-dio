"""
  A estética
 Identar Código é uma forma de manter o códico fonte mais legível e manutenível.
 Mas em Python ela exerce um segundo papel, através da identação o interpretador consegue 
 determinar onde um bloco de comando inicia e onde ele termina

  Bloco de comando:
 As linguagens de programação costumam utilizar caracteres ou palavras reservadas para terminar o inicio e o fim do bloco.
 Em Java e C por exemplo, utilizavamos chaves:
"""


def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print('valor sacado!')


sacar(100)
