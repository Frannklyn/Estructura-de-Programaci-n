class Pasajero:
    # El constructor: se llama al crear el objeto
    def __init__(self, nom, ced, eda):
        self.nombre = nom          # atributo del objeto
        self.cedula = ced
        self.edad = eda

    # Método: acción que puede realizar el objeto
    def saludar(self):
        print(f"Hola, soy {self.nombre}")

    # Método especial __str__: cómo se ve en print()
    def __str__(self):
        return f"{self.nombre} ({self.cedula}) - {self.edad} años"

# Crear objetos (instanciar la clase)
p1 = Pasajero("Ana", "0912345678", 28)
p2 = Pasajero("Luis", "0987654321", 35)
lista = [p1, p2]
for p in lista:
    print(p)
    p.saludar()  # llama a __str__ automáticamente
# Acceder a atributos
print(p1.nombre)              # Ana
print(p2.edad)                # 35

# Llamar métodos
p1.saludar()                  # Hola, soy Ana

# print() usa __str__ automáticamente
print(p1)                     # Ana (0912345678) - 28 años