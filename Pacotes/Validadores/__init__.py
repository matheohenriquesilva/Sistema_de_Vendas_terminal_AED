from Pacotes.Mensagens import mensagem_caractere_invalido

# (Função que filtra só os valores INT.)
def leia_int(msg):
    while True:
        try:
            numero = int(input(msg))
        except (TypeError, ValueError):
            mensagem_caractere_invalido()
            continue
        else:
            return numero

# (Função que filtra só os valores FLOAT.)
def leia_float(msg):
    while True:
        try:
            numero = float(input(msg))
        except (ValueError, TypeError):
            mensagem_caractere_invalido()
            continue
        else:
            return numero
