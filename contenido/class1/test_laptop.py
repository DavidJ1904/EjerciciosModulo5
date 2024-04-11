from laptop import Lapto
from lapto_gaming import Laptop_gaming

def imprimir_informe(Lapto):
  informe = Lapto.realizar_informe_uso()
  for clave, valor in informe.items():
    print(f"{clave}:{valor}")
  print("\n")
    


Lapto_Pepito = Lapto("levono","i7",32)
Lapto_Maria = Lapto("levono","i7",32,600)


#for numero in range(1,1000):
#    asus_laptop = Lapto.asus_laptops(numero)
#    print(asus_laptop.__dict__)
#print(Lapto.comparar_costo(Lapto_Pepito, Lapto_Maria))

Laptop_Juanito = Laptop_gaming("MSI","I7", 4 ,"RTX 8G")

print("Pepito: ")
imprimir_informe(Lapto_Pepito)
print("Juanito: ")
imprimir_informe(Laptop_Juanito)