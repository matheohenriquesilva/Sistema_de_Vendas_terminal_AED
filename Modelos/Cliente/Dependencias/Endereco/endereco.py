class Endereco:
    def __init__(self, cep, num_casa, estado, rua=None, bairro=None, cidade=None):
        self.__cep = cep
        self.__num_casa = num_casa
        self.__estado = estado
        self.__rua = rua
        self.__bairro = bairro
        self.__cidade = cidade

    def __str__(self):
        parte1 = f"CEP: {self.__cep}\nNÚMEROº: {self.__num_casa}\nUF: {self.__estado}"
        parte2 = f"RUA: {self.__rua}\nBAIRRO: {self.__bairro}\nCIDADE: {self.__cidade}"
        if self.__cidade == None:
            return parte1
        else:
            string_ = f"{parte1}\n{parte2}"
            return string_

    def set_cep(self, novo_cep):
        self.__cep = novo_cep
        return True

    def get_cep(self):
        return self.__cep

    def set_num_casa(self, novo_num_casa):
        self.__num_casa = novo_num_casa
        return True

    def get_num_casa(self):
        return self.__num_casa

    def set_estado(self, novo_estado):
        self.__estado = novo_estado
        return True

    def get_estado(self):
        return self.__estado

    def set_rua(self, novo_rua):
        self.__rua = novo_rua
        return True

    def get_rua(self):
        return self.__rua

    def set_bairro(self, novo_bairro):
        self.__bairro = novo_bairro
        return True

    def get_bairro(self):
        return self.__bairro

    def set_cidade(self, novo_cidade):
        self.__cidade = novo_cidade
        return True

    def get_cidade(self):
        return self.__cidade
