from Modelos.Cliente.ctrl_cliente import Sessao_cliente
from Modelos.Produto.ctrl_produto import Sessao_produto
from Modelos.Venda.ctrl_venda import Sessao_venda
from Pacotes.Validadores import leia_int
from Pacotes.Mensagens import mensagem_opcao_invalida

class Sistema:
    def __init__(self):
        self.__controlador_cliente = Sessao_cliente()
        self.__controlador_produto = Sessao_produto()
        self.__controlador_venda = Sessao_venda(self.__controlador_cliente, self.__controlador_produto)

    def __menu_principal(self):
        print(f"\n{' DashBoard ':=^40}")
        print("\t1 - CLIENTE:")
        print("\t2 - PRODUTO:")
        print("\t3 - VENDA:")
        print("\t0 - SAIR:")
        print("=" * 40)

    def __encerrar(self):
        from time import sleep
        opcao = input("\nClique apenas em ENTER para SAIR||> ")
        if opcao == "":
            sleep(0.7)
            msg_saindo = "\033[34mSAINDO DO PROGRAMA!\033[m"
            print(f"{msg_saindo:>50}")
            sleep(0.9)
            return True
        return False

    def iniciar(self):
        while True:
            self.__menu_principal()
            opcao = leia_int("Selecione uma opção:|> ")
            if opcao == 0:
                if self.__encerrar():
                    break
            elif opcao == 1:
                self.__controlador_cliente.iniciar()#Sessão CLIENTE.
            elif opcao == 2:
                self.__controlador_produto.iniciar()#Sessão PRODUTO.
            elif opcao == 3:
                self.__controlador_venda.iniciar()#Sessão VENDA.
            else:
                mensagem_opcao_invalida()
