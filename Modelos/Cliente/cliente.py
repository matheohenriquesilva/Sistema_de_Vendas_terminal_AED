class Cliente:
    def __init__(self, nome, cpf, endereco):
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__contatos = list()

    def __str__(self):
        return f"NOME: {self.__nome}\nCPF: {self.__cpf}\n||_ENDEREÇO_||\n{self.__endereco}\n||_CONTATOS_||"

    def imprimir_contatos(self):
        lista_contatos = self.__contatos.copy()
        if len(lista_contatos) > 0:
            for contato in lista_contatos:
                print(f"{contato}")
        else:
            print("\tNENHUM CONTATO CADASTRADO!!")

    def tem_contato(self):
        if len(self.__contatos) > 0:
            return True

    def set_nome(self, novo_nome):
        self.__nome = novo_nome
        return True

    def get_nome(self):
        return self.__nome

    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf
        return True

    def get_cpf(self):
        return self.__cpf

    def set_endereco(self, novo_endereco):
        self.__endereco = novo_endereco
        return True

    def get_endereco(self):
        return self.__endereco

    def set_contato(self, novo_contato):
        self.__contatos.append(novo_contato)
        return True

    def get_contato(self):
        return self.__contatos.copy()
