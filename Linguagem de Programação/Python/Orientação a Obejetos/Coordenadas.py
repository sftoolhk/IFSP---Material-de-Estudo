class Point(object):
    """Ponint class for representing and manipulating x, y coordinates."""
    
    #Contructor
    def __init__(self):
        """Create a new point at the x and y coordinates.""" 
        self.x = 0
        self.y = 0
        

print("Criando os objetos P1 e P2:\n")

P1 = Point()

P2 = Point()

print("Objetos criados com sucesso...\n")

print("P1: %s" %P1)
print("P2: %s\n" %P2)

print("P1 = P2 -> %s" %(P1 is P2))
print()