class Nodo:
    def __init__(self, datos_vehiculo):
        self.datos_vehiculo = datos_vehiculo
        self.siguiente = None

class Cola:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def encolar(self, datos_vehiculo):
        nuevo_nodo = Nodo(datos_vehiculo)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def desencolar(self):
        if self.cabeza is None:
            return None

        nodo_desencolado = self.cabeza
        self.cabeza = self.cabeza.siguiente
        if self.cabeza is None:
            self.cola = None

        return nodo_desencolado.datos_vehiculo

    def esta_vacia(self):
        return self.cabeza is None

def cola_recepcion(datos_vehiculo):
    cola_recepcion = Cola()
    cola_recepcion.encolar(datos_vehiculo)
    print(f"Vehículo {datos_vehiculo['matricula']} agregado a la cola de recepción.")

def cola_pruebas(datos_vehiculo):
    cola_pruebas = Cola()
    cola_pruebas.encolar(datos_vehiculo)
    print(f"Vehículo {datos_vehiculo['matricula']} agregado a la cola de pruebas.")

def cola_despacho(datos_vehiculo):
    cola_despacho = Cola()
    cola_despacho.encolar(datos_vehiculo)
    print(f"Vehículo {datos_vehiculo['matricula']} agregado a la cola de despacho.")

def obtener_vehiculos_en_operacion():
    tamaño_cola_recepcion = 0
    tamaño_cola_pruebas = 0
    tamaño_cola_despacho = 0

    if not cola_recepcion.esta_vacia():
        tamaño_cola_recepcion = obtener_tamaño_cola(cola_recepcion)

    if not cola_pruebas.esta_vacia():
        tamaño_cola_pruebas = obtener_tamaño_cola(cola_pruebas)

    if not cola_despacho.esta_vacia():
        tamaño_cola_despacho = obtener_tamaño_cola(cola_despacho)

    total_vehiculos = tamaño_cola_recepcion + tamaño_cola_pruebas + tamaño_cola_despacho
    print(f"Total de vehículos en operación: {total_vehiculos}")

def obtener_tamaño_cola(cola):
    nodo_actual = cola.cabeza
    tamaño = 0
    while nodo_actual:
        tamaño += 1
        nodo_actual = nodo_actual.siguiente
    return tamaño

def generar_reporte_diario():
    # Implementar la logica para generar un reporte diario con información de los vehículos
    print("Generando reporte diario...")

# Ejemplo de uso
datos_vehiculo = {
    "matricula": "ABC123",
    "tipo": "carro",
    "propietario": "Juan Perez"
}

cola_recepcion(datos_vehiculo)
# Simular pruebas y mover el vehículo a la cola de pruebas
cola_pruebas(datos_vehiculo)
# Simular la finalización de las pruebas y mover el vehículo a la cola de despacho
cola_despacho(datos_vehiculo)

obtener_vehiculos_en_operacion()
generar_reporte_diario()
