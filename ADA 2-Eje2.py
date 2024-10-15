from collections import deque

class ColaServicios:
    def __init__(self):
        self.cola = deque()

    def agregar_cliente(self, codigo_cliente):
        self.cola.append(codigo_cliente)
        return codigo_cliente

    def atender_cliente(self):
        return self.cola.popleft() if self.cola else "No hay clientes en la cola"

class SistemaColas:
    def __init__(self):
        self.colas = {i: ColaServicios() for i in range(1, 4)}
        self.contador = 0

    def generar_codigo_cliente(self):
        self.contador += 1
        return f"c{self.contador}"

    def manejar_entrada(self, entrada):
        try:
            comando, servicio = entrada.split()
            servicio = int(servicio)
            if comando == "C":
                codigo_cliente = self.generar_codigo_cliente()
                self.colas[servicio].agregar_cliente(codigo_cliente)
                print(f"Cliente {codigo_cliente} agregado al servicio {servicio}.")
            elif comando == "A":
                print(f"Atendiendo al cliente del servicio {servicio}: {self.colas[servicio].atender_cliente()}")
            else:
                print("Comando desconocido.")
        except (ValueError, KeyError):
            print("Entrada o servicio inválido.")

    def mostrar_servicios(self):
        print("Servicios: 1, 2, 3")

sistema = SistemaColas()

while True:
    sistema.mostrar_servicios()
    entrada = input("Ingrese comando (C para cliente, A para atender o 'Salir'): ")
    if entrada.lower() == 'salir':
        break
    sistema.manejar_entrada(entrada)