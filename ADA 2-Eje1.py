from collections import deque

class Cola:
    def __init__(self):
        self.elementos = deque()
    
    def encolar(self, valor):
        self.elementos.append(valor)
    
    def desencolar(self):
        return self.elementos.popleft() if self.elementos else None
    
    def vacia(self):
        return not self.elementos

    def mostrar(self):
        return ', '.join(map(str, self.elementos)) if self.elementos else 'Esta cola está vacía'

def imprimir(cola_A, cola_B, resultados=None):
    print(f"\n{'Cola A':^10} {'Cola B':^10} {'Resultado':^10}")
    print(f"{'-'*10} {'-'*10} {'-'*10}")
    
    max_len = max(len(cola_A.elementos), len(cola_B.elementos))
    
    for i in range(max_len):
        valor_A = cola_A.elementos[i] if i < len(cola_A.elementos) else ''
        valor_B = cola_B.elementos[i] if i < len(cola_B.elementos) else ''
        res = resultados[i] if resultados and i < len(resultados) else ''
        print(f"{str(valor_A):^10} {str(valor_B):^10} {str(res):^10}")

def sumar(cola_A, cola_B): 
    resultado_parcial = []
    imprimir(cola_A, cola_B)
    
    while not cola_A.vacia() and not cola_B.vacia():
        valor_A = cola_A.desencolar()
        valor_B = cola_B.desencolar()
        suma = valor_A + valor_B
        resultado_parcial.append(suma)
        
        print(f"\nSumando los valores: {valor_A} + {valor_B} = {suma}")
        imprimir(cola_A, cola_B, resultado_parcial)
    
    print(f"\n{'Resultados finales de las sumas de los números:':^40}")
    print(f"{'-'*40}")
    for res in resultado_parcial:
        print(f"{res:^40}")
    
    print(f"\nEstado final de Cola A: [{cola_A.mostrar()}]")
    print(f"Estado final de Cola B: [{cola_B.mostrar()}]")
    print()

cola_A = Cola()
cola_B = Cola()

for valor in [3, 4, 2, 8, 12]:
    cola_A.encolar(valor)

for valor in [6, 2, 9, 11, 3]:
    cola_B.encolar(valor)

cola_A.desencolar()
cola_B.desencolar()

sumar(cola_A, cola_B)
