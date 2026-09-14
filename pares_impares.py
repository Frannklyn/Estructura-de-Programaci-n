class AnalizadorNumeros:
    def __init__(self):
        self.ultimo_resultado = {'pares': [], 'impares': []}

    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        resultado = {'pares': [], 'impares': []}
        for numero in numeros:
            if self.es_par(numero):
                resultado['pares'].append(numero)
            else:
                resultado['impares'].append(numero)
        self.ultimo_resultado = resultado
        return resultado

    def cantidad_pares_impares(self):
        return (len(self.ultimo_resultado['pares']),
                len(self.ultimo_resultado['impares']))

an = AnalizadorNumeros()
print(an.separar(1, 2, 3, 4, 5))
print(an.cantidad_pares_impares())