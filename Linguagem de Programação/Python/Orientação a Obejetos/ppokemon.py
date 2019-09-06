class pokemon(object):

    __slots__ = ['name', '__HP', '__MP']

    def __init__(self, name, HP, MP):
        self.name = name
        self.__HP = HP
        self.__MP = MP


    def get_HP(self):
        return self.__HP
    

    def set_HP(self, HP):
        self.__HP = HP


    def get_MP(self):
        return self.__MP
    

    def set_MP(self, MP):
        self.__HP = MP

 
def main():

    print('\n')

    pikachu = pokemon('Pikachu', 100, 100)
    charmander = pokemon('Charmander', 0, 100)

    print('Nome: %s' %(pikachu.name))
    print('HP: %d' %(pikachu.get_HP()))
    print('MP: %d' %(pikachu.get_MP()))
    print()

    charmander.set_HP(500)

    print('Nome: %s' %(charmander.name))
    print('HP: %d' %(charmander.get_HP()))
    print('MP: %d' %(charmander.get_MP()))
    print('\n')

    #print(pikachu.__dict__)
    #print(charmander.__dict__)
    print(pikachu.__slots__)

if __name__ == "__main__":
    main()