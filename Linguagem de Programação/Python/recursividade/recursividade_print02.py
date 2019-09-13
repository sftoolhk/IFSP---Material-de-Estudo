def fatorial(n):
    
    # Caso base
    if n == 0:
        return 1
    
    
    # Caso recursivo
    else:
        return (n * fatorial (n - 1))


# Função principal
if __name__ == "__main__":
    # Entrada de dados
    valor = int(input("Informe o valor:"))

    #Chama a função para calcular o fatorial
    print("Fatorial de %d: %d" %(valor, fatorial(valor)))