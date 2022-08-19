from produto import Produto
from usuario import Usuario


class Funcionalidades:
    # 1 - Funcionalidade - Menu do Sistema
    @staticmethod
    def menu_sistema():
        print("\n################################################")
        print("############# SISTEMA - MENU ####################")
        print("1 - Efetuar Login\t 2 - Estoque\t 3 - Consulta Estoque")
        opcao_menu = input("Digite sua opção: ")
        return opcao_menu

    # 2 - Funcionalidade - Login
    @staticmethod
    def login_sistema():
        print("\n################################################")
        print("########### LOGON NO SISTEMA ###################")
        tentativas = 3

        # Efetua tentativas de Login
        while tentativas > 0:
            userlogin = input("Informe seu login: ")
            senhalogin = input("Digite seu password: ")

            # Istancia objeto Usuario
            user = Usuario(userlogin, senhalogin)

            # Verifica se usuario e Adm
            if not user.valida_loginAdm():
                tentativas -= 1
                print("Usuario e Senha invalidos! Tente Novamente...\n")
            else:
                sucesso = 1


            if tentativas == 0:
                sucesso = 0
            # Retorna se o Login foi realizado com Sucesso
            return sucesso

    # 3 - Funcionalidade - Cadastro de produtos
    @staticmethod
    def cadastro_produto():
        print("\n################################################")
        print("########### CADASTRO DE PRODUTOS ###############")

        # lista vazia que recebe os produtos
        lista_produto = []
        # Limite de cadastro por vez
        qtde_limite = 3
        while qtde_limite > 0:
            nm_produto = input("Informe nome do Produto: ")
            vl_preço = float(input("Informe o preço do Produto: "))
            ds_genero = input("informe o genero em idade: ")
            qtde_cad = input("digite a quantidade cadastrado na loja: ")

            # Instancia um objeto
            product = Produto(nm_produto, ds_genero, qtde_cad, vl_preço)
            lista_produto.append(product)
            print(product)

            # Pergunta de deseja cadastrar um novo produto
            resp = input("Cadastar novo Produto?[S ou N]: ")

            if resp.capitalize() == "S":
                qtde_limite -= 1
            else:
                break
        # Informa o usuario que exedeu o limite de cadastro
        if qtde_limite == 0:
            print("O limite de cadastro de produtos foi atingido! Retorne ao sistema.")

        # Retorna a lista de produtos cadatrados
        return lista_produto


    # 4 - Funcionalidade - Consulta Estoque
    @staticmethod
    def consulta_estoque(lista_produto):
        print("############################################################")
        print("##################### ESTOQUE DA LOJA ######################")
        print("####| Produto                | Genero | Quantidade | Preço |####")
        for prod in lista_produto:
            prod.consulta_produto()