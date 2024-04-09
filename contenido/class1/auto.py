class auto:
    def __init__(self,marca, modelo, año, kilometraje=0):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje
        #Muestra de informacion
    def mostar_informacion():
        print(f"Las especificaciones del carro son: {auto_comprado.__dict__}")
        #Actualizar el kilometraje
    def actializar_kilometraje(kilometraje_nuevo):
        if kilometraje_nuevo> auto_comprado.kilometraje:
            auto_comprado.kilometraje = kilometraje_nuevo
            print(kilometraje_nuevo)
        else:
            ("La cantidad de kilometros debe ser positiva")
        #Realizar un viaje
    def realizar_viaje(kilometraje_recorrido):
        if kilometraje_recorrido>0:
             auto_comprado.kiometraje= kilometraje_recorrido
             print(auto_comprado.__dict__)
        else:
             print("La cantidad de kilometro debe de ser positiva")
        #Mostrar estado del auto
    def estado_auto():
        if auto_comprado.kiometraje<20000:
             print("Estoy como nuevo")
        elif auto_comprado.kiometraje>=20000 and auto_comprado.kiometraje<=100000:
             print("ya estoy usado")
        elif auto_comprado.kiometraje>100000:
            print("¡ya dejame descansar!")
  
auto_comprado = auto("Renault","Megane",2004)
auto.mostar_informacion()
auto.actializar_kilometraje(10000)
auto.realizar_viaje(30000)
auto.estado_auto()
