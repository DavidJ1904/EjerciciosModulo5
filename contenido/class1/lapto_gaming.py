from laptop import Lapto

class Laptop_gaming(Lapto):
    def __init__(self, marca, procesador, memoria,tarjeta_graf, costo=500, impuestos=10):
        super().__init__(marca, procesador, memoria, costo, impuestos)
        self.tarjeta_graf = tarjeta_graf
    
    def realizar_diagnostico_sistema(self):
        resultado_diagnostico = super().realizar_diagnostico_sistema(); #ALMACENARLO EN UNA VARIABLE 
        #OTRA FUNCIONALIDAD
        resultado_juego = self.realizar_diagnostico_sistema_juego()
        resultado_diagnostico["resultados juegos"] = resultado_juego
        return resultado_diagnostico
    
    def realizar_diagnostico_sistema_juego(self):
        juegos= ["FORNITE","COD","GTA"]
        resultados = {}
        for juego in juegos: #JUEGO ME MUESTRA ES EL NOMBRE 
            fps_base = 30
            if "RTX" in self.tarjeta_graf:
                fps= fps_base*3
            elif "GTX" in self.tarjeta_graf:
                fps= fps_base*2
            else:
                fps= fps_base
            resultados[juego] = f"{fps} FPS"
        return resultados
    pass