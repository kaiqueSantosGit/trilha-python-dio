"""
PEP* - Python Enhancement Proposal

São propostas  de melhorias para a linguagem python

The zen of python

import this

A ideia da pep8 é que possamos escrever codigos python de forma pythónica =
de forma bonita de forma visualmente agradavel

(1) - utilize Camel Case para nomes de clases; toda inicial deve ser maiuscula, e se for nome composto
iniciais de cada palavra deve ser maiuscula

class Calculadora:
    pass

class calculadora_cientifica:  ERROR
    pass

class CalculadoraCientifica:

(2) - Utilize nomes em minusculo, separados por underline para funções ou variaveis

def soma():
    pass

def soma_dois():
    pass

numero = 4

numero_impar = 5

(3) - Utilize quatro espaços para identação! (NÃO UTILIZAR TAB)

if 'a' in 'Banana':
    print ('tem')

if 'a' in 'Banana':
print ('tem')         ERRADO

(4) - Linhas em branco
- Separar funções e definções de classes com duas linhas em branco;
- Metodos dentro de uma classe devem ser separados com uma unica em branco;

(5) - Import
- Imports devem ser sempre feitos em linhas separadas;
#Errado

import sys, os

# Import Certo

import sys
import os
# Não há problemas em utilizar from types import StringType, ListType

- Caso tenha muitos imports de um mesmo pacote recomenda-se fazer;
from types import (
    StringType,
    ListType,
    SetType,
    OutroType,
)
- Imports devem ser colocados no topo do arquivo logo depois de quaisquer comentarios ou docstrings e
antes de constantes ou variaveis globais;

(6) - Espaços em expressões e instruções

#Não faça

funcao( algo[ 1 ], { outro: 2 } )

#Faça

funcao(algo[1], {outro: 2})

-pdf documento sobre o PEP8 para estudos
file:///C:/Users/kaiqu/OneDrive/Documentos/cursos/python/02-pep8.pdf

"""

print ('Aula concluida com sucesso!')





