def mensagem_caractere_invalido():
    msg_erro = "\033[31mCARACTERE INVÁLIDO!\033[m"
    return print(f"{msg_erro:>50}")

def mensagem_opcao_invalida():
    msg_erro = "\033[31mOPÇÃO NÃO EXISTE!\033[m"
    return print(f"{msg_erro:>50}")

def mensagem_dado_invalido():
    msg_erro = "\033[31mDADO INVÁLIDO!\033[m"
    return print(f"{msg_erro:>50}")

def mensagem_nenhum_item():
    msg_erro = "\033[31mNENHUM ITEM CADASTRADO!\033[m"
    return print(f"{msg_erro:>50}")

def mensagem_cpf_existente():
    msg_erro = "\033[31mCPF JÁ CADASTRADO!\033[m"
    return print(f"{msg_erro:>50}")

def mensagem_cadastro_feito():
    msg = "\033[31mCADASTRADO FEITO COM SUCESSO!\033[m"
    return print(f"{msg:>50}")

def mensagem_erro_inesperado():
    msg_erro = "\033[31mUM ERRO INESPERADO ACONTECEU!\033[m"
    return print(f"{msg_erro:>50}")

def mensagem_cpf_nao_existe():
    msg_erro = "\033[31mESSE CPF NÃO ENCONTRADO NO SISTEMA!\033[m"
    return print(f"{msg_erro:>50}")

def mensagem_print_estado(estado):
    novo_estado = estado.upper()
    msg = f"\033[33m {novo_estado} \033[m"
    return print(f"{msg:-^50}")

def mensagem_codigo_existente():
    msg_erro = "\033[31mCÓDIGO JÁ CADASTRADO!\033[m"
    return print(f"{msg_erro:>50}")
