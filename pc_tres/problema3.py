class Circulo:
    
    constante_pi = 3.1416

    def __init__(self, name):
        self.name = name

    def nombrar(self):
        print(f"el monbre de la figura es {self.name}")

    def area_circulo(self, radio):
        if radio <0:
            print("error")
        else:
            area = radio * self.constante_pi
            print(f"el area del circulo es {area}")


c1 = Circulo("circulo")
c1.nombrar()
c1.area_circulo(5)