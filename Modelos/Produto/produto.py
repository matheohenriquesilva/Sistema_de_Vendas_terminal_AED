class Produto:
    def __init__(self, codigo, descricao, valor):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valor = valor

    def __str__(self):
        return f"[{self.__codigo}] - {self.__descricao} - |R${self.__valor}|"

    def set_codigo(self, novo_codigo):
        self.__codigo = novo_codigo
        return True

    def get_codigo(self):
        return self.__codigo

    def set_descricao(self, nova_descricao):
        self.__descricao = nova_descricao
        return True

    def get_descricao(self):
        return self.__descricao

    def set_valor(self, novo_valor):
        self.__valor = novo_valor
        return True

    def get_valor(self):
        return self.__valor
