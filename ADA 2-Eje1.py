from collections import deque

class Cola:
    def __init__(self):
        self.elementos = deque()
    
    def encolar(self, valor):
        self.elementos.append(valor)
    
    def desencolar(self):
        return self.elementos.popleft() if self.elementos else None
    
    def esta_vacia(self):
        return not self.elementos

def sumar(cola_A, cola_B): 
    print("\n  Cola A   Cola B   Resultado")
    resultado = Cola()
    
    while not cola_A.esta_vacia() and not cola_B.esta_vacia():
        valor_A = cola_A.desencolar()
        valor_B = cola_B.desencolar()
        suma = valor_A + valor_B
        resultado.encolar(suma)
        print(f"    {valor_A:<8} {valor_B:<9} {suma:<5}")
    return resultado

cola_A = Cola()
cola_B = Cola()

for valor in [3, 4, 2, 8, 12]:
    cola_A.encolar(valor)

for valor in [6, 2, 9, 11, 3]:
    cola_B.encolar(valor)

cola_res = sumar(cola_A, cola_B)
print()