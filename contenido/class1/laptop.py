class Lapto:
    def __init__(self, marca, procesador, memoria, costo = 500, impuestos = 10):
        self.marca = marca
        self.procesador = procesador
        self.memoria = memoria
        self.costo = costo
        self.impuestos = impuestos

    def valor_final(self):
        return self.costo + self.impuestos
    
    def valor_descuento(self, descuento):
        return (self.costo*descuento)/100

Lapto_Pepito = Lapto("levono","i7",32)


print(Lapto_Pepito.__dict__)
print(Lapto_Pepito.valor_final())
print(f"El valor de descuento: {Lapto_Pepito.valor_descuento(10)}")