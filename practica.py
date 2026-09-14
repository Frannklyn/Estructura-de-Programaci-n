def ejer1():
    #Convertir grados Celsius a Fahrenheit
    c = int(input("Ingrese los grados celsius: "))

    f = c * 9/5 + 32

    print(f"En temperatura Fahrenheit es: {f} °F")

def ejer2():
    #Segundos a horas, minutos y segundos
    tseg = int(input("Ingrese los segundos totales: "))

    h = tseg // 3600
    resto = tseg % 3600
    min = resto // 60
    seg = resto % 60

    print(f"{h}:{min:02d}:{seg:02d}")

def ejer3():
    #Intercambiar dos variables
    a = int(input("Ingrese la variable a: "))
    b = int(input("Ingrese la variable b: "))

    a, b = b, a

    print(f"Variable a: {a}, Variable b: {b}")

def ejer4():
    #Calcular el IVA
    IVA = 0.15
    precio = int(input("Ingrese el precio: "))

    iva = precio * IVA
    total = precio + iva

    print(f"IVA agregado: ${iva:.2f}")
    print(f"Total: ${total:.2f}")

def ejer5():
    #Suma digitos de un numero de 3 cifras
    num = int(input("Ingrese un numero de 3 cifras: "))

    centenas = num // 100
    decenas = (num // 10) % 10
    unidades = num % 10
    suma = centenas + decenas + unidades 

    print(f"La suma es: {suma}")

def ejer6():
    #Convertir minutos a horas y minutos
    total = int(input("Ingrese los minutos totales: "))

    h = total // 60
    min = total % 60

    print(f"{h} horas {min} minutos")

def ejer7():
    #Indice de masa corporal (IMC)
    peso = float(input("Peso (kg): "))
    estatura = float(input("Estatura (m): "))

    imc = peso / (estatura ** 2)

    print(f"IMC: {imc:.2f}")

def ejer8():
    #Redondeo por cifra decimal
    num = float(input("Ingrese un numero: "))
    dec = int(input("Ingrese la cantidad de decimales: "))

    result = round(num, dec)

    print(f"El resultado es: {result}")

def ejer9():
    #Descuento por cantidad
    precio = float(input("Ingrese el precio: "))
    cant = int(input("Ingrese la cantidad de productos: "))

    if cant >= 10:
        descuento = 0.15
    elif cant >= 5:
        descuento = 0.05
    else:
        descuento = 0

    subt = precio * cant
    total = subt * (1 - descuento)

    print(f"Precio unitario: ${precio}")
    print(f"Descuento: {int(descuento*100)}%")
    print(f"Total: ${total:.2f}")

def ejer10():
    #Tabla de multiplicar
    n = int(input("Ingrese un numero: "))

    for i in range (1, 13):
        print(f"{n} x {i}: {n*i}")

def ejer11():
    #Contar digitos de un numero
    num = int(input("Ingrese una cantidad de numeros: "))
    n = abs(num)
    digitos = 0

    if n == 0:
        digitos = 1
    else: 
        while n > 0:
            digitos +=1
            n = n // 10

    print(f"Hay {digitos} digitos")

def ejer12():
    #Suma de pares e impares
    n = int(input("Ingrese la cantidad de numeros: "))
    sp = 0
    si = 0

    for i in range(n):
        num = int(input(f"Numero {i+1}: "))

        if num % 2 == 0:
            sp += num
        else: 
            si += num

    print(f"Suma de los pares: {sp}")
    print(f"Suma de impares: {si}")

def ejer13():
    while True:
        edad = int(input("Ingrese una edad (0 - 120): "))

        if 0 <= edad <= 120:
            break
        print("Edad invalida; intenta otra vez")
    print(f"Edad valida: {edad}")

import random
def ejer14():
    #Adivina el numero
    secreto = random.randint(1, 100)
    intentos = 0

    while True:
        intento = int(input("Adivina (1-100): "))
        intentos += 1

        if intento == secreto: 
            print(F"Felicidades en {intentos} intentos adivinaste")
            break
        elif intento < secreto:
            print("Es mayor")
        else:
            print("Es menor")

def ejer15():
    num = int(input("¿Cuántos numeros? "))
    a, b = 0, 1    

    for _ in range(num):                 
        print(a, end=" ")
        a, b = b, a + b                 

    print()   
ejer15()                          