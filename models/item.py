from abc import ABC, abstractmethod

#Classe abstrata Item, que serve como base para Servico

class Item(ABC):

    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, valor):
        if not valor.strip():
            raise ValueError(
                "A descrição não pode ser vazia."
            )

        self._descricao = valor.strip()

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        if valor < 0:
            raise ValueError(
                "O valor não pode ser negativo."
            )

        self._valor = valor

    @abstractmethod
    def calcular_valor(self):
        pass