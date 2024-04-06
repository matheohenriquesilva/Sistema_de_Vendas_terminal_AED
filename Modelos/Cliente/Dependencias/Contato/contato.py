class Contato:
    def __init__(self, tipo, dado):
        self.__tipo = tipo
        self.__dado = dado

    def __str__(self):
        return f"\tx.[{self.__tipo}]: |> {self.__dado} <|"

    def validar_contato(self, tipo):
        if tipo == "email":
            return True
        elif tipo == "telefone":
            return True
        elif tipo == "instagram":
            return True
        elif tipo == "facebook":
            return True
        else:
            return False

    def set_tipo(self, novo_tipo):
        self.__tipo = novo_tipo
        return True

    def get_tipo(self):
        return self.__tipo

    def set_dado(self, novo_dado):
        self.__dado = novo_dado
        return True

    def get_dado(self):
        return self.__dado
