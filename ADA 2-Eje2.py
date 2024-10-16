from collections import deque

class ColaServicios:
    def __init__(self):
        self.cola = deque()

    def agregar(self, codigo_cliente):
        self.cola.append(codigo_cliente)

    def atender(self):
        return self.cola.popleft() if self.cola else "No hay clientes para atender"
    
    def mostrar_cola(self):
        return list(self.cola) if self.cola else ["No hay clientes"]

class Sistema:
    def __init__(self):
        self.colas = {i: ColaServicios() for i in range(1, 5)}
        self.contador = 0

    def codigo(self):
        self.contador += 1
        return f"c{self.contador}"
            
    def man_entr(self, entrada):
        try:
            comando, servicio = entrada.split()
            servicio = int(servicio)
            codigo_cliente = self.codigo() if comando == "C" else None
            
            if comando == "C":
                self.colas[servicio].agregar(codigo_cliente)
                print(f"✨ Cliente {codigo_cliente} agregado al servicio {servicio} ✨")
            elif comando == "A":
                print(f"🛎️  Atendiendo al cliente del servicio {servicio}. Código de cliente: {self.colas[servicio].atender()}")
            else:
                print("🚫 Comando desconocido ")
        except (ValueError, KeyError):
            print("❌ Entrada o servicio inválido ")
        self.mostrar_cola()

    def mostrar_cola(self):
        print("\n📋  Estado actual de las colas:")
        for servicio, cola in self.colas.items():
            print(f"Servicio {servicio}: ", cola.mostrar_cola())
        print()

    def servicios(self):
        print(" " * 41 + "Centro de Servicios Públicos Disponibles")
        print("=" * 137)        
        print("Servicio 1: Pago de facturas de electricidad")
        print("Servicio 2: Pago de impuestos locales")
        print("Servicio 3: Mantenimiento de vías públicas")
        print("Servicio 4: Renovación de licencias\n")

def imprimir_bienvenida():
    print("""
                         ██████╗ ██╗███████╗███╗   ██╗██╗   ██╗███████╗███╗   ██╗██╗██████╗  ██████╗   
                         ██╔══██╗██║██╔════╝████╗  ██║██║   ██║██╔════╝████╗  ██║██║██╔══██╗██╔═══██╗        
                         ██████╔╝██║█████╗  ██╔██╗ ██║██║   ██║█████╗  ██╔██╗ ██║██║██║  ██║██║   ██║      
                         ██╔══██╗██║██╔══╝  ██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║██║  ██║██║   ██║      
                         ██████║ ██║███████╗██║ ╚████║ ╚████╔╝ ███████╗██║ ╚████║██║██████╔╝╚██████╔╝       
                         ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═╝╚═════╝  ╚═════╝
    """)

sistema = Sistema()
imprimir_bienvenida()

while True:
    sistema.servicios()
    entrada = input("Ingrese el comando 'C' (Cliente), 'A' (Atender) o 'S' (Salir) y el número de servicio: ")
    if entrada.lower() == 's':
        print("\nSaliendo del programa....\n")
        break
    sistema.man_entr(entrada)
