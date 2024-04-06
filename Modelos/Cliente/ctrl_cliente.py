from Modelos.Cliente.dao_cliente import Dao_cliente
from Modelos.Cliente.cliente import Cliente
from Modelos.Cliente.Dependencias.Endereco.endereco import Endereco
from Modelos.Cliente.Dependencias.Contato.contato import Contato
from Pacotes.Validadores import leia_int
from Pacotes.Mensagens import *

class Sessao_cliente:
    def __init__(self):
        self.__dao = Dao_cliente()
        self.__cliente = Cliente
        self.__endereco = Endereco
        self.__contato = Contato

    def __cadastrar(self):
        while True:
            print("Informe os dados do cliente para o cadastro:")
            cpf0 = input("Digite seu CPF_________: ")
            if self.__dao.buscar_cliente_cpf(cpf0) == None:#Verifica se o CPF ainda não foi cadastrado.
                nome0 = input("Digite seu NOME________: ")
                print("Informe o dados do endereço do cliente:")
                cep0 = input("Digite seu CEP_________: ")
                num_casa0 = input("Digite o Nº da casa____: ")
                estado0 = input("Digite o UF____________: ")
                op1 = input("Clique apenas em ENTER para detalhar endereço:||> ")#Usuário escolhe se deseja ou não detalhar endereço.
                rua0 = None
                bairro0 = None
                cidade0 = None
                if len(op1) == 0:
                    rua0 = input("Digite sua RUA_________: ")
                    bairro0 = input("Digite seu BAIRRO______: ")
                    cidade0 = input("Digite sua CIDADE______: ")
                endereco0 = self.__endereco(cep=cep0, num_casa=num_casa0, estado=estado0, rua=rua0, bairro=bairro0, cidade=cidade0)
                cliente0 = self.__cliente(nome=nome0, cpf=cpf0, endereco=endereco0)
                while True:
                    op2 = input("Clique apenas em ENTER para adicionar contato ao cliente:||> ")#Usuário escolhe se deseja adicionar contatos.
                    if len(op2) == 0:
                        print("Informe os dados de contato do cliente:")
                        print("'EMAIL', 'TELEFONE', 'INSTAGRAM', 'FACEBOOK'.")
                        while True:
                            tipo0 = input("Digite um dos tipos de contatos listados a cima: ").lower()#Usuário escolhe que tipo de contato quer adiconar.
                            contato0 = self.__contato(tipo=tipo0, dado="")
                            if contato0.validar_contato(tipo0):#Verifica se o tipo de contato é válido.
                                dado0 = input("Digite o contato: ")
                                contato0 = self.__contato(tipo=tipo0, dado=dado0)
                                if cliente0.set_contato(contato0):
                                    break
                            else:
                                mensagem_dado_invalido()
                    else:
                        break
                if self.__dao.salvar_novo_cliente(cliente0):
                    mensagem_cadastro_feito()
                    break
                mensagem_erro_inesperado()
            else:
                mensagem_cpf_existente()
            op3 = input("Clique apenas em ENTER para buscar por outro CPF:||> ")
            if len(op3) > 0:
                break

    def __buscar_por_cpf(self):
        todos_clientes = self.__dao.listar_clientes()
        if len(todos_clientes) > 0:
            while True:
                cpf = input("DIGITE O CPF PARA A BUSCA:|> ")
                if self.__dao.buscar_cliente_cpf(cpf) == None:
                    mensagem_cpf_nao_existe()
                else:
                    cliente = self.__dao.buscar_cliente_cpf(cpf)
                    print("- " * 20)
                    print(cliente)
                    cliente.imprimir_contatos()
                    print("- " * 20)
                op = input("Clique apenas em ENTER para buscar por outro CPF:||> ")
                if len(op) > 0:
                    break
        else:
            mensagem_nenhum_item()

    def __listar_todos(self):
        todos_clientes = self.__dao.listar_clientes()
        if len(todos_clientes) > 0:
            for cliente in todos_clientes:
                print("- " * 20)
                print(cliente)
                cliente.imprimir_contatos()
                print("- " * 20)
        else:
            mensagem_nenhum_item()

    def __listar_por_estado(self):
        todos_clientes = self.__dao.listar_clientes()
        if len(todos_clientes) > 0:
            temp_estados = list()
            for cliente0 in todos_clientes:
                estado0 = cliente0.get_endereco().get_estado().lower()
                if estado0 not in temp_estados:
                    temp_estados.append(estado0)
            for estado1 in temp_estados:
                mensagem_print_estado(estado1)
                for cliente1 in todos_clientes:
                    estado_aux = cliente1.get_endereco().get_estado().lower()
                    if estado1 == estado_aux:
                        print("- " * 20)
                        print(cliente1)
                        cliente1.imprimir_contatos()
        else:
            mensagem_nenhum_item()

    def __detalhar_endereco(self):
        todos_clientes = self.__dao.listar_clientes()
        if len(todos_clientes) > 0:
            while True:
                cpf = input("DIGITE O CPF PARA A BUSCA:|> ")
                if self.__dao.buscar_cliente_cpf(cpf) == None:
                    mensagem_cpf_nao_existe()
                else:
                    cliente0 = self.__dao.buscar_cliente_cpf(cpf)
                    print(f"Cliente {cliente0.get_nome().upper()} encontrado!!!")
                    endereco0 = cliente0.get_endereco()
                    if endereco0.get_cidade() is None:
                        rua0 = input("Digite sua RUA_________: ")
                        endereco0.set_rua(rua0)
                        bairro0 = input("Digite seu BAIRRO______: ")
                        endereco0.set_bairro(bairro0)
                        cidade0 = input("Digite sua CIDADE______: ")
                        endereco0.set_cidade(cidade0)
                        print("Endereço detalhado com sucesso!")
                    else:
                        print("Cliente já está com o endereço detalhado!")
                break
        else:
            mensagem_nenhum_item()

    def __adiconar_contato(self):
        todos_clientes = self.__dao.listar_clientes()
        if len(todos_clientes) > 0:
            while True:
                cpf = input("DIGITE O CPF PARA A BUSCA:|> ")
                if self.__dao.buscar_cliente_cpf(cpf) is None:
                    mensagem_nenhum_item()
                    break
                else:
                    cliente0 = self.__dao.buscar_cliente_cpf(cpf)
                    print(f"Cliente {cliente0.get_nome().upper()} encontrado!!!")
                    while True:
                        print("Informe os dados de contato do cliente:")
                        print("'EMAIL', 'TELEFONE', 'INSTAGRAM', 'FACEBOOK'.")
                        tipo0 = input("Digite um dos tipos de contatos listados a cima: ").lower()
                        contato0 = self.__contato(tipo=tipo0, dado="")
                        if contato0.validar_contato(tipo0):
                            dado0 = input("Digite o contato: ")
                            contato0 = self.__contato(tipo=tipo0, dado=dado0)
                            if cliente0.set_contato(contato0):
                                break
                        else:
                            mensagem_dado_invalido()
                            break
                op2 = input("Clique apenas em ENTER para adicionar contato ao cliente:||> ")
                if len(op2) > 0:
                    break
        else:
            mensagem_nenhum_item()

    def __excluir(self):
        todos_clientes = self.__dao.listar_clientes()
        if len(todos_clientes) > 0:
            while True:
                cpf = input("DIGITE O CPF PARA A BUSCA:|> ")
                cliente = self.__dao.buscar_cliente_cpf(cpf)
                if cliente is None:
                    mensagem_cpf_nao_existe()
                    break
                else:
                    print(f"TEM CERTEZA QUE DESEJA EXCLUIR O CLIENTE: {cliente.get_nome()}")
                    op2 = input("Clique apenas em ENTER para excluir esse cliente:||> ")
                    if len(op2) == 0:
                        self.__dao.remover_cliente(cliente)
                        print("CLIENTE EXCLUÍDO COM SECESSO.")
                        break
                    else:
                        print("VOCÊ CANCELOU A OPERAÇÃO.")
        else:
            mensagem_nenhum_item()

    def get_cliente(self, cpf=None):
        lista_todos = self.__dao.listar_clientes()
        if len(lista_todos) > 0:
            return self.__dao.buscar_cliente_cpf(cpf)
        else:
            return False

    def __menu_cliente(self):
        print(f"{' Sessão do CLIENTE ':|^40}")
        print("\t1 - CADASTRAR:")
        print("\t2 - BUSCAR POR CPF:")
        print("\t3 - LISTAR TODOS:")
        print("\t4 - LISTAR TODOS POR ESTADO:")
        print("\t5 - ADICIONAR DETALHES NO ENDEREÇO:")
        print("\t6 - ADICIONAR CONTATO:")
        print("\t7 - EXCLUIR CLIENTE:")
        print("\t0 - SAIR:")

    def __encerrar(self):
        from time import sleep
        sleep(0.7)
        msg_saindo = "\033[34mSAINDO DA SESSÃO CLIENTE!\033[m"
        print(f"{msg_saindo:>50}")

    def iniciar(self):
        while True:
            self.__menu_cliente()
            opcao = leia_int("Selecione uma opção:|> ")
            if opcao == 0:
                self.__encerrar()
                break
            elif opcao == 1:
                self.__cadastrar()
            elif opcao == 2:
                self.__buscar_por_cpf()
            elif opcao == 3:
                self.__listar_todos()
            elif opcao == 4:
                self.__listar_por_estado()
            elif opcao == 5:
                self.__detalhar_endereco()
            elif opcao == 6:
                self.__adiconar_contato()
            elif opcao == 7:
                self.__excluir()
            else:
                mensagem_opcao_invalida()
