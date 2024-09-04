
from bomba_combustivel import BombaEtanol, BombaGasolina

def exibir_menu():
    print("Posto")
    print("1 - Abastecer Etanol por Valor")
    print("2 - Abastecer Etanol por Litro")
    print("3 - Abastecer Gasolina por Valor")
    print("4 - Abastecer Gasolina por Litro")
    print("5 - Abastecer Gasolina com Aditivo por Valor")
    print("6 - Abastecer Gasolina com Aditivo por Litro")
    print("7 - Sair")

def main():
    bomba1 = BombaEtanol(valor_litro=3, quantidade_disponivel=1000)
    bomba2 = BombaGasolina(valor_litro=4, quantidade_disponivel=1000)
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            valor = float(input("Digite o valor para abastecer com etanol: "))
            litros = bomba1.abastecer_por_valor(valor)
            if litros <= 0:
                print("Quantidade insuficiente na bomba ou valor inválido.")
            else:
                print(f"Abastecido {litros} litros de etanol.")

        elif opcao == '2':
            litros = float(input("Digite a quantidade de litros para abastecer com etanol: "))
            valor = bomba1.abastecer_por_litro(litros)
            if valor <= 0:
                print("Quantidade insuficiente na bomba ou quantidade de litros inválida.")
            else:
                print(f"Valor a pagar: R${valor}")

        elif opcao == '3':
            valor = float(input("Digite o valor para abastecer com gasolina: "))
            litros = bomba2.abastecer_por_valor(valor)
            if litros <= 0:
                print("Quantidade insuficiente na bomba ou valor inválido.")
            else:
                print(f"Abastecido {litros} litros de gasolina.")

        elif opcao == '4':
            litros = float(input("Digite a quantidade de litros para abastecer com gasolina: "))
            valor = bomba2.abastecer_por_litro(litros)
            if valor <= 0:
                print("Quantidade insuficiente na bomba ou quantidade de litros inválida.")
            else:
                print(f"Valor a pagar: R${valor}")

        elif opcao == '5':
            valor = float(input("Digite o valor para abastecer com gasolina aditivada: "))
            litros = bomba2.abastecer_por_valor_com_aditivo(valor)
            if litros <= 0:
                print("Quantidade insuficiente na bomba ou valor inválido.")
            else:
                print(f"Abastecido {litros} litros de gasolina aditivada.")

        elif opcao == '6':
            litros = float(input("Digite a quantidade de litros para abastecer com gasolina aditivada: "))
            valor = bomba2.abastecer_por_litro_com_aditivo(litros)
            if valor <= 0:
                print("Quantidade insuficiente na bomba ou quantidade de litros inválida.")
            else:
                print(f"Valor a pagar: R${valor}")

        elif opcao == '7':
            print("Saindo")
            break

        else:
            print("Opção inválida !!!")
            print("Tente novamente")
main()
