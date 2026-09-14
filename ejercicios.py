#Pide una temperatura en grados Celsius y muéstrala en Fahrenheit. Fórmula: F = C × 9/5 + 32.
F = float(input("Ingrese un grado: "))
C = (F-32) * 5/9
print(f"Su conversion a Celsius es: {C:.2f}°")
#Pide un total de segundos y muéstralos como hh:mm:ss. Ej.: 3725 segundos → 1:02:05.
total = int(input("Ingrese un total de segundos: "))
horas = total // 3600
resto = total % 3600
minutos = resto // 60
segundos = resto % 60
print(f"{horas}:{minutos:02d}:{segundos:02d}")
#Lee dos números y muéstralos intercambiados. Python permite hacerlo en una sola línea, muy diferente a JS.
a = int(input("Ingrese un número a: "))
b = int(input("Ingrese un número b: "))

a,b = b,a
print(f"a = {a}, b = {b}")
#Lee el precio de un producto sin IVA y muestra el IVA (15%) y el total. (aumentado - descuento)
precio = float(input("Ingrese precio del producto: "))
if precio > 100:
    desc = 0.10
    precio_desc = precio * desc
    precio_tot = precio - precio_desc
else: 
    print("No aplica")
    precio_tot = precio

iva = 0.15
precio_iva = precio_tot * iva
total_final = precio_tot + precio_iva

print(f"El IVA (15%) es: ${precio_iva:.2f}")
print(f"El precio total a pagar es: ${total_final:.2f}")
#Lee un número de 3 cifras y muestra la suma de sus dígitos. Ejemplo: 435 → 4+3+5 = 12.
num = int(input("Ingrese un número de 3 cifras: "))
centenas = num // 100
decenas = (num // 10) % 10
unidades = num % 10

suma = centenas + decenas + unidades
print(f"Suma: {suma}")

#Lee una cantidad de minutos y muéstrala como «X horas Y minutos». Ejemplo: 135 → «2 horas 15 minutos».
minutos = int(input("Minutos totales: "))
horas = minutos // 60
mins = minutos % 60
print(f"{horas} horas {mins} minutos")

#Lee peso (kg) y estatura (m) y calcula el IMC. Fórmula: IMC = peso / estatura². Muestra el IMC con 2 decimales.
peso = float(input("Ingrese peso: "))
altura = float(input("Ingrese altura: "))
IMC = peso / altura**2
print(f"El resultado de su IMC es de: {IMC:.2f}")

#Lee un número decimal y una cantidad de decimales, y muéstralo redondeado. Ejemplo: 3.14159 con 2 decimales → 3.14.
num = float(input("Número: "))
dec = int(input("Decimales: "))
resultado = round(num, dec)
print(resultado)

#Un producto vale $12. Si compras 10 o más te dan 15% de descuento, si compras entre 5 y 9 te dan 5%. Calcula el total.
precio = float(input("Ingrese precio del producto: "))
cantidad = int(input("Ingrese cantidad del producto: "))
if cantidad >= 10:
    desc = 0.15
elif cantidad >= 5 and cantidad <= 9:
    desc = 0.05
else:
    desc = 0
precio_d = precio * cantidad
precio_t = precio_d * (1- desc)
print(f"Precio unitario: ${cantidad}")
print(f"Descuento: {desc*100}%")
print(f"Precio total a pagar: ${precio_t:.2f}")

#Lee un número N y muestra su tabla de multiplicar (del 1 al 12).
n = int(input("Tabla de: "))
for i in range(1, 13):
    print(f"{n} x {i} = {n * i}")

#Lee un número y cuenta cuántos dígitos tiene (sin convertir a string).
n = int(input("Ingrese un numero: ")) 
c = 0
while n > 0:
    n = n // 10   
    c = c + 1     
print(f"{c} digitos")
