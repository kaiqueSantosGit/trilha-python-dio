"""
  São operadores utilizados para comparar se os dois objetos testados o
  ocupam a mesma posição na memória

  # Exemplo
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso
# Resultado deve ser "True"
curso is not nome_curso
# Resultado deve ser "False"
saldo is limite
"""
saldo = 1000
limite = 500

print(saldo is limite)
print(saldo is not limite)
