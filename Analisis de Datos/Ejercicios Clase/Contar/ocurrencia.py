archivo = open('constitucion.txt', 'r', encoding='utf-8')
mensaje = archivo.read().lower()  # Convertir a minúsculas
archivo.close()

palabras = mensaje.split()  # Separar el texto en palabras
palabras_unicas = set(palabras)  # Obtener las palabras únicas utilizando un conjunto

frecuencia_palabras = {}

for palabra in palabras:
    palabra = palabra.lower().strip(".,[...]{}...()  +*-") # cambiar a minúscula y quitar puntuación
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1

# Ordenar las palabras alfabéticamente mediante el método sorted
palabras_ordenadas = sorted(frecuencia_palabras.items())

# Imprimir los resultados
print("Palabra\t\tFrecuencia")

for palabra, frecuencia in palabras_ordenadas:
    print(f"{palabra}\t\t\t\t\t\t\t\t{frecuencia}")