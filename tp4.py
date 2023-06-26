"""
#1
def suma(n1,n2):
    return n1+n2

num1 = int(input("Ingrese un número para sumarlo: "))
num2 = int(input("Ingrese otro número para sumarlo: "))
print(suma(num1,num2))

#2
def calculadora(n1,n2):
    print(f"Suma: {n1} + {n2} = {n1+n2}")
    print(f"Resta: {n1} - {n2} = {n1-n2}")
    print(f"Multiplicación: {n1} x {n2} = {n1*n2}")
    print(f"División: {n1} / {n2} = {n1/n2}")
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
calculadora(num1,num2)

#3
def division(n1,n2):
    if n2 == 0:
        print("Error: La división por 0 no está definida.")
    else:
        return n1/n2
n1 = int(input("Ingrese un número: "))
n2 = int(input("Ingrese un número: "))
print(f"El resultado de la división de los números es {division(n1,n2)}")

#4
def sumaDeNumeros(listNums):
    contenedor = 0
    for n in listNums:
        contenedor = n + contenedor
    return contenedor
lista = []
x = 1
fin = int(input("Cuántos números desea sumar? --> "))
while x <= fin:
    n = int(input("Ingrese un número: "))
    lista.append(n)
    x = x+1
print(f"El resultado de la suma de los números es {sumaDeNumeros(lista)}")

#5
def mayorNum(list):
    max = list[0]
    for n in list:
        if n > max:
            max = n
    return max
lista = []
x = 1
fin = int(input("Cuántos números desea agregar? --> "))
while x <= fin:
    n = int(input("Ingrese un número: "))
    lista.append(n)
    x = x+1
print(f"El número más grande de la lista es el {mayorNum(lista)}")

#6
def longitud(str):
    length = 0
    for l in str:
        length = length + 1
    return length
frase = str(input("Ingrese un texto: "))
print(f"La cantidad de caracteres de la palabra ingresada es {longitud(frase)}")

#7
def cuadrado(n):
    return n**2
num = int(input("Ingrese un número: "))
print(f"El cuadrado de {num} es {cuadrado(num)}")

#8
def positivoNegativo(n):
    if n > 0:
        print("El número es positivo.")
    elif n < 0:
        print("El número es negativo.")
    else:
        print("El número es 0.")
num = int(input("Ingrese un número: "))
positivoNegativo(num)

#9
def igualdad(n1,n2):
    if n1 == n2:
        print("Los números son iguales.")
    else:
        print("Los números son distintos.")
n1 = int(input("Ingrese un número: "))
n2 = int(input("Ingrese otro número: "))
igualdad(n1,n2)

#10
def rango(n,a,b):
    if a > b:
        if n >= b and n <= a:
            print(f"El número {n} se encuentra en el rango de {b} y {a}")
        else:
            print(f"{n} no se encuentra en el rango de {b} y {a}")
    elif b > a:
        if n >= a and n <=b:
            print(f"El número {n} se encuentra en el rango de {a} y {b}")
        else:
            print(f"{n} no se encuentra en el rango de {a} y {b}")
    elif a == b:
        if a == n:
            print("Los números son iguales.")
        else:
            print(f"{n} no se encuentra en el rango.")
n1 = int(input("Ingrese un número para determinar si está en el rango: "))
n2 = int(input("Ingrese un número: "))
n3 = int(input("Ingrese un número: "))
rango(n1,n2,n3)

#11
def cantidadVocales(str):
    vocales = 0
    for l in str:
        if l == "a" or l == "A":
            vocales = vocales + 1
        elif l == "e" or l == "E":
            vocales = vocales + 1
        elif l == "i" or l == "I":
            vocales = vocales + 1
        elif l == "o" or l == "O":
            vocales = vocales + 1
        elif l == "u" or l == "U":
            vocales = vocales + 1
    return vocales
frase = str(input("Ingrese una frase: "))
print(f"La cantidad de vocales en la frase es {cantidadVocales(frase)}")

#12
def concatenarPalabras(str1, str2):
    return f"{str1} {str2}"
frase1 = str(input("Ingrese una palabra/frase: "))
frase2 = str(input("Ingrese una palabra/frase: "))
print(concatenarPalabras(frase1,frase2))

#13
def letraEnFrase(str, letra):
    count = 0
    for l in str:
        if l == letra:
            count = count + 1
    return count
frase = str(input("Ingrese una frase: "))
letra = str(input("Ingrese una letra: "))
print(f"La letra {letra} se encuentra {letraEnFrase(frase,letra)} veces en la frase ingresada.")

#14
def mayus(str):
    newWord = str[0].upper()+str[1:].lower()
    return newWord
frase = str(input("Ingrese una frase: "))
print(mayus(frase))

#15
def mayus(str):
    return str.upper()
frase = str(input("Ingrese una frase: "))
print(mayus(frase))

#16
def ordenar(list):
    orderList = sorted(list)
    return orderList
lista = []
x = 1
fin = int(input("Cuántos números desea agregar? --> "))
while x <= fin:
    n = int(input("Ingrese un número: "))
    lista.append(n)
    x = x+1
print(f"Los números ordenados son: {ordenar(lista)}")

#17
def ordenar(list):
    orderList = sorted(list, reverse=True)
    return orderList
lista = []
x = 1
fin = int(input("Cuántos números desea agregar? --> "))
while x <= fin:
    n = int(input("Ingrese un número: "))
    lista.append(n)
    x = x+1
print(f"Los números ordenados son de manera descendente son: {ordenar(lista)}")

#18
def function(j,z):
    cantidad = 0
    if j < z:
        for i in range(j,z):
            if i % 2 == 0:
                cantidad += 1
    else:
        print("El primer número debe ser el menor.")
    return cantidad
n1 = int(input("Ingrese un número: "))
n2 = int(input("Ingrese un número: "))
print(f"La cantidad de números pares en el intervalo [{n1},{n2}] es de {function(n1,n2)}")
"""
print("Hello world")
