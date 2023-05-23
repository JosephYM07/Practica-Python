# Este bloque de código le pide al usuario que ingrese el número de filas y columnas para dos matrices. 

while True:
    row1=int(input("\n-Ingrese el número de filas de la primera matriz: "))
    column1=int(input("-Ingrese el número de columnas de la primera matriz: "))
    matrix1=[]
    row2=int(input("\n-Ingrese el número de filas de la segunda matriz: "))
    column2=int(input("-Ingrese el número de columnas de la segunda matriz: "))
    matrix2=[]
    #Luego verifica si el número de columnas en la primera matriz es igual al número de filas
    # en la segunda matriz. Si no son iguales, imprime un mensaje de error
    if column1!=row2:
        print("[No se puede multiplicar las matrices La matriz base debe tener el mismo número de columnas que filas\n ejemplo: (2x3)x(3x2)]")
    else: 
        break;
    #  Luego  pide al usuario que ingrese las dimensiones nuevamente. Si son iguales, el bucle se rompe y el programa continúa.
            
print("\n\nIngrese los elementos de la primera matriz: ")
for i in range(row1):
    row=[]
    for j in range(column1):
        element=int(input("\n-Ingrese el elemento a ["+str(i+1)+"]["+str(j+1)+"]: "))
        row.append(element)
    matrix1.append(row)

print("\n\nIngrese los elementos de la primera matriz: ")
for i in range(row2):
    row=[]
    for j in range(column2):
        element=int(input("\n-Ingrese el elemento a ["+str(i+1)+"]["+str(j+1)+"]: "))
        row.append(element)
    matrix2.append(row)

print("\n\nLa primera matriz es: ")
for i in range(row1):
    for j in range(column1):
        print("[ ",matrix1[i][j], end=" ]")
    print()

print("\n\nLa segunda matriz es: ")
for i in range(row2):
    for j in range(column2):
        print("[ ",matrix2[i][j], end=" ]")
    print()

    # Este bloque de código multiplica las dos matrices ingresadas por el usuario y almacena el resultado
    # en una nueva matriz llamada `resultado`. Lo hace iterando a través de cada fila de la primera matriz
    # (`matrix1`) y cada columna de la segunda matriz (`matrix2`). Para cada elemento de la matriz
    # resultante, calcula el producto  de la fila correspondiente en `matriz1` y la columna en
    # `matriz2`. El producto punto se calcula iterando a través de cada elemento en la fila y
    # multiplicándolo por el elemento correspondiente en la columna, y luego sumando los productos. La
    # suma resultante se agrega luego a una nueva fila en la matriz `resultado`.

result=[]
for i in range(row1):
    row=[]
    for j in range(column2):
        element=0
        for k in range(column1):
            element+=matrix1[i][k]*matrix2[k][j]
        row.append(element)
    result.append(row)

print("\n\nEl resultado de la multiplicación es:")
for i in range(row1):
    for j in range(column2):
        print("[ ",result[i][j], end=" ]")
    print()
