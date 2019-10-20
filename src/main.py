import pprint
import os
import sys

# Breadth First Search Method (Busqueda en Amplitud)
def amplitud(grafo, inicio, destino):
    cola = [(inicio, [inicio], 0)]
    visitado = {inicio}
    while cola:
        (node, camino, costo) = cola.pop(0)
        for temp in grafo[node].keys():
            if temp == destino:
                return camino + [temp], costo + grafo[node][temp]
            else:
                if temp not in visitado:
                    visitado.add(temp)
                    cola.append((temp, camino + [temp], costo + grafo[node][temp]))


# Depth First Search Method (Busqueda en Profundidad)
def profundidad(grafo, inicio, destino):
    pila = [(inicio, [inicio], 0)]
    visitado = {inicio}
    while pila:
        (node, camino, costo) = pila.pop()
        for temp in grafo[node].keys():
            if temp == destino:
                return camino + [temp], costo + grafo[node][temp]
            else:
                if temp not in visitado:
                    visitado.add(temp)
                    pila.append((temp, camino + [temp], costo + grafo[node][temp]))

# Best First search (Busqueda Primero el Mejor)
def Primero_el_mejor(grafo, inicio, destino):
    #Metodo
    pass

if __name__ == "__main__":
    # Pprint para mostrar de forma Pretty
    pp = pprint.PrettyPrinter(indent=4)
    # Grafo principal
    grafo_principal = {}

    # Lee el archivo .txt y carga el grafo_principal
    sys.argv[1]
    with open(sys.argv[1], 'r') as f:
        for l in f:
            ciudad_a, ciudad_b, costo, distancia = l.split(",")
            if ciudad_a not in grafo_principal:
                grafo_principal[ciudad_a] = {}
            grafo_principal[ciudad_a][ciudad_b] = int(costo)
            if ciudad_b not in grafo_principal:
                grafo_principal[ciudad_b] = {}
            grafo_principal[ciudad_b][ciudad_a] = int(costo)
    n = 1
    while n == 1:
        os.system("clear")
        print("""============================================
                    Grafo Completo
    ============================================""")
        pp.pprint(grafo_principal)
        print("""============================================
    [1] Amplitud
    [2] Profundidad
    [3] Primero el mejor
    [0] Salir
    ============================================""")
        x = input("Opcion: ")
        if x == '1':
            inicio = input("Ingresa el Inicio: ")
            while inicio not in grafo_principal:
                print("Ciudad no encontrada intenta nuevamente")
                inicio = input("Ingresa el Inicio: ")
            destino = input("Ingresa el Destino: ")
            while destino not in grafo_principal:
                print("Ciudad no encontrada intenta nuevamente")
                destino = input("Ingresa el Destino: ")
            print("""============================================
                    Resultados
    ============================================""")
            print (amplitud(grafo_principal, inicio, destino))
            print("============================================")
            input()

        elif x == '2':
            inicio = input("Ingresa el Inicio: ")
            while inicio not in grafo_principal:
                print("Ciudad no encontrada intenta nuevamente")
                inicio = input("Ingresa el Inicio: ")
            destino = input("Ingresa el Destino: ")
            while destino not in grafo_principal:
                print("Ciudad no encontrada intenta nuevamente")
                destino = input("Ingresa el Destino: ")
            print("""============================================
                    Resultados
                    ============================================""")
            print (profundidad(grafo_principal, inicio, destino))
            print("============================================")
            input()

        elif x == '3':
            inicio = input("Ingresa el Inicio: ")
            while inicio not in grafo_principal:
                print("Ciudad no encontrada intenta nuevamente")
                inicio = input("Ingresa el Inicio: ")
            destino = input("Ingresa el Destino: ")
            while destino not in grafo_principal:
                print("Ciudad no encontrada intenta nuevamente")
                destino = input("Ingresa el Destino: ")
            print("""============================================
                    Resultados
    ============================================""")
            print(primero_el_mejor(grafo_principal, inicio, destino))
            print("============================================")
            input()

        elif x == '0':
            break