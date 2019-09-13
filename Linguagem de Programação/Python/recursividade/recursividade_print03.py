def fibonacci(n):
    # Caso base
    if n < 2:
        return n


    # Caso recursivo
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":

    # Quantidade de meses
    meses = int(input("Informe o número de meses: "))


    # Calcula o total de casais
    casais = fibonacci(meses)

    # Exibe o resultado
    print("Em %d meses haverá %d casais de coelhos..." %(meses, casais))
