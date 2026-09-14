# Varios parámetros
""" nom="Juan"
# Parámetros con valor por defecto
def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}")
def suma(a, b):
    return a + b
# Llamadas
print(suma(3, 5))  
n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
r1= suma(n1, n2)
r2 = suma(2, 8)  # llamada con nombres 
sumas=[]   
sumas.append(r1)
sumas.append(r2)
print(sumas)
print(suma(sumas[0], sumas[1] ))  # llamada con nombres
saludar("Ana")               # Hola, Ana (usa el default)
saludar("Ana", "Buenos días") # Buenos días, Ana
saludar(saludo="Hi", nombre="Ana")  # llamada con nombres

# Función sin parámetros ni retorno
def separador():
    print("=" * 40)

separador()   
 """
nombre = "Juan"
def multiplicar(*numeros):
    acu = 1
    for num in numeros:
        acu = acu * num
    print("num ",num)
    return acu

print(multiplicar(2, 3, 4))

def datos(**nombres ):

    for clave, valor in nombres.items():
        print(f"{clave}: {valor}")
     # Acceso a un valor específico
datos(nombre="Juan", edad=30, ciudad="Madrid")


def operacion(a,b):
    suma=a+b
    multiplicacion=a*b
    return suma,multiplicacion

resultados = operacion(5, 3)
s,m = operacion(5, 3)
print(resultados)
print(f"Suma: {s}, Multiplicación: {m}")
print(nombre)

def evento(titulo, *invitados, lugar="Casa", **detalles):
    print(f"Evento: {titulo} en {lugar}")
    print(f"Invitados: {invitados}")
    print(f"Detalles: {detalles}")

evento("Cumpleaños", "Ana", "Luis", "Diana",
       lugar="Salón", tema="80s", regalo=True)