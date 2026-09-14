# Creación
vacia = []
notas = [7, 8.5, 9, 6.5]
nombres = ["Ana", "Luis", "Diana"]
mezcla = [1, "dos", True, [3, 4],{"nombre":"ana","edad":40}]  # admite cualquier tipo

# Acceso, longitud, verificación
print(notas[0])       # 7
print(notas[-1])      # 6.5 (último)
print(len(notas))     # 4
print(9 in notas)     # True

# Modificación
notas[0] = 10          # cambiar por índice
notas.append(8)         # añadir al final → O(1)
notas.insert(0, 5)      # insertar al inicio → O(n)
notas.remove(6.5)        # quita la primera ocurrencia de 6.5
ultima = notas.pop()      # saca y retorna el último

# Recorrido
for n in notas:
    print(n)

for i, n in enumerate(notas):
    print(f"posición {i} → {n}")

# Ordenamiento
notas.sort()              # in-place, ascendente
notas.sort(reverse=True)  # in-place, descendente
nueva = sorted(notas)   # retorna copia ordenada

# Slicing y copia
primeras = notas[:2]     # primeros 2
copia = notas[:]          # copia completa (no alias)

# Comprensión de listas
cuadrados = [n*n for n in range(6)]  # [0,1,4,9,16,25]
cuadrados2 = tuple([n*n for n in range(6)])  # [0,1,4,9,16,25]
pares = [n for n in notas if n % 2 == 0]