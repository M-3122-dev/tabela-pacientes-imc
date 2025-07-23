def calcula_imc(peso, altura):
    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
        classificacao = "Peso normal"
    elif 25 <= imc <= 29.9:
        classificacao = "Sobrepeso"
    elif 30 <= imc <= 39.9:
        classificacao = "Obesidade"
    else:
        classificacao = "Obesidade grave"

    return imc, classificacao

def imprimir_tabela(pacientes):
    prioridade = {
        'Obesidade grave': 1,
        'Obesidade':2,
        'Sobrepeso':3,
        'Peso normal':4,
        'Abaixo do peso':5
    }

    pacientes_ordenados = sorted(pacientes, key=lambda x: (prioridade[x["classificacao"]], -x['idade']))

    print("\nTABELA DE PACIENTE (prioridade por gravidade e idade)")
    print(f"{'Nome':<20} {'Idade':<6} {'Peso':<9} {'Altura':<10} {'Classificação'}")
    print("-" * 60)

    for pessoa in pacientes_ordenados:
        print(f"{pessoa['nome']:<20} {pessoa['idade']:<6} {pessoa['peso']:<9} {pessoa['altura']:<10} {pessoa['classificacao']}")


def main():
    lista_pacientes = []

    while True:
        nome = input("Nome: ").strip().title()
        for palavra in ["da", "de", "di", "dos", "do", "a", "e"]:
            nome = nome.replace(f" {palavra.title()} ", f" {palavra} ")

        idade = int(input("Idade: "))
        peso = float(input("Peso (Kg): "))
        altura = float(input("Altura (m): "))

        imc, classificacao = calcula_imc(peso, altura)

        paciente = {
            "nome": nome,
            "idade": idade,
            "peso": peso,
            "altura": altura,
            "imc": imc,
            "classificacao": classificacao
        }

        lista_pacientes.append(paciente)

        while True:
            opcao = input("Quer continuar? [S/N]: ").strip().upper()
            if opcao in ["S", "N"]:
                break

        if opcao == "N":
            break

    imprimir_tabela(lista_pacientes)
    print("Encerrando o programa. Até a próxima!")


if __name__ == "__main__":
    main()
