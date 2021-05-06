#Imports
import os

#Constantes
MSG_DADOS_INVALIDOS = "\n\nDados informados são inválidos."
MSG_VOLTAR_MENU = "Digite 's' + [ENTER] para sair ou apenas [ENTER] para voltar ao menu... "
MSG_MENU_OPCAO_INVALIDA = "\n\nOpção inválida. Tecle [ENTER] para retornar ao menu."

#Funções
def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def fibonacci(qtde):
    try:
        qtde = int(qtde)
        res = [0, 1]

        for x in range(qtde - 2):
            res.append(res[x] + res[x + 1])

        return res
    except:
        return MSG_DADOS_INVALIDOS

def calcularIMC():
    imc = [
        [0, 18.5, "MAGREZA"],
        [18.5, 24.9, "NORMAL"],
        [25, 29.9, "SOBREPESO"],
        [30, 34.9, "OBESIDADE GRAU I"],
        [35, 39.9, "OBESIDADE SEVERA GRAU II"],
        [40, 1000, "OBESIDADE MÓRBIDA GRAU III"]
    ]

    try:
        peso = input("Informe seu peso: ")
        altura = input("Informe sua altura: ")
        vIMC = float(peso) / float(altura) ** 2
        resultado = ""

        for x in imc:
            if vIMC >= x[0] and vIMC <= x[1]:
                resultado = x[2]

        return f"Seu IMC é: {round(vIMC, 2)}\nResultado: {resultado}"
    except:
        return "\n\nDados informados são inválidos."

def saidaOuMenu(tecla):
    if tecla.upper() == "S":
        limparTela()
        exit()
    else:
        menu()

def menu():
    limparTela()
    print("##########################################################################")
    print("##############################  MENU  ####################################")
    print("##########################################################################")
    print("####                                                                  ####")
    print("####                   1. Sequência de Fibonacci                      ####")
    print("####                   2. Cálculo do IMC                              ####")
    print("####                   0. Finalizar Aplicação                         ####")
    print("##########################################################################")

    opcao = int(input("\nInforme uma opção de menu: "))

    limparTela()

    if opcao == 1:
        qtde = input("Informe a quantidade de números na sequência: ")
        res = fibonacci(qtde)
        print(res)
        tecla = input(f"\n\n{MSG_VOLTAR_MENU}")
        saidaOuMenu(tecla)
    elif opcao == 2:
        res = calcularIMC()
        print(res)
        tecla = input(f"\n\n{MSG_VOLTAR_MENU}")
        saidaOuMenu(tecla)
    elif opcao == 0:
        saidaOuMenu("S")
    else:
        tecla = input(MSG_MENU_OPCAO_INVALIDA)
        saidaOuMenu(tecla)

#Aplicação
menu()