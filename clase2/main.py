class Articulo:
    tipo: str
    anio: int
    referencia = "FGTY"
    nombre: str
    precio: float

    def __init__(self, n, p, valor_interno):
        self.nombre = n
        self.precio = p + valor_interno

    def asignar_tipo(self, tipo) -> None:
        self.tipo = tipo

    def asignar_anio(self, anio) -> None:
        self.anio = anio
    
    def asignar_referencia(self, referencia) -> None:
        self.referencia = referencia
    
    def obtener_nombre(self) -> str:
        return self.nombre
    
    def obtener_precio(self) -> float:
        return self.precio
    
    def obtener_tipo(self) -> str:
        return self.tipo
    
    def obtener_anio(self) -> int:
        return self.anio
    
    def obtener_referencia(self) -> str:
        return self.referencia
    
    @staticmethod
    def procesar():
        pass
    


class Pantalla (Articulo):
    resolucion: str
    alto: int
    ancho: int
    tasa_refresco: int

    def __init__(self, nombre, precio):
        super().__init__(nombre, precio, 0)
        self.tipo = "Pantalla"
    
    def asignar_resolucion(self, resolucion):
        self.resolucion = resolucion
    
    def asignar_alto(self, alto) -> None:
        self.alto = alto

    def asignar_ancho(self, ancho) -> None:
        self.ancho = ancho
    
    def asignar_tasa_refresco(self, tasa_refresco) -> None:
        self.tasa_refresco = tasa_refresco

    def obtener_resolucion(self) -> str:
        return self.resolucion

    def obtener_alto(self) -> int:
        return self.alto
    
    def obtener_ancho(self) -> int:
        return self.ancho
    
    def obtener_tasa_refresco(self) -> int:
        return self.tasa_refresco
    


pantalla_dell = Pantalla("Pantalla Dell", 1000)
pantalla_dell.asignar_resolucion("1920x1080") 
print(pantalla_dell.obtener_nombre()) 



#https://codeshare.io/jA0PV3