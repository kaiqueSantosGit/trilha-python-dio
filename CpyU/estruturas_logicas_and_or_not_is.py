"""
Estruturas logigas: and (e), or (ou), not (não), is (é)

Operadores  unários:
   - not;
Operadores binários:
   - and, or, is
Regras de funcionamento:
   - Para o 'and' ambos os usuarios precisam ser True
   - Para o 'or' um ou outro valor precisa ser True
   - Para o 'not' o valor do booleano é invertido, ou seja, se for True vira False e vice versa.

   if ativo and logado:
    print('Bem vindo usuario')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

"""
ativo = False
logado = False


if not ativo:
    print('você precisa ativar sua conta, cheque seu email')
else:
    print('Bem vindo usuario')
