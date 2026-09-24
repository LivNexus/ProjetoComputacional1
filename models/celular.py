from.equipamento import Equipamento

class Celular(Equipamento):
    def __init__(self, id, marca, modelo, defeito, sistema_operacional):
        super().__init__(id, marca, modelo, defeito)
        self.sistema_operacional = sistema_operacional

    @property
    def sistema_operacional(self):
        return self._sistema_operacional

    @sistema_operacional.setter
    def sistema_operacional(self, valor):
        if not valor or not valor.strip():
            raise ValueError(
                "O sistema operacional não pode ser vazio."
            )

        self._sistema_operacional = valor.strip()

    def descricao(self):
        return (
            f"Celular {self.marca} {self.modelo} | "
            f"Sistema: {self.sistema_operacional} | "
        )