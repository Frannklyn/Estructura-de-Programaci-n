# EJERCICIO 1: Validador de notas con promedio
# --- PASO 1: Entender el problema (E-P-S) ---
# ENTRADA: Notas individuales o en lotes (*args).
# PROCESO: Validar cada nota (0-100), guardar en lista, calcular promedio.
# SALIDA: True/False, lista de válidas, promedio.
# EJEMPLO ENTRADA: c = Calificador(); c.cargar_notas(85, 92, 110, 78, -5, 88).
# SALIDA ESPERADA: [85, 92, 78, 88] y 85.75.

# --- PASO 2: Bosquejo a mano ---
# Lote de notas: 85, 92, 110, 78, -5, 88.
# ¿Es 85 válido? Sí (0-100) -> Guardo.
# ¿Es 92 válido? Sí -> Guardo.
# ¿Es 110 válido? No (>100) -> Ignoro.
# ¿Es 78 válido? Sí -> Guardo.
# ¿Es -5 válido? No (<0) -> Ignoro.
# ¿Es 88 válido? Sí -> Guardo.
# Lista final: [85, 92, 78, 88].
# Promedio: (85 + 92 + 78 + 88) / 4 = 343 / 4 = 85.75.

# --- PASO 3: Descubrir el patrón ---
# 1. Constructor (__init__): Inicializar una lista vacía para las notas válidas.
# 2. Método validar_nota(nota): Condicional para retornar True si 0 <= nota <= 100, si no, False.
# 3. Método cargar_notas(*args): Bucle for para iterar sobre *args. Llamar a validar_nota(nota) y, si es True, agregar a la lista con append().
# 4. Método promedio(): Retornar la suma de la lista dividida para la longitud de la lista (len).


# --- PASO 4: Escribir el código ---
class Calificador:
    def __init__(self):
        self.notas_validas = []
    
    def validar_nota(self, nota):
        if 0 <= nota <= 100:
            return True
        else:
            return False
        
    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota) == True:
                self.notas_validas.append(nota) 
        return self.notas_validas
        
    def promedio(self):
        if len(self.notas_validas) == 0:
            return 0
        else:
            return sum(self.notas_validas) / len(self.notas_validas)

c = Calificador()
c.cargar_notas(85, 92, 110, 78, -5, 88)
print(f"Promedio: {c.promedio()}")


# --- PASO 5: Prueba de escritorio (Trace execution) ---
# ACCIÓN                                 | LISTA INTERNA       | SALIDA 
# c = Calificador()                      | []                  | - 
# cargar_notas(85, 92, 110, 78, -5, 88)  | [85, 92, 78, 88]    | [85, 92, 78, 88].
# promedio()                             | [85, 92, 78, 88]    | 85.75.

# ==========================================
# EJERCICIO 2: Contador de palabras únicas
# ==========================================

# --- PASO 1: Entender el problema (E-P-S) ---
# ENTRADA: Palabras individuales o en lotes (*args).
# PROCESO: Guardar las palabras al mismo tiempo en un conjunto (para unicidad) y en una lista (para orden). Luego contar las únicas.
# SALIDA: La cantidad total de palabras únicas (un número).
# EJEMPLO ENTRADA: at = AnalizadorTexto(); at.agregar_multiples("hola", "mundo", "hola"); at.contar_palabras().
# SALIDA ESPERADA: 2.

# --- PASO 2: Bosquejo a mano ---
# Lote de palabras: "hola", "mundo", "hola".
# 1. Llega "hola":
#    - Lista: ["hola"]
#    - Conjunto: {"hola"}
# 2. Llega "mundo":
#    - Lista: ["hola", "mundo"]
#    - Conjunto: {"hola", "mundo"}
# 3. Llega "hola" de nuevo:
#    - Lista: ["hola", "mundo", "hola"] (La lista sí admite repetidos).
#    - Conjunto: {"hola", "mundo"} (El conjunto ignora el duplicado automáticamente).
# Conteo final: El conjunto tiene 2 elementos.

# --- PASO 3: Descubrir el patrón ---
# 1. Constructor (__init__): Inicializar DOS colecciones vacías. Una lista [] y un conjunto set().
# 2. Método agregar_palabra(palabra): Usar el método .append() para la lista, y el método .add() para el conjunto.
# 3. Método agregar_multiples(*args): Bucle for para iterar sobre args. Reutilizar el método anterior llamando a self.agregar_palabra(palabra) en cada vuelta.
# 4. Método contar_palabras(): Usar len() sobre el conjunto para retornar cuántas palabras únicas hay.


# --- PASO 4: Escribir el código ---
class AnalizadorTexto:
    def __init__(self):
        self.lista_palabras = []
        self.conjunto_palabras = set()
    
    def agregar_palabra(self, palabra):
        self.lista_palabras.append(palabra)
        self.conjunto_palabras.add(palabra)
    
    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)
    
    def contar_palabras(self):
        return len(self.conjunto_palabras)

at = AnalizadorTexto()
at.agregar_multiples("hola", "mundo", "hola")
cantidad = at.contar_palabras()

print(f"Palabras únicas encontradas: {cantidad}")
print(f"Historial en lista: {at.lista_palabras}")


# --- PASO 5: Prueba de escritorio (Trace execution) ---
# ACCIÓN                                      | LISTA INTERNA               | CONJUNTO INTERNO    | SALIDA 
# at = AnalizadorTexto()                      | []                          | set()               | - 
# agregar_multiples("hola", "mundo", "hola")  | ["hola", "mundo", "hola"]   | {"hola", "mundo"}   | - 
# contar_palabras()                           | ["hola", "mundo", "hola"]   | {"hola", "mundo"}   | 2


