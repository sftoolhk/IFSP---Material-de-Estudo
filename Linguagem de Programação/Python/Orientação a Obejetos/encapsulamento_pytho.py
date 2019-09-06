# Classe Teste
class Teste(object):

    # Construtor
    def __init__(self, a, b, c):
        self.publico = a
        self._protegido = b # Um underline para definir um objeto protegido
        self.__privado = c # Dois underline para definir um objeto privado
    # Método público
    def metodo_publico(self):
        print("Esse é um método público!\n")

    # Método protegido
    def _metodo_protegido(self):
        print("Esse é um método protegido!\n")
    
    # Método privado
    def __metodo_privado(self):
        print("Esse é um método privado!\n")
    
if __name__ == "__main__":

    # Cria o objeto 'teste'
    teste = Teste(1, 2, 3)

    # Público
    print("A: ", teste.publico)
    teste.metodo_publico()

    #Protegido
    print("B: ", teste._protegido) 
    teste._metodo_protegido()
    
    # Privado (incorreta)
    try:
        print("C: ", teste.__privado)
        teste.__metodo_privado()

        # Privado (correta)
    except:
        print("C: ", teste._Teste__privado)
        teste._Teste__metodo_privado()
