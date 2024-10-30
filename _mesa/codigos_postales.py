# Lista para almacenar los nuevos valores de la primera columna
nuevos_valores_primera_columna = []

# Conjunto para rastrear los valores ya agregados
valores_vistos = set()

# Abre el archivo en modo lectura
with open('Baja California.txt', 'r') as archivo:
    # Lee todas las líneas del archivo
    lineas = archivo.readlines()

    # Itera sobre cada línea del archivo
    for linea in lineas:
        # Divide la línea en partes usando '|' como separador y toma el primer valor
        valor_primera_columna = linea.strip().split('|')[0]
        # Verifica si el valor ya ha sido visto antes
        if valor_primera_columna not in valores_vistos:
            # Agrega el valor de la primera columna a la lista de nuevos valores
            nuevos_valores_primera_columna.append(valor_primera_columna)
            # Agrega el valor a los valores vistos
            valores_vistos.add(valor_primera_columna)

# Abre el archivo en modo escritura para sobrescribir
with open('Baja California.txt', 'w') as archivo:
    # Escribe los nuevos valores de la primera columna en el archivo
    for valor in nuevos_valores_primera_columna:
        archivo.write(valor + '\n')