# ==========================================
# EJERCICIO 3: Gestor de compras con totales
# ==========================================

# --- PASO 1: Entender el problema (E-P-S) ---
# ENTRADA: Nombres de artículos (texto) y precios (números)[cite: 1].
# PROCESO: Guardar en diccionario, sumar valores, filtrar por rango[cite: 1].
# SALIDA: Total de la compra y lista de artículos en rango[cite: 1].
# EJEMPLO ENTRADA: c = CarroCompras(); c.agregar_articulo("pan", 2.50); c.agregar_articulo("leche", 3.00); c.total_carrito()[cite: 1].
# SALIDA ESPERADA: 5.50[cite: 1].

# --- PASO 2: Bosquejo a mano ---
# 1. Agrego "pan" a $2.50:
#    Diccionario: {"pan": 2.50}
# 2. Agrego "leche" a $3.00:
#    Diccionario: {"pan": 2.50, "leche": 3.00}
# 3. Calculo el total:
#    Suma de precios = 2.50 + 3.00 = 5.50.
# 4. Filtro por rango (ej. entre 2.00 y 2.60):
#    "pan" vale 2.50 -> ¡Entra!
#    "leche" vale 3.00 -> Se pasa, no entra.
#    Resultado del filtro: ["pan"]

# --- PASO 3: Descubrir el patrón ---
# 1. Constructor (__init__): Inicializar un diccionario vacío {}.
# 2. Método agregar_articulo(nombre, precio): Guardar en el diccionario usando self.carrito[nombre] = precio[cite: 1].
# 3. Método total_carrito(): Sumar los valores del diccionario usando sum(self.carrito.values())[cite: 1].
# 4. Método articulos_por_rango(precio_min, precio_max): Iterar con for nombre, precio in self.carrito.items(). Validar si el precio está en el rango y guardar el nombre en una lista[cite: 1].

# --- PASO 4: Escribir el código ---
class CarroCompras:
    def __init__(self):
        self.carrito = {}

    def agregar_articulo(self, nombre, precio):
        self.carrito[nombre] = precio

    def total_carrito(self):
        return sum(self.carrito.values())

    def articulos_por_rango(self, precio_min, precio_max):
        articulos_filtrados = []
        for nombre, precio in self.carrito.items():
            if precio >= precio_min and precio <= precio_max:
                articulos_filtrados.append(nombre)
        return articulos_filtrados 
    
c = CarroCompras()
c.agregar_articulo("pan",2.50)
c.agregar_articulo("leche",3.00)
c.total_carrito()
lista_baratos = c.articulos_por_rango(2.00, 2.60) 
print(lista_baratos)

# --- PASO 5: Prueba de escritorio (Trace execution) ---
# ACCIÓN                            | DICCIONARIO INTERNO           | SALIDA 
# c = CarroCompras()                | {}                            | - 
# agregar_articulo("pan", 2.50)     | {"pan": 2.50}                 | - 
# agregar_articulo("leche", 3.00)   | {"pan": 2.50, "leche": 3.00}  | - 
# total_carrito()                   | {"pan": 2.50, "leche": 3.00}  | 5.50
class InversorSecuencia:
    def __init__(self):
        self.resultados = {}

    def invertir_lista(self, lista):
        lista_invertida = []
        indice = len(lista) - 1 
        while indice >= 0:
            elemento = lista[indice]
            lista_invertida.append(elemento)
            indice -= 1
        return lista_invertida

    def invertir_multiples(self, *listas):
        for sublista in listas:
            invertida = self.invertir_lista(sublista)
            clave_etiqueta = tuple(sublista) 
            self.resultados[clave_etiqueta] = invertida 
        return self.resultados
    
inv = InversorSecuencia()
diccionario_final = inv.invertir_multiples([1, 2, 3], [10, 20, 30])
print(diccionario_final)

# ==========================================
# EJERCICIO 5: Detector de números pares e impares
# ==========================================

# --- PASO 1: Entender el problema (E-P-S) ---
# ENTRADA: Números en lote (*numeros)[cite: 1].
# PROCESO: Clasificar cuáles son pares y cuáles impares usando el operador módulo (%)[cite: 1].
# SALIDA: Un diccionario con dos listas, y una tupla con las cantidades[cite: 1].
# EJEMPLO ENTRADA: an = AnalizadorNumeros(); an.separar(1,2,3,4,5)[cite: 1].
# SALIDA ESPERADA: {'pares': [2, 4], 'impares': [1, 3, 5]}[cite: 1].

# --- PASO 3: Descubrir el patrón ---
# 1. Constructor (__init__): ¿Necesitas inicializar un diccionario con las listas de pares e impares vacías desde el principio?
# 2. Método es_par(numero): Usa (numero % 2 == 0) para retornar True o False[cite: 1].
# 3. Método separar(*numeros): Iterar con for. Si es_par() es True, hacer .append() en la lista de pares. Si es False, en la de impares[cite: 1]. Retornar el diccionario.
# 4. Método cantidad_pares_impares(): Retornar una tupla así: ( len(lista_pares), len(lista_impares) )[cite: 1].

# --- PASO 4: Escribir el código ---
class AnalizadorNumeros:
    def __init__(self):
        self.resultados = {'pares': [], 'impares': []}

    def es_par(self, numero):
        if numero % 2 == 0:
            return True
        else:
            return False

            