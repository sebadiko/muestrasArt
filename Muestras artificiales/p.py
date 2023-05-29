import random

tabla = {
    0: 0.0121,
    1: 0.0927,
    2: 0.1943,
    3: 0.3574,
    4: 0.2263,
    5: 0.0804,
    6: 0.0368
}

def calcular_frecuencia_acumulada(tabla):
    frecuencia_acumulada = []
    acumulador = 0
    for valor in tabla.values():
        acumulador += valor
        frecuencia_acumulada.append(acumulador)
    return frecuencia_acumulada

def calcular_indices(frecuencia_acumulada):
    indices = []
    for i in range(len(frecuencia_acumulada)):
        if i == 0:
            inferior = 0
        else:
            inferior = frecuencia_acumulada[i-1]
        superior = frecuencia_acumulada[i]
        indices.append((inferior, superior))
    return indices

def generar_muestra_artificial(tabla):
    frecuencia_acumulada = calcular_frecuencia_acumulada(tabla)
    indices = calcular_indices(frecuencia_acumulada)

    muestra_artificial = []
    n = len(tabla)

    for _ in range(n):
        numero_aleatorio = random.random()
        for i in range(n):
            inferior, superior = indices[i]
            if inferior <= numero_aleatorio <= superior:
                muestra_artificial.append(i)
                break

    return muestra_artificial

muestra_artificial = generar_muestra_artificial(tabla)
print("Muestra artificial:", muestra_artificial)