a = 3
b = 3

print(type(b))

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

nodo1 = Nodo(5)
nodo2 = Nodo(5)

print(type(nodo2))
print("="*50)
print("Nodo 2")
print(nodo2)
print("Nodo 1")
print(nodo1)