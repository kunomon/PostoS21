class BombaCombustivel:
    def __init__(self, valor_litro, quantidade_disponivel):
        self.valor_litro = valor_litro
        self.quantidade_disponivel = quantidade_disponivel

    def abastecer_por_valor(self, valor):
        litros = valor / self.valor_litro
        return litros

    def abastecer_por_litro(self, litros):
        valor = litros * self.valor_litro
        return valor


class BombaEtanol(BombaCombustivel):
    pass


class BombaGasolina(BombaCombustivel):
    aditivo_percentual= 0.05

    def abastecer_por_valor_com_aditivo(self, valor):
        valor_com_aditivo = self.valor_litro * (1 + self.ADITIVO_PERCENTUAL)
        litros = valor / valor_com_aditivo
        return litros

    def abastecer_por_litro_com_aditivo(self, litros):
        valor_com_aditivo = self.valor_litro * (1 + self.ADITIVO_PERCENTUAL)
        valor = litros * valor_com_aditivo
        return valor
