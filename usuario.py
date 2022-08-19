class Usuario:
    # Metodo Contrutor
    def __init__(self, login, senha):
        # Propriedades da Classe
        self._login = login
        self._senha = senha
        self._loginAdm = "m233678"
        self._senhaAdm = "123456"

    # Metodo getter
    @property
    def login(self):
        return self._login


    @login.setter
    def login(self, novo_login):
        self._login = novo_login

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, nova_senha):
        self._senha = nova_senha

    # valida Senha Adm
    def valida_loginAdm(self):
        if self._login == self._loginAdm and self._senha == self._senhaAdm:
            return True
        else:
            return False

