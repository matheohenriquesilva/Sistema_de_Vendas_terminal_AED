from Modelos.Venda.dao_venda import Dao_venda
from Modelos.Venda.venda import Venda
from Pacotes.Validadores import leia_int
from Pacotes.Mensagens import *

class Sessao_venda:
    def __init__(self, controlador_cliente, controlador_produto):
        self.__controlador_cliente = controlador_cliente
        self.__controlador_produto = controlador_produto
        self.__dao = Dao_venda()

    def __cadastrar(self):
        while True:
            if self.__controlador_cliente.get_cliente() is False:#Verifica se existe algum cliente cadastrado no sistema. 01
                mensagem_nenhum_item()
            else:#01
                cpf = input("Digite o CPF do cliente para associar a sua venda: ")
                if self.__controlador_cliente.get_cliente(cpf):#Verifica se existe algum cliente com esse CPF. 02
                    cliente0 = self.__controlador_cliente.get_cliente(cpf)
                    print(f"CLIENTE SELECIONADO: {cliente0.get_nome()}")
                    while True:
                        codigo0 = input("Digite o CÓDIGO da venda: ")
                        if self.__dao.buscar_venda_codigo(codigo0) is not None:#Verifica se existe alguma venda com esse CODIGO. 03
                            mensagem_codigo_existente()
                            op = input("Clique apenas em ENTER para verificar o codiggo novamente:||> ")
                            if len(op) > 0:
                                break
                        else:#03
                            venda0 = Venda(codigo=codigo0, cliente=cliente0)
                            lista_produtos = self.__controlador_produto.get_lista_produtos()
                            if len(lista_produtos) > 0:
                                venda = self.__adicionar_produtos_vendas(venda0)
                                print(venda)
                                venda.imprimir_produtos()
                                self.__dao.salvar_venda(venda)
                                mensagem_cadastro_feito()
                            else:
                                print(f"{'POR FAVOR CADASTRE ALGUM PRODUTO NA SESSÃO PRODUTO!!!':>50}")
                            break
                else:#02
                    mensagem_cpf_nao_existe()
            break

    def __buscar_por_codigo(self):
        lista_todos = self.__dao.todas_vendas()
        if len(lista_todos) > 0:
            while True:
                codigo = input("Digite o codigo da venda para buscar: ")
                venda = self.__dao.buscar_venda_codigo(codigo)
                if venda:
                    print("VENDA ENCONTRADA!")
                    print(venda)
                    venda.imprimir_produtos()
                else:
                    print("NENUMA VENDA CADASTRADA COM ESSE CODIGO!!!")
                op = input("Digite apenas em ENTER para pesquisar novamente: ")
                if len(op) > 0:
                    break
        else:
            mensagem_nenhum_item()

    def __listar_todos(self):
        lista_todos = self.__dao.todas_vendas()
        if len(lista_todos) > 0:
            for venda in lista_todos:
                print('- ' * 20)
                print(venda)
                venda.imprimir_produtos()
                print('- ' * 20)
        else:
            mensagem_nenhum_item()

    def __listar_por_cliente(self):
        lista_todos = self.__dao.todas_vendas()
        if len(lista_todos) > 0:
            while True:
                cpf = input("Digite o CPF do cliente para listar a vendas associadas: ")
                cliente0 = self.__controlador_cliente.get_cliente(cpf)
                if cliente0:
                    vendas_temp = list()
                    for venda in lista_todos:
                        if venda.get_cliente() == cliente0:
                            vendas_temp.append(venda)
                    if len(vendas_temp) > 0:
                        for venda in vendas_temp:
                            print(venda)
                            venda.imprimir_produtos()
                            print(" - " * 20)
                    else:
                        print(f"NENHUMA VENDA ASSOCIADA AO CLIENTE: {cliente0.get_nome()}")
                else:
                    mensagem_cpf_nao_existe()
                op = input("Digite apenas em ENTER para pesquisar novamente: ")
                if len(op) > 0:
                    break
        else:
            mensagem_nenhum_item()

    def __listar_por_estado(self):
        lista_todos = self.__dao.todas_vendas()
        if len(lista_todos) > 0:
            clientes_temp = list()
            for venda in lista_todos:
                cliente0 = venda.get_cliente()
                clientes_temp.append(cliente0)
            estados_temp = list()
            for cliente0 in clientes_temp:
                estado0 = cliente0.get_endereco().get_estado().lower()
                if estado0 not in estados_temp:
                    estados_temp.append(estado0)
            for estado1 in estados_temp:
                mensagem_print_estado(estado1)
                for venda in lista_todos:
                    cliente1 = venda.get_cliente()
                    estado_aux = cliente1.get_endereco().get_estado().lower()
                    if estado1 == estado_aux:
                        print("- " * 20)
                        print(venda)
                        venda.imprimir_produtos()
        else:
            mensagem_nenhum_item()

    def __total_vendas(self):
        lista_todos = self.__dao.todas_vendas()
        tamanho_vendas = len(lista_todos)
        if tamanho_vendas > 0:
            print(f"Tem {tamanho_vendas} vendas cadastradas no sistema.")
        else:
            print(f"Tem {tamanho_vendas} vendas cadastradas no sistema.")
            mensagem_nenhum_item()

    def __total_produtos_vendido(self):
        lista_todos = self.__dao.todas_vendas()
        if len(lista_todos) > 0:
            total_produtos_vendidos = 0
            for venda in lista_todos:
                aux = venda.total_da_venda()
                total_produtos_vendidos += aux
            print('- -' * 25)
            print(f"O total do valor de produtos vendidos foi de R${total_produtos_vendidos}")
            print('- -' * 25)
        else:
            mensagem_nenhum_item()

    def __listar_valor_total_venda(self):
        lista_todos = self.__dao.todas_vendas()
        if len(lista_todos) > 0:
            while True:
                codigo = input("Digite o codigo da venda para ver o seu valor total: ")
                venda = self.__dao.buscar_venda_codigo(codigo)
                if venda:
                    print("VENDA ENCONTRADA!")
                    total_venda = venda.total_da_venda()
                    print(venda)
                    venda.imprimir_produtos()
                    print(f"O valor total dos produtos dessa venda é de R${total_venda}")
                else:
                    print("NENUMA VENDA CADASTRADA COM ESSE CODIGO!!!")
                op = input("Digite apenas em ENTER para pesquisar novamente: ")
                if len(op) > 0:
                    break
        else:
            mensagem_nenhum_item()

    def __excluir_venda(self):
        lista_todos = self.__dao.todas_vendas()
        if len(lista_todos) > 0:
            codigo0 = input("Digite o codigo da venda para EXCLUÍR: ")
            venda0 = self.__dao.buscar_venda_codigo(codigo0)
            if venda0:
                print(f"VENDA ENCONTRADA!")
                print(venda0)
                venda0.imprimir_produtos()
                op = input("Digite apenas em ENTER para apagar essa venda: ")
                if len(op) == 0:
                    self.__dao.apagar_venda(venda0)
                    print("VENDA APAGADA COM SUCESSO!")
                else:
                    print("VOCÊ CANCELOU A OPERAÇÃO!!")
            else:
                print("NENHUMA VENDA CADASTRADA COM ESSE CODIGO.")
        else:
            mensagem_nenhum_item()

    def __adicionar_produtos_vendas(self, venda0):
        cont = 0
        lista_todos = self.__controlador_produto.get_lista_produtos()
        while True:
            for venda in lista_todos:
                print(venda)
                print(' > ' * 20)
            codigo0 = input("Digite o CÓDIGO do respectivo produto para adicionar a Venda: ")
            produto0 = self.__controlador_produto.get_produto(codigo0)
            if produto0 is not None:
                venda0.set_produto(produto0)
                print(f"PRODUTO: {produto0} ADICIONADO COM SUCESSO!!!")
                cont += 1
            else:
                mensagem_nenhum_item()
                print("ESSE CÓDIGO NÃO É DE NENHUM PRODUTO LISTADO ACIMA!!!")
            if cont >= 1:
                op0 = input("Clique apenas em ENTER para adicionar um produto a venda:||> ")
                if len(op0) > 0:
                    break
        return venda0

    def __menu_vendas(self):
        print(f"{' Sessão de VENDAS ':|^40}")
        print("\t1 - CADASTRAR:")
        print("\t2 - BUSCAR POR CÓDIGO:")
        print("\t3 - LISTAR TODOS:")
        print("\t4 - LISTAR VENDAS POR CLIENTES:")
        print("\t5 - LISTAR TODAS AS VENDAS POR ESTADOS:")
        print("\t6 - TOTAL DE VENDAS NO SISTEMA:")
        print("\t7 - TOTAL DE PRODUTOS VENDIDOS:")
        print("\t8 - LISTAR VALOR TOTAL DAS VENDAS:")
        print("\t9 - EXCLUÍR VENDA:")
        print("\t0 - SAIR:")

    def __encerrar(self):
        from time import sleep
        sleep(0.7)
        msg_saindo = "\033[34mSAINDO DA SESSÃO VENDA!\033[m"
        print(f"{msg_saindo:>50}")

    def iniciar(self):
        while True:
            self.__menu_vendas()
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
                self.__listar_por_cliente()
            elif opcao == 5:
                self.__listar_por_estado()
            elif opcao == 6:
                self.__total_vendas()
            elif opcao == 7:
                self.__total_produtos_vendido()
            elif opcao == 8:
                self.__listar_valor_total_venda()
            elif opcao == 9:
                self.__excluir_venda()
            else:
                mensagem_opcao_invalida()
