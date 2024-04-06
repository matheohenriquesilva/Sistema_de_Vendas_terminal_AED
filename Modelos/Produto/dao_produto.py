class Dao_produto:
    def __init__(self):
        self.__banco_dados_produto = list()

    def buscar_por_codigo(self, codigo):
        lista_produtos = self.todos_produtos()
        for produto in lista_produtos:
            if produto.get_codigo() == codigo:
                return produto
        return None

    def salvar_produto(self, produto):
        self.__banco_dados_produto.append(produto)
        return True

    def todos_produtos(self):
        return self.__banco_dados_produto.copy()

    def deletar_produto(self, produto):
        self.__banco_dados_produto.remove(produto)
        return True
