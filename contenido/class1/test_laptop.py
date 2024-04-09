from laptop import Lapto


Lapto_Pepito = Lapto("levono","i7",32)
Lapto_Maria = Lapto("levono","i7",32,600)


for numero in range(1,1000):
    asus_laptop = Lapto.asus_laptops(numero)
    print(asus_laptop.__dict__)
#print(Lapto.comparar_costo(Lapto_Pepito, Lapto_Maria))