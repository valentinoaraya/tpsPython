"""
#1
palabra = "Mordor"
print(palabra[0],palabra[2])

#2
frase = str(input("Ingrese una frase: "))
print(frase[0])
print(frase[0].upper())

#3
frase = str(input("Ingrese una frase con longitud mayor a 5: "))
if len(frase) > 5:
    print(frase[0:3])
else:
    print("Error: Frase con longitud menor que 5 caracteres.")

#4
n = int(input("Ingrese un número: "))
if n > 1 and n < 50:
    for n in range(n,51):
        print(n)
else:
    print("Número incorrecto.")

#5
nums = [2,64,34,3,8,65]
suma = nums[0] + nums[2] + nums[5]
print(suma)

#6
ingredients = ["Chocolate", "Huevos", "Manteca", "Crema de leche", "Frutillas"]
for ing in ingredients: 
    if ingredients.index(ing) == len(ingredients) - 1:
        print("Canela en polvo")
    else:
        print(ing)

#7
list = [56,7,34,19,3,1,76,2,81,4,2,8]
for n in list:
    if list.index(n) % 2 == 0: # DUDA: SE DUPLICA LA INDEXACIÓN DEL NÚMERO 2. 
        print(n)

#8
palabra1 = str(input("Ingrese una palabra: "))
palabra2 = str(input("Ingrese otra palabra: "))
union = palabra1+palabra2
print(union)
# Respuesta 1: Se me ocurren 2 soluciones:
    # 1- Crear una variable que contenga la concatenación de las palabras y luego mostrarla.
    # 2- Agregar las palabras ingresadas a una lista y luego mostrarlas con el operador *.

# Respuesta 2: La diferencia es que en la concatenación las palabras se unen y se hacen una. Y en mostrarlas seguidas en pantalla se muestran las palabras separadas.

#9
colors = ["amarillo", "azul", "violeta"]
elements = ["zapallo", "tomate", "limón"]
newList = [*colors, *elements]
print(newList)

#10
peliculas = []
count = 1
while count <= 10:
    pelicula = str(input("Ingrese el nombre de una película: "))
    peliculas.append(pelicula)
    count = count + 1

n = int(input("Ingrese un número del 1 al 10: "))

if n >= 1 and n <= 10:
    print(f"La película en esa posición es '{peliculas[n-1]}'")
else:
    print("El número ingresado está fuera de rango.")

#11
palabra = str(input("Ingrese una palabra: "))
length = len(palabra)
newWord = palabra[0]+palabra[round((length/2)-1)]+palabra[length-1]
print(newWord)
    
#12
import math
palabra = str(input("Ingrese una palabra: "))
mid = math.ceil((len(palabra)/2) - 1)
print(palabra[mid-1]+palabra[mid]+palabra[mid+1])

#13
frutas = ["Manzana", "Banana", "Naranja"]
verduras = ["Brócoli", "Lechuga", "Zanahoria"]
frutasVerduras = []
for i in range(len(frutas)):
    frutasVerduras.append(frutas[i])
    frutasVerduras.append(verduras[i])
print(frutasVerduras)

-------------- Cadenas de Caracteres o Strings --------------

#14
nombreCompleto = str(input("Ingrese su nombre y apellido: "))
arrayNombre = nombreCompleto.split(" ")
nombreCapitalizado = []
for n in arrayNombre:
    nombreCapitalizado.append(n[0].upper()+n[1:].lower())
print(" ".join(nombreCapitalizado))

#15
frase = str(input("Ingrese una frase: "))
for l in frase:
    if frase.index(l) % 2 == 0:
        print(l)

#16
frase = str(input("Ingrese una frase: "))
letra = str(input("Ingresa una letra: "))
count = 0
for l in frase:
    if l == letra:
        count = count + 1
print(f"La letra '{letra}' aparece {count} veces en la frase ingresada.")

#17
abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z", " "]
abecedarioMayus = [" "]
listaCaracteres = []
for l in abecedario:
    abecedarioMayus.append(l.upper())
frase = str(input("Ingrese una frase con símbolos: "))
spaces = 0
for c in frase:
    if c in abecedario or c in abecedarioMayus:
        if c == " ":
            spaces += 1
    elif c in listaCaracteres:
        listaCaracteres.remove(c)
        listaCaracteres.append(c)
    else:
        listaCaracteres.append(c)
print(f"La cantidad de espacios en la frase es {spaces}.")
print(f"Los símbolos que hay en la frase son: {listaCaracteres}")

#18
frase = str(input("Ingrese una frase: "))
for i in range(len(frase)):
    if frase[i] == "a" or frase[i] == "A":
        frase = frase[:i]+"4"+frase[i+1:]
    elif frase[i] == "e" or frase[i] == "E":
        frase = frase[:i]+"3"+frase[i+1:]
print(frase)

#19
nombreArchivo = input("Ingrese el nombre de un archivo: ")
for i in range(len(nombreArchivo)):
    if nombreArchivo[i] == " ":
        nombreArchivo = nombreArchivo[:i]+"_"+nombreArchivo[i+1:]
    elif nombreArchivo[i] == ".":
        numeroNumerales = len(nombreArchivo[i+1:])
        nombreArchivo = nombreArchivo[:i+1]+"#"*numeroNumerales
print(nombreArchivo)

#20
n = int(input("Ingrese un número de no más de un dígito: "))
listNumbers = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
if n >=0 and n < 10: 
    for i in range(len(listNumbers)):
        if n == i:
            print(listNumbers[i])        
else:
    print("Error: número negatiovo o de más de un dígio.")
    
#21
frase = str(input("Ingrese una frase: "))
cantidadEspacios = 0
espacioAnterior = 0
numeroEspacio = 0
for l in frase:
    if l == " ":
        cantidadEspacios += 1
for i in range(len(frase)):
    if frase[i] == " ":
        numeroEspacio += 1
        if numeroEspacio == cantidadEspacios:
            if cantidadEspacios == 1:
                print(frase[espacioAnterior:i])
                print(frase[i+1:])
            else:    
                print(frase[espacioAnterior+1:i])
                print(frase[i+1:])
        elif espacioAnterior == 0:
            print(frase[espacioAnterior:i])
            espacioAnterior = i
        else:
            print(frase[espacioAnterior+1:i])
            espacioAnterior = i

#22
listaNombres = ["Valentino", "Nacho", "Faustino", "Agustin", "Mauro", "Luciano"]
nombre = str(input("Ingrese un nombre: "))
for i in range(len(listaNombres)):
    if nombre.upper() == listaNombres[i].upper():
        print("El nombre pertenece a la lista.")

#23
nombres = []
nombresConM = []
x=1
while x<=8:
    nombre = str(input("Ingrese un nombre: "))
    nombres.append(nombre)
    x += 1

def firstLetter(listNames):
    for n in listNames:
        if n[0] == "M":
            nombresConM.append(n)
    return nombresConM

print(firstLetter(nombres))

#24
frase = str(input("Ingrese una frase: "))
palabras = frase.split(" ")
print(palabras)

#25
frase = str(input("Ingrese una frase: "))
letras = []
for l in frase:
    if l != " ":
        letras.append(l)
print(letras)

#26
cantidadNombres = int(input("Qué cantidad de nombres quiere agregar? --> "))
nombres = []
apellidos = []
x = 1
while x <= cantidadNombres:
    nombreApellido = str(input("Ingrese un nombre completo: "))
    for l in range(len(nombreApellido)):
        if nombreApellido[l] == " ":
            nombres.append(nombreApellido[:l])
            apellidos.append(nombreApellido[l+1:])
    x += 1
print(nombres)
print(apellidos)

#27
x = 1
totalNotas = 0
while x <= 8:
    nota = float(input(f"Ingrese la {x}° nota: "))
    totalNotas += nota
    x += 1
prom = round(totalNotas/8,2)
print(f"El promedio de las nostas es de {prom}")

#28 -- SIN LISTAS --
abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
abcInMayus = []
for letra in abc:
    abcInMayus.append(letra.upper())
frase = str(input("Ingresa una fase: "))
cantidadPalabras = 1
for i in range(len(frase)):
    if i != len(frase)-1:
        if frase[i] == " " and frase[i+1] != " " and (frase[i+1] in abc or frase[i+1] in abcInMayus):
            cantidadPalabras += 1
print(f"La cantidad de palabras en la frase es de {cantidadPalabras}")
#28 -- CON LISTA --
listaPalabras = frase.split(" ")
print(f"La cantidad de palabras en la frase es de {len(listaPalabras)}")

#29
x = 1
listNumbers = []
listDigits = []
fin = int(input("Cuántos números desea añadir? --> "))
while x <= fin:
    n = int(input("Ingrese un número: "))
    listNumbers.append(n)
    x += 1
for number in listNumbers:
    numInString = str(number)
    digit = len(numInString)
    listDigits.append(digit)
print(f"La lista de números es: {listNumbers}")
print(f"La lista de digitos es: {listDigits}")

#30
import random
totalTiradas = 0
for i in range(20):
    n = random.randint(1,6)
    totalTiradas = totalTiradas + n
promedio = totalTiradas/20
print(f"El promedio de las tiradas es {promedio}")

#31
import random
totalTiradas = 0
for i in range(2500):
    n = random.randint(1,6)
    totalTiradas = totalTiradas + n
promedio = totalTiradas/2500
print(f"El promedio de las tiradas es {promedio}")

#32
import random
marcas = []
x = 1
while x <= 10:
    marca = str(input("Ingrese su marca favorita: "))
    marcas.append(marca)
    x += 1
print(marcas[random.randint(1,10)])

#33
cantidadNotas = int(input("Cuántas notas desea ingresar? --> "))
notas = []
for i in range(cantidadNotas):
    nota = float(input(f"Ingrese la {i+1}° nota: "))
    notas.append(nota)
print(notas)
"""