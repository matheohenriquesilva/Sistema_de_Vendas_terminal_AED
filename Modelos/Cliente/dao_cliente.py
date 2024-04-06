class Dao_cliente:
    def __init__(self):
        self.__banco_dados_clientes = []

    def salvar_novo_cliente(self, novo_cliente):
        if self.buscar_cliente_cpf(novo_cliente.get_cpf()) == None:
            self.__banco_dados_clientes.append(novo_cliente)
            return True
        return False

    def buscar_cliente_cpf(self, cpf):
        for cliente in self.__banco_dados_clientes:
            if cliente.get_cpf() == cpf:
                return cliente
        return None

    def listar_clientes(self):
        return self.__banco_dados_clientes.copy()

    def remover_cliente(self, cliente):
        self.__banco_dados_clientes.remove(cliente)
        return True
