from .equipamento import Equipamento

class Computador(Equipamento):
    def __init__(self, id, marca, modelo, defeito, tipo, processador):
        super().__init__(id, marca, modelo, defeito)
        self.tipo = tipo
        self.processador = processador

    @property
    def processador(self):
        return self._processador

    @processador.setter
    def processador(self, valor):
        if not valor or not valor.strip():
            raise ValueError(
                "O processador não pode ser vazio."
            )

        self._processador = valor.strip()

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        if not valor or not valor.strip():
            raise ValueError(
                "O tipo não pode ser vazio."
            )

        self._tipo = valor.strip()

    def descricao(self):
        return (
            f"Computador {self.marca} {self.modelo} | "
            f"Processador: {self.processador} | "
            f"Tipo: {self.tipo}"
        )