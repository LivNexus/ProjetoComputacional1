from .item import Item


class Servico(Item):

    def calcular_valor(self):
        return self.valor