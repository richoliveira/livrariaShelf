class Produto:
    def __init__(self, nomeproduto, genero, quantidade, valor=float):
        self._nomeproduto = nomeproduto
        self._quantidade = quantidade
        self._genero = genero
        self._valor = valor

    # Metodo get Nome produto
    @property
    def nomeproduto(self):
        return self._nomeproduto.title()

    # Metodo setter Nome produto
    @nomeproduto.setter
    def nomeproduto(self, novo_produto):
        self._nomeproduto = novo_produto

    def __str__(self):
        return f"Produto {self._nomeproduto} Genero +{self._genero} cadastrado com sucesso."

    def consulta_produto(self):
        print(f"####| {self._nomeproduto}                 | {self._genero}      | {self._quantidade}         | {self._valor} |####")