from random import randint

DEBUG = False
TENTATIVAS = 6
TOTAL_RODADAS = TENTATIVAS - 1
PONTUACAO_MAXIMA = 100
MENSAGENS = {
    'DEFAULT': {
        'SAUDACAO': 'Escolhi um número entre 0 e 10. Tente adivinhar',
        'VITORIA': 'Parabéns! você acertou',
        'DERROTA': 'Que pena!! Você é um fracasso',
        'INPUT_JOGADOR': 'Digite um número entre 0 e 10: ',
        'NOVA_PARTIDA': 'Gostaria de jogar novamente? (1-Sim; 2-Não) ',
        'ENCERRAMENTO': 'Até a próxima!!!',
        'PONTUACAO': lambda pontuacao: f'A sua pontuação final é {pontuacao} pontos'
    },
    'ERRO': {
        'TENTATIVA_INVALIDA': 'ERRO: São permitidos apenas números inteiros entre 0 e 10',
        'NOVA_PARTIDA_INVALIDA': 'ERRO: São permitidas apenas as opções: 1-Sim ou 2-Não',
    }
}


def mensagem_tela(mensagem, pontuacao=None, mensagem_resultado=None):
    TAMANHO_LINHA = 70
    ALINHAMENTO = f'^{TAMANHO_LINHA}'
    print(f'{"-" * TAMANHO_LINHA}')
    print(f'{mensagem.upper():{ALINHAMENTO}}')
    if pontuacao is not None:
        print(f'{mensagem_resultado.upper():{ALINHAMENTO}}')
    print(f'{"-" * TAMANHO_LINHA}')


def get_input_jogador(mensagem):
    return str(input(mensagem))


def valida_tentativa_jogador(numero):
    try:
        int(numero)
    except ValueError:
        return False
    return int(numero) in range(11)


def valida_opcao_jogador(input):
    try:
        int(input)
    except ValueError:
        return False
    return int(input) in range(3)


def nova_partida(input):
    # 1 - Sim: 2 - Não
    return input == '1'


def verifica_acerto(numero_jogador, numero_computador):
    return int(numero_jogador) == numero_computador


