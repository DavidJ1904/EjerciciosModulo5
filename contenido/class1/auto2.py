class auto:
    def __init__(self, marca,modelo,año,kilometraje=0):
      self.marca = marca
      self.modelo= modelo
      self.año=año
      self.kilometraje= kilometraje
    #Metodo de clase con el año
    @classmethod
    def auto_toyota(cls):
        marca = "Toyota"
        modelo = "Tacoma"
        año = 2024
        return cls(marca, modelo, año)
    #Metodo de clase con el kilometraje
    @classmethod
    def auto_kilometraje(cls,kilometraje):
       marca = "Toyota"
       modelo = "Tocoma"
       año = 2023
       kilometraje = 0
       return cls(marca, modelo, año, kilometraje)
    
    #Metodo comprar kilometraje
    @staticmethod
    def comprar_kilometraje(auto1, auto2):
       if auto1.kilometraje ==  auto2.kilometraje:
          return "Los autos tienen el mismo kilometraje"
       return "Los autos no tienen el mismo kilometraje"

    #Metodo comprar año
    @staticmethod
    def comprar_año(auto1, auto2):
       if auto1.año == auto2.año:
          return "Los autos tienen el mismo año"
       return "Los autos no tienen el mismo año"
    
nuevo_auto = auto.auto_toyota()
print(nuevo_auto.__dict__)

for codigo in range(20, 24):
   nuevo_auto = auto.auto_kilometraje(codigo)
   print(nuevo_auto.__dict__)
#Comparar año
mazda = auto("Mazda","CX-30",2019)
renault = auto("Renault","Megane",2004)
print(auto.comprar_año(mazda,renault))
#Comparar Kilometraje    
mazda = auto("Mazda","CX-30",2019,kilometraje=170890)
renault = auto("Renault","Megane",2004,kilometraje=134092)
print(auto.comprar_kilometraje(mazda,renault))