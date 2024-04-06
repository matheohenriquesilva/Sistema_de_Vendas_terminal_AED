class Venda:
    def __init__(self, codigo, cliente):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__produtos = list()

    def __str__(self):
        return f"|CÓDIGO|[{self.__codigo}] - |CLIENTE|[{self.__cliente.get_nome()}] - |CPF|[{self.__cliente.get_cpf()}]\n\t|PRODUTOS|"

    def imprimir_produtos(self):
        lista_todos = self.__produtos.copy()
        if len(lista_todos) > 0:
            for produto in self.__produtos:
                print(f"\t{produto}")
        else:
            print("\tNENHUM PRODUTO CADASTRADO!")

    def total_da_venda(self):
        lista_todos = self.__produtos.copy()
        total_venda = 0
        for produto in lista_todos:
            valor0 = produto.get_valor()
            total_venda += valor0
        return total_venda

    def set_codigo(self, novo_codigo):
        self.__codigo = novo_codigo
        return True

    def get_codigo(self):
        return self.__codigo

    def set_cliente(self, novo_cliente):
        self.__cliente = novo_cliente
        return True

    def get_cliente(self):
        return self.__cliente

    def set_produto(self, novo_produto):
        self.__produtos.append(novo_produto)
        return True

    def get_produtos(self):
        return self.__produtos.copy()
