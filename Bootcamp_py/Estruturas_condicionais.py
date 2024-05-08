"""
  A estrutura condicional permite o desvio de fluxo de controle, quando 
  determinadas expressoes lógicas são atendidas.

if - Para criar uma estruturaa condicional semples, composta por um 
único desvio, podemos utilizar a palavra reservada if. O comando irá testar
a expressão lógica, e em caso de retorno verdadeiro as ações presentes no bloco de 
codigo do if serão executadas.

saldo = 2000
saque = float(input("Informe o valor do saque! "))

if saldo >= saque:
    print("Realizando saque!")

if saldo < saque:
    print("Saldo insuficiente!")

if/else - Para criar uma estrutura condicional com dois desvios, podemos
utilizar as palavras reservadas if e else. como sabemos se a expressão lógica testada 
if for verdadeira, então o bloco de codigo do if sera executado. caso contrario o bloco
de codigo do else será executado.

saldo = 2000
saque = float(input("Informe o valor do saque! "))

if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")

if/elif/else - Em alguns cenarios queremos mais de dois desvios, para isso 
podemos utilizar a palavra reservada elif. O elif é composto por uma nova expressão
lógica, que será testada e caso retorne verdadeiramente o bloco de código do elif será executado.
Não existe um numero maximo de elifs que podemos utilizar, porém evite criar grandes estruturas condicionais, 
pois elas aumentam a complexidade do código.

opcao = int(input("informe uma opção: [1] Sacar \n[2] Extrato: "))
saldo = 2000

if opcao == 1:
    saque = float(input("Informe a quantia para o saque!"))
    if saldo >= saque:
        print("Realizando Saque...")
    else:
        print("saldo insuficiente")

if opcao == 2:
    print("Exibindo extrato...")
else:
    print("Opção invalida")


"""
MAIOR_IDADE = 18
IDADE_ESPECIAL = 12
idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Ainda não pode tirar a CNH.")

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer as aulas teoricas, mas não pode fazer as aulas praticas")
else:
    print("Ainda não pode tirar a CNH.")
