from abc import ABC, abstractmethod

#Classe abstrata Equipamento, que serve como base para Computador e Celular

class Equipamento(ABC):

    def __init__(self, id, marca, modelo, defeito):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.defeito = defeito

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        if valor <= 0:
            raise ValueError("O ID deve ser positivo.")

        self._id = valor

    
    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, valor):
        if not valor or not valor.strip():
            raise ValueError("A marca não pode ser vazia.")

        self._marca = valor.strip()

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, valor):
        if not valor or not valor.strip():
            raise ValueError("O modelo não pode ser vazio.")

        self._modelo = valor.strip()

    @property
    def numero_serie(self):
        return self._numero_serie

    @numero_serie.setter
    def numero_serie(self, valor):
        if not valor or not valor.strip():
            raise ValueError(
                "O número de série não pode ser vazio."
            )

        self._numero_serie = valor.strip()

    @property
    def defeito(self):
        return self._defeito

    @defeito.setter
    def defeito(self, valor):
        if not valor or not valor.strip():
            raise ValueError("O defeito não pode ser vazio.")

        self._defeito = valor.strip()

    @abstractmethod
    def descricao(self):
        pass