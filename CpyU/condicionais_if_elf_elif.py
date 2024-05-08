"""
Estruturas condicionais
if, else, elif
"""

"""
Estrutura condicional if, em C

if(idade < 18){
    printf("Menor de idade");
}
"""

idade = 18

if idade < 18:  # "Se" idade for menor que 18.
    print('Menor de idade')
# elfi pode se ter varios dentro do bloco já if e else so se pode ter um de cada no bloco.
elif idade == 18:
    print('Tem 18 anos')
else:
    print('Maior de idade')
