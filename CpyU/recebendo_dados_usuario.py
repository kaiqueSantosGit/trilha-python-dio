"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo string

Em python, string é tudo o que estiver entre:
- aspas simples;
- aspasduplas;
- aspas simples triplas;
- aspas duplas triplas;
"""
#entrada de dados
# print('qual seu nome')
# nome = input() # Significa -> Entrada

nome = input('Qual seu nome?') #forma de se fazer com menos linhas de codigo

# Exemplo de print 'antigo' 2.x
# print('Seja bem vindo(a) %s' % nome)

# Exemplo de print 'moderno' 3.x
#print('Seja Bem-vindo(a) {0}' .format(nome))

# Exemplo mais 'atual' 3.7
print(f'Seja Bem-vindo(a) {nome} ')

# print('Qual sua idade')
# idade = input()

idade = int(input('Qual sua idade?'))  #forma de se fazer com menos linhas de codigo

# Exemplo de print 'mais' atual 3.7
print(f' {nome} tem {idade} anos')

"""
int(idade) -> cast
Cast é a 'conversão' de um tipo de dado para outro
"""
print(f' {nome} nasceu em {2023 - idade}')

print(f'aula concluida com sucesso {nome}')