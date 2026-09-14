# Creación
#                 -1
saludo = "Hola mundo"
#         0123456789
mensaje = 'con comillas simples también'
multi = """tres comillas
para varias líneas"""
# Acceso e índice negativo
print(saludo[0])   # 'H'
print(saludo[-1])  # 'o' (último)

# Slicing (rebanadas)
print(saludo[0:4])  # 'Hola'
print(saludo[5:10])   # 'mundo'
print(saludo[:])   # 'mundo'
sal = saludo
# Longitud y recorrido
print(len(saludo))  # 10
for ch in saludo:
    print(ch)

# Inmutabilidad
# saludo[0] = "h"  ← ERROR: TypeError
saludo = "h" + saludo[1:]  # Crear una nueva cadena
frase="Hola, ¿cómo estás?"
cv = 0
ca = 0
cp = 1
cs=0
signos=",.:;"
vocales="aeiouAEIOU"
for car in frase: 
    #if car in vocales:  # ← se crea una NUEVA cadena
     #   cv = cv + 1

    if car == "a" or car == "A" or car == "e" or car == "E" or car == "i" or car == "I" or car == "o" or car == "O" or car == "u" or car == "U":  # ← se crea una NUEVA cadena
        cv = cv + 1
    if (car >= "A" and car <= "Z") or (car >= "a" and car <= "z"):
        ca = ca + 1
    if car == " ":
        cp += 1  
    if car in signos:
        cs = cs + 1

#print(f"Cantidad de vocales: {cv}")
#print(f"Cantidad de consonantes: {ca}")
nombre="Da,n,i,e,la"
lista=["Juan", "María", "Pedro"]
x = nombre.split(",")
nombres= "".join(lista)
print(nombre.find("p"))
print(nombre.index("p"))