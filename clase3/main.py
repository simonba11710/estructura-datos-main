
"""
factorial: int = 1

for i in range(1, 6):
    factorial = i * factorial

print(factorial)
"""
# con while
"""
i = 0
q = 1

while i < 5:
    i = i + 1
    q = q * i

print(q)
"""

# con funciones
"""
def factorial (n: int) -> int:
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
"""

def multiplicacion(a: int, b: int) -> int:
    if a == 1:
        return b
    return b + multiplicacion(a - 1, b)

print(multiplicacion(5, 2))