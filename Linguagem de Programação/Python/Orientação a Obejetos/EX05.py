class Point(object):
    """Ponint class for representing and manipulating x, y coordinates."""
    
    #Contructor
    def __init__(self, x = 0, y = 0):
        """Create a new point at the x and y coordinates.""" 
        self.x = x
        self.y = y

    def get_x(self):
        """Returns the x coordinate of the point."""
        return self.x    

    def get_y(self):
        """Returns the y coordinate of the point."""
        return self.y
    
    def distance_from_origin(self):
        """Returns the distance from the point to the origin."""
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def midpoint(self, target):
        """Calculates the midpoint between two points and returns a new object with that value."""
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my) 
    
print("Criando os objetos P1 e P2:\n")

p1 = Point()

p2 = Point()

print("Objetos criados com sucesso...\n")

print("P1: %s" %p1)
print("P2: %s\n" %p2)

# Verifica se os objetos são iguais
print("P1 = P2 -> %s" %(p1 is p2))
print()

# Retorna o valor das coordenadas do ponto P1
print("Coordenada X de P1: %s" %(p1.get_x()))
print("Coordenada y de P1: %s" %(p1.get_y()))
print()

# Retorna o valor das coordenadas do ponto P2
print("Coordenada X de P2: %s" %(p2.get_x()))
print("Coordenada y de P2: %s" %(p2.get_y()))
print()

print("Criando o objeto P3:\n")
p3 = Point(10, 20)

print("Coordenada X de P3: %s" %(p3.get_x()))
print("Coordenada y de P3: %s" %(p3.get_y()))
print()

print("Distância de P3 até a origem: %.2f" %(p3.distance_from_origin()))

print("Criação daos objetos P4 e P5...\n")

p4 = Point(3, -2)
p5 = Point(5, 15)

print("Calculando o ponto médio (PM) entre P4 e P5...\n")

PM = p4.midpoint(p5)

print("Coordenada X de PM: %s" %(PM.get_x()))
print("Coordenada Y de PM: %s" %(PM.get_y()))
print()