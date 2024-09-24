class BombaCombustivel:
    def __init__(self, valor_litro, quantidade_disponivel):
        self.__valor_litro = valor_litro  
        self.__quantidade_disponivel = quantidade_disponivel  

    def obter_valor_litro(self):
        return self.__valor_litro  

    def definir_valor_litro(self, valor):
        if valor > 0:
            self.__valor_litro = valor 
    
    def obter_quantidade_disponivel(self):
        return self.__quantidade_disponivel 

    def definir_quantidade_disponivel(self, quantidade):
        if quantidade >= 0:
            self.__quantidade_disponivel = quantidade  

    def abastecer_por_valor(self, valor):
        if valor <= 0:
            return -1  
        litros = valor / self.__valor_litro
        if litros > self.__quantidade_disponivel:
            return -1  
        self.__quantidade_disponivel -= litros
        return litros

    def abastecer_por_litro(self, litros):
        if litros <= 0 or litros > self.__quantidade_disponivel:
            return -1  
        valor = litros * self.__valor_litro
        self.__quantidade_disponivel -= litros
        return valor
