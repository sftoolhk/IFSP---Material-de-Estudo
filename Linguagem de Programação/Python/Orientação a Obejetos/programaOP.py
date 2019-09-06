class TV(object):

    def __init__(self):

        print("A TV está sendo ligada...\n")
        self.ligado = True
        self.__canal = 1
        self.__volume = 1
        self.__polegadas = None
    
    def __del__(self):
        print("Desligando a TV...\n")


    def set_canal(self, c):
        if not self.ligado:
            print("Ligue a TV primeiro!\n")
        else:
            self.__canal = c
    

    def set_volume(self, v):

        if not self.ligado:
            print("Ligue a TV primeiro!\n")
        else:
            self.__volume = v
    

    def get_canal(self):
        return self.__canal


    def get_volume(self):
        return self.__volume

        
def main():
    tv = TV()

    # Desliga a TV
    tv.ligado = True

    # Seta o canal e volume da TV
    tv.set_canal(10)
    tv.set_volume(10)
    

    # Exibi o canal e volume da TV
    print("Dados na minha TV...")
    print("Canal: %d" %(tv.get_canal()))
    print("Volume: %d" %(tv.get_volume()))
    print("Status: %s\n" %(tv.ligado))


# Executa o trecho com o código principal
if __name__ == "__main__":
    main()