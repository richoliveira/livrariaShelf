# importa classes
from usuario import Usuario
from produto import Produto
from funcionalidades import Funcionalidades as funcSis

opcao = 1

while opcao != 0:
    # Chama a Funcionalidade que cria o Menu do SIstema
    opcao = funcSis.menu_sistema()
    # Funcionalidade Login
    if opcao == "1":
        login_sucesso = funcSis.login_sistema()
        if login_sucesso == 1:
            print("Login Administrador realizado com sucesso.")
        elif login_sucesso == 0:
            print("Excedeu as tentativas de login! Tente novamente em 24 horas...")
            opcao = 0

    # 2 - Funcionalidade - Cadastro
    elif opcao == "2":
        # Chama a funcionalidade de Cadstro de produtos
        lista_produto = funcSis.cadastro_produto()

    # 3 - Funcionalidade - Consulta Estoque
    elif opcao == "3":
        funcSis.consulta_estoque(lista_produto)
