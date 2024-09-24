from BombaCombustivel import BombaCombustivel

class BombaGasolina(BombaCombustivel):
    ADITIVO_PERCENTUAL = 0.05 

    def __init__(self, valor_litro, quantidade_disponivel):
        super().__init__(valor_litro, quantidade_disponivel)

    def abastecer_por_valor_com_aditivo(self, valor):
        if valor <= 0:
            return -1  
        valor_com_aditivo = self._BombaCombustivel__valor_litro * (1 + self.ADITIVO_PERCENTUAL)  # Acesso ao valor_litro
        litros = valor / valor_com_aditivo
        if litros > self._BombaCombustivel__quantidade_disponivel:  # Acesso à quantidade_disponível
            return -1  
        self._BombaCombustivel__quantidade_disponivel -= litros
        return litros

    def abastecer_por_litro_com_aditivo(self, litros):
        if litros <= 0 or litros > self._BombaCombustivel__quantidade_disponivel:  # Acesso à quantidade_disponível
            return -1 
        valor_com_aditivo = self._BombaCombustivel__valor_litro * (1 + self.ADITIVO_PERCENTUAL)  # Acesso ao valor_litro
        valor = litros * valor_com_aditivo
        self._BombaCombustivel__quantidade_disponivel -= litros
        return valor
