"""
#1
vector = []
for i in range(5):
    num = int(input("Ingrese un número: "))
    vector.append(num)
for nums in vector:
    print(nums)

#2
vector = []
for i in range(5):
    num = int(input("Ingrese un número: "))
    vector.append(num)
for j in range(len(vector)-1,-1,-1):
    print(vector[j])

#3
import random
vector = []
for i in range(20):
    vector.append(random.randint(0,100))
num = int(input("Ingrese un número: "))
if num in vector:
    print(f"El número {num} si se encuentra en el vector.")
    print(f"--> {vector}")
else:
    print(f"El número {num} no se encuentra en el vector.")
    print(f"--> {vector}")

#4
nombres = []
x = ""
while x != "zzz":
    nombre = str(input("Ingrese un nombre: "))
    if nombre == "zzz":
        x = nombre
    else:
        nombres.append(nombre)
for n in nombres:
    print(n)
    
#5
vector = ["elemento 1", "elemento 2", "elemento 3", "elemento 4", "elemento 5", "elemento 6", "elemento 7", "elemento 8", "elemento 9", "elemento 10", "elemento 11", "elemento 12", "elemento 13", "elemento 14", "elemento 15", "elemento 16", "elemento 17", "elemento 18", "elemento 19", "elemento 20"]
x = int(input("Ingrese la posición de inicio: "))
y = int(input("Ingrese la posición final: "))
if x > y:
    print("El valor de inicio no puede ser mayor que el valor final.")
elif x < 0 or y > 19:
    print("Los valores están fuera de rango.")
else:
    print(vector[x:y+1])

#6
import random
vector = []
for i in range(30):
    vector.append(random.randint(1,100))
x = int(input("Ingrese un valor entre 1 y 30: "))
y = int(input("Ingrese un valor entre 1 y 30: "))
if x < 1 or x > 30 or y < 1 or y > 30:
    print("Error: Alguno de los valores está fuera de rango.")
else:
    print(f"Vector original --> {vector}")
    newValorX = vector[x-1]
    newValorY = vector[y-1]
    vector[x-1] = newValorY
    vector[y-1] = newValorX
    print(f"Vector intercambiado --> {vector}")
    
#7
import random
suma = 0
vector = []
for i in range(18):
    vector.append(random.randint(1,50))
for n in vector:
    suma = suma + n
print(vector)
print(f"La suma total de los elementos del vector es {suma}")

#8
import random
suma = 0
vector = []
for i in range(18):
    vector.append(random.randint(1,50))
for n in vector:
    suma = suma + n
promedio = suma/18
print(vector)
print(f"El promedio de la suma total de los elementos del vector es {promedio}")

#9
import random
vector = []
for i in range(18):
    vector.append(random.randint(1,50))
maxValor = vector[0]
minValor = vector[0]
for n in vector:
    if n > maxValor:
        maxValor=n
    if n < minValor:
        minValor=n
print(vector)
print(f"El valor máximo del vector es {maxValor} y el mínimo es {minValor}")

#10
import random
butacas = []
butacasVacias = 0
for i in range(50):
    x = random.randint(0,1)
    if x == 1:
        butacas.append(True)
    else:
        butacas.append(False)
for b in butacas:
    if b == False:
        butacasVacias += 1
print(butacas)
print(f"Hay {butacasVacias} butacas desocupadas.")

#11
notas = [33, 11, 20, 2, 15, 1, 12, 11, 8, 14, 10]
notaMenor = notas[0]
for n in notas:
    if n < notaMenor:
        notaMenor = n
print(notas)
notas.remove(notaMenor)
print(f"La nota más baja es {notaMenor}")
sumaTotal = 0
for n in notas:
    sumaTotal = sumaTotal + n
promedio = sumaTotal/len(notas)
print(notas)
print(f"El promedio de las notas es {promedio}")

#12
import random
matriz = []
for f in range(4):
    fila = []
    for c in range(3):
        fila.append(random.randint(1,100))
    matriz.append(fila)
for fila in matriz:
    print(fila)

#13
import random
matriz = []
for f in range(5):
    fila = []
    for c in range(4):
        fila.append(random.randint(1,100))
    matriz.append(fila)
print("Filas: ")
for fila in matriz:
    print(fila)
print("Columnas: ")
columnas = []
for j in range(4):
    columna = []
    for fila in matriz:
        columna.append(fila[j])
    columnas.append(columna)
for columna in columnas:
    print(columna)
    
#14
matriz = []
vectorSumaFilas = []
vectorSumaColumnas = []
for f in range(4):
    fila = []
    for c in range(3):
        num = int(input(f"Ingrese el número en la posición {f+1}{c+1}: "))
        fila.append(num)
    matriz.append(fila)
for fila in matriz:
    sumaFilas = 0
    for numero in fila:
        sumaFilas += numero
    vectorSumaFilas.append(sumaFilas)
for i in range(3):
    sumaColumnas = 0
    for fila in matriz:
        sumaColumnas += fila[i]
    vectorSumaColumnas.append(sumaColumnas)
print(" ")
print("La matriz es: ")
for f in matriz:
    print(f)
print(" ")
print(f"La suma de las filas es --> {vectorSumaFilas}")
print(f"La suma de las columnas es --> {vectorSumaColumnas}")

#15 - Lo mismo que el 14
"""
#14
matriz = []
vectorSumaFilas = []
vectorSumaColumnas = []
for f in range(4):
    fila = []
    for c in range(3):
        num = int(input(f"Ingrese el número en la posición {f+1}{c+1}: "))
        fila.append(num)
    matriz.append(fila)
for fila in matriz:
    sumaFilas = 0
    for numero in fila:
        sumaFilas += numero
    vectorSumaFilas.append(sumaFilas)
for i in range(3):
    sumaColumnas = 0
    for fila in matriz:
        sumaColumnas += fila[i]
    vectorSumaColumnas.append(sumaColumnas)
print(" ")
print("La matriz es: ")
for f in matriz:
    print(f)
print(" ")
print(f"La suma de las filas es --> {vectorSumaFilas}")
print(f"La suma de las columnas es --> {vectorSumaColumnas}")