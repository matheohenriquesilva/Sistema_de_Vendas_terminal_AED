class Dao_venda:
    def __init__(self):
        self.__banco_de_dados_vendas = list()

    def salvar_venda(self, venda):
        self.__banco_de_dados_vendas.append(venda)
        return True

    def buscar_venda_codigo(self, codigo):
        todas_vendas = self.todas_vendas()
        for venda in todas_vendas:
            if venda.get_codigo() == codigo:
                return venda
        return None

    def todas_vendas(self):
        return self.__banco_de_dados_vendas.copy()

    def apagar_venda(self, venda):
        self.__banco_de_dados_vendas.remove(venda)
        return True
