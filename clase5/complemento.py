from collections import deque

class Vehiculo:
    def __init__(self, tipo_vehiculo, nombre_cliente, motivo_revision):
        self.tipo_vehiculo = tipo_vehiculo
        self.nombre_cliente = nombre_cliente
        self.motivo_revision = motivo_revision
        self.numero_vehiculo = None
        self.resultados_revision = {}

class CDA:
    def __init__(self):
        self.cola_espera = deque()
        self.cola_revision = deque()

    def registrar_vehiculo(self, vehiculo):
        vehiculo.numero_vehiculo = len(self.cola_espera) + 1
        self.cola_espera.append(vehiculo)

    def iniciar_revision(self):
        if self.cola_espera:
            vehiculo = self.cola_espera.popleft()
            self.cola_revision.append(vehiculo)

    def agregar_resultado(self, numero_vehiculo, resultado):
        vehiculo = self.obtener_vehiculo(numero_vehiculo)
        vehiculo.resultados_revision[resultado.tipo_prueba] = resultado

    def despachar_vehiculo(self, numero_vehiculo):
        vehiculo = self.obtener_vehiculo(numero_vehiculo)
        if vehiculo in self.cola_revision:
            self.cola_revision.remove(vehiculo)
        print(f"Vehículo {vehiculo.numero_vehiculo} despachado")

    def obtener_vehiculo(self, numero_vehiculo):
        for vehiculo in self.cola_espera + self.cola_revision:
            if vehiculo.numero_vehiculo == numero_vehiculo:
                return vehiculo
        return None

    def consultar_vehiculos_en_espera(self):
        return len(self.cola_espera)

    def retirar_vehiculo(self, numero_vehiculo):
        vehiculo = self.obtener_vehiculo(numero_vehiculo)
        if vehiculo in self.cola_espera:
            self.cola_espera.remove(vehiculo)
        elif vehiculo in self.cola_revision:
            self.cola_revision.remove(vehiculo)
            print(f"Revisión del vehículo {vehiculo.numero_vehiculo} cancelada")

    def generar_reporte(self):

        pass


cda = CDA()

vehiculo1 = Vehiculo("Carro", "Juan Pérez", "Cambio de aceite")
vehiculo2 = Vehiculo("Moto", "Ana García", "Revisión de frenos")
vehiculo3 = Vehiculo("Camión", "Pedro López", "Mantenimiento general")
vehiculo4 = Vehiculo("Helicoptero", "Simon Barrera", "Revision del motor")

cda.registrar_vehiculo(vehiculo1)
cda.registrar_vehiculo(vehiculo2)
cda.registrar_vehiculo(vehiculo3)
cda.registrar_vehiculo(vehiculo4)

cda.iniciar_revision()
cda.iniciar_revision()

cda.agregar_resultado(1, Resultado("Aceite", "Bueno"))
cda.agregar_resultado(2, Resultado("Frenos", "Desgastados"))

cda.despachar_vehiculo(1)
cda.despachar_vehiculo(2)

print(f"Vehículos en espera: {cda.consultar_vehiculos_en_espera()}")

cda.retirar_vehiculo(3)

cda.generar_reporte()