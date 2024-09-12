while True:
    pergunta = input("Gostaria de utilizar a calculadora? [s][n]\n").lower()
    if pergunta == "n":
        print("Ok, tchau")
        break
    elif pergunta == "s":
        try:
            n1 = float(input("Primeiro valor\n"))
            n2 = float(input("Segundo valor\n"))
            operacao = input("Escolha a operação: soma[1], subtração[2], multiplicação[3], divisão[4], potenciação[5]\n")

            operacoes = {
                "1": n1 + n2,
                "2": n1 - n2,
                "3": n1 * n2,
                "4": n1 / n2 if n2 != 0 else "Erro: divisão por zero",
                "5": n1 ** n2
            }

            resultado = operacoes.get(operacao, "Operação inválida")
            print(f"O resultado é: {resultado}")

        except ValueError:
            print("Valor inválido")
    else:
        print("Ok, tchau")
        break
