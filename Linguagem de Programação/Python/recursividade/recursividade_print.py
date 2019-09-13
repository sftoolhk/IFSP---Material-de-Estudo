def Print(n):

    # Caso base
    print("Executando o caso base!")
    if n == 0:
        return 0
    
    # Caso recursivo
    else:
        print("Valor de N: ", n)
        return Print(n - 1)

if __name__ == "__main__":

    valor = int(input("Informe o valor: "))
    print()

    Print(valor)
