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


class BombaEtanol(BombaCombustivel):
    def __init__(self, valor_litro, quantidade_disponivel):
        super().__init__(valor_litro, quantidade_disponivel)


class BombaGasolina(BombaCombustivel):
    aditivo_percentual = 0.05 

    def __init__(self, valor_litro, quantidade_disponivel):
        super().__init__(valor_litro, quantidade_disponivel)

    def abastecer_por_valor_com_aditivo(self, valor):
        if valor <= 0:
            return -1  
        valor_com_aditivo = self._valor_litro * (1 + BombaGasolina.ADITIVO_PERCENTUAL)
        litros = valor / valor_com_aditivo
        if litros > self._quantidade_disponivel:
            return -1  
        self._quantidade_disponivel -= litros
        return litros

    def abastecer_por_litro_com_aditivo(self, litros):
        if litros <= 0 or litros > self._quantidade_disponivel:
            return -1 
        valor_com_aditivo = self._valor_litro * (1 + BombaGasolina.ADITIVO_PERCENTUAL)
        valor = litros * valor_com_aditivo
        self._quantidade_disponivel -= litros
        return valor