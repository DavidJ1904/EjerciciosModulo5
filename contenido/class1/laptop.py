class Lapto:
    def __init__(self, marca, procesador, memoria, costo = 500, impuestos = 10):
        self.marca = marca
        self.procesador = procesador
        self.memoria = memoria
        self.costo = costo
        self.impuestos = impuestos
    #Metodos de instancia
    def valor_final(self):
        return self.costo + self.impuestos
    
    def valor_descuento(self, descuento):
        return (self.costo*descuento)/100

    #Metodos estaticos
    @staticmethod
    def comparar_costo(Laptop1, Laptop2):
        if Laptop1.costo == Laptop2.costo:
            return "Los costos son iguales"
        return "Los costos son diferentes"
    
    #Metodo de clase
    @classmethod
    def asus_laptops(cls, costo ):
        marca = "Asus"
        procesador = "i5"
        memoria = 16
        return cls(marca, procesador, memoria, costo)
    
