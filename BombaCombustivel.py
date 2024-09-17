class BombaCombustivel:
    def __init__(self, valor_litro, quantidade_disponivel):
        self._valor_litro = valor_litro
        self._quantidade_disponivel = quantidade_disponivel

    def obter_valor_litro(self):
        return self._valor_litro

    def definir_valor_litro(self, valor):
        self._valor_litro = valor

    def obter_quantidade_disponivel(self):
        return self._quantidade_disponivel

    def definir_quantidade_disponivel(self, quantidade):
        self._quantidade_disponivel = quantidade

    def abastecer_por_valor(self, valor):
        if valor <= 0:
            return -1  
        litros = valor / self._valor_litro
        if litros > self._quantidade_disponivel:
            return -1  
        self._quantidade_disponivel -= litros
        return litros

    def abastecer_por_litro(self, litros):
        if litros <= 0 or litros > self._quantidade_disponivel:
            return -1  
        valor = litros * self._valor_litro
        self._quantidade_disponivel -= litros
        return valor


