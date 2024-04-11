import random
from laptop import Lapto
class Laptop_Business(Lapto):
  def __init__(self, marca, procesador, memoria, costo=500, impuesto=10):
    super().__init__(marca, procesador, memoria, costo, impuesto)

  def realizar_diagnostico_sistema(self):
    resultado_diagnostico = super().realizar_diagnostico_sistema()
    #OTRA FUNCIONALIDAD
    resultado_conectividad = self.verificar_conectividad_red()
    resultado_diagnostico["Resultado Conectividad"] = resultado_conectividad
    return resultado_diagnostico
  
  def verificar_conectividad_red(self):
    aspecto_conectividad = ["Disponibilidad de Wifi","Servidores empresariales", "latencia de la red"]
    resultados = {}
    for aspecto_conectividad_wifi in aspecto_conectividad:
      if "Disponibilidad de Wifi" in aspecto_conectividad:
        conectividad = random.choice([True,False])
      elif "Servidores empresariales" in aspecto_conectividad:
        conectividad = random.choice([True,False])
      elif "latencia de la red" in aspecto_conectividad:
        conectividad = random.choice([True,False])
      resultados[aspecto_conectividad_wifi] = f"{conectividad}"
    return resultados
  
  #METODO PARA MOSTRAR 
  def __str__(self) -> str:
    return f" marca: {self.marca} \n procesador: {self.procesador} \n memoria: {self.memoria} \n costo: {self.costo} \n impuesto: {self.impuestos} \n"
    

laptop_juanito = Laptop_Business("MSI","I7",500)
print(laptop_juanito.realizar_diagnostico_sistema())