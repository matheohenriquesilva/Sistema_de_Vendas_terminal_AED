from Modelos.Produto.produto import Produto
from Modelos.Produto.dao_produto import Dao_produto
from Pacotes.Validadores import leia_int, leia_float
from Pacotes.Mensagens import *

class Sessao_produto:
    def __init__(self):
        self.__dao = Dao_produto()
        self.__produto = Produto

    def __cadastrar(self):
        while True:
            print("Informe os dados do produto:")
            codigo0 = input("Digite o CÓDIGO do produto: ")
            if self.__dao.buscar_por_codigo(codigo0) is None:
                descricao0 = input("Digite a DESCRIÇÃO do produto: ")
                valor0 = leia_float("Digite o VALOR do produto: R$")
                produto0 = self.__produto(codigo=codigo0, descricao=descricao0, valor=valor0)
                self.__dao.salvar_produto(produto0)
                mensagem_cadastro_feito()
                break
            else:
                mensagem_codigo_existente()
                op = input("Clique apenas em ENTER para buscar por outro CÓDIGO:||> ")
                if len(op) > 0:
                    break

    def __buscar_por_codigo(self):
        lista_todos = self.__dao.todos_produtos()
        if len(lista_todos) > 0:
            while True:
                codigo0 = input("Digite o CÓDIGO: ")
                produto = self.__dao.buscar_por_codigo(codigo0)
                if produto is None:
                    mensagem_nenhum_item()
                else:
                    print('- ' * 20)
                    print(produto)
                    print('- ' * 20)
                op = input("Clique apenas em ENTER para buscar por outro CÓDIGO:||> ")
                if len(op) > 0:
                    break
        else:
            mensagem_nenhum_item()

    def __listar_todos(self):
        lista_todos = self.__dao.todos_produtos()
        if len(lista_todos) > 0:
            for produto in lista_todos:
                print(produto)
                print("- " * 20)
        else:
            mensagem_nenhum_item()

    def __apagar(self):
        lista_todos = self.__dao.todos_produtos()
        if len(lista_todos) > 0:
            while True:
                codigo0 = input("Digite o CÓDIGO para EXCLUIR: ")
                produto = self.__dao.buscar_por_codigo(codigo0)
                if produto is None:
                    mensagem_nenhum_item()
                    op = input("Clique apenas em ENTER para buscar novamente:||> ")
                    if len(op) > 0:
                        break
                else:
                    print(f"Tem certeza que deseja APAGAR o produto: {produto}?")
                    op = input("Clique apenas em ENTER para COMFIRMAR:||> ")
                    if len(op) == 0:
                        self.__dao.deletar_produto(produto)
                        print("PRODUTO EXCLUÍDO COM SUCESSO!")
                    else:
                        print("VOCÊ CANCELOU A AÇÃO!\nPRODUTO NÂO DELETADO!")
                    break
        else:
            mensagem_nenhum_item()

    def get_lista_produtos(self):
        return self.__dao.todos_produtos()

    def get_produto(self, codigo):
        return self.__dao.buscar_por_codigo(codigo)

    def __menu_produto(self):
        print(f"{' Sessão do PRODUTO ':|^40}")
        print("1 - CADASTRAR:")
        print("2 - BUSCAR POR CÓDIGO:")
        print("3 - LISTAR TODOS:")
        print("4 - EXCLUIR PRODUTO:")
        print("0 - SAIR:")

    def __encerrar(self):
        from time import sleep
        sleep(0.7)
        msg_saindo = "\033[34mSAINDO DA SESSÃO PRODUTO!\033[m"
        print(f"{msg_saindo:>50}")

    def iniciar(self):
        while True:
            self.__menu_produto()
            opcao = leia_int("Selecione uma opção:|> ")
            if opcao == 0:
                self.__encerrar()
                break
            elif opcao == 1:
                self.__cadastrar()
            elif opcao == 2:
                self.__buscar_por_codigo()
            elif opcao == 3:
                self.__listar_todos()
            elif opcao == 4:
                self.__apagar()
            else:
                mensagem_opcao_invalida()
