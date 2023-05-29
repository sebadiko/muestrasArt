def calcular_frecuencia_acumulada(frecuencias):
    frecuencia_acumulada = []
    acumulador = 0
    for frecuencia in frecuencias:
        acumulador += frecuencia
        frecuencia_acumulada.append(acumulador)
    return frecuencia_acumulada

def obtener_cantidad_decimales(numero):
    decimal = str(numero).split('.')
    if len(decimal) > 1:
        return len(decimal[1])
    else:
        return 0

def calcular_indices(frecuencia_acumulada, densidad, n, decimales):
    indices = []
    resta = densidad
    i = 0
    for i in range(n):
        inferior = round((float(frecuencia_acumulada[i]) - float(resta[i])), decimales)
        superior = round((frecuencia_acumulada[i]), decimales)
        indices.append((inferior, superior))
    return indices

def main():
    n = int(input("Ingrese el número de valores: "))
    valores_x = []
    valores_f = []

    for i in range(n):
        x = float(input(f"Ingrese el valor de x[{i}]: "))
        f = float(input(f"Ingrese el valor de f(x[{i}]): "))
        valores_x.append(x)
        valores_f.append(f)

    frecuencia_acumulada = calcular_frecuencia_acumulada(valores_f)
    decimales = max([obtener_cantidad_decimales(f) for f in valores_f])
    indices = calcular_indices(frecuencia_acumulada, valores_f, n, decimales)

    print("Frecuencia acumulada:", frecuencia_acumulada)
    print("Índices:", indices)

if __name__ == "__main__":
    main()