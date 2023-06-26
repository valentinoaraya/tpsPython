"""
#1 - Diferencia entre algoritmo y programa
    Si bien ambos hacen referencia a una serie de instrucciones, los algoritmos pueden estar escritos 
    en códigoo en lenguaje natural, mientras que los programas sólo pueden estar escritos en código.

#2 - Tipos de datos en Python
    1. Enteros: Pueden almacenar cualquier valor entero, puede ser de cualquier tamaño.
    2. Flotantes: Puede almacenar cualquier valor decimal, puede ser de cualquier tamaño.
    3. Strings: Es una secuencia de caracteres dentro de comillas ("").
    4. Booleanos: Los datos booleanos incluyen dos valores posibles (True o False).
    5. Diccionario: Datos capaces de almacenar pares clave-valor ({"nombre": "Valentino"}).
    6. Listas y Tuplas: Datos capaces de almacenar una secuencia de datos diferentes. Las tuplas son inmutables.
    7. Conjuntos: Colecciones desordenadas de valores de datos únicos.

#3 - Tipos de datos en C
    1. Int: Representa números enteros con o sin signo, que estarán compuestos por los dígitos del 0 al 9, pudiendo ser precedidos por los signos + o -.
    2. Float: Se emplean para representar números reales (con decimales).
    3. Char: Este tipo de datos se emplea para representar un carácter perteneciente a un determinado código utilizado por el ordenador (normalmente el código ASCII).
    Son muchos menos datos que en python, las diferencias que encontré son que python tiene los diccionarios, listas, tuplas y colecciones y C no. Ambos lenguajes soportan mucha cantidad de tamaño para almacenar datos.

#4
    a) No es correcto porque la función int() puede pasar a entero cadenas de texto pero que no sean decimales, por ejemplo: n = int("341") si se puede pasar.
    b) Si es correcto porque lo que ingresamos es un strings.
    c) Es correcto sumar strings de esta forma, pero si quisieramos sumar enteros habría que pasarlos.
    d) Es correcto sumar strings de esta forma, pero si quisieramos sumar enteros habría que pasarlos.

#5
    a) 3*(23-7)+186 = 234
    b) (185+53)/2+5 = 124
    c) (314+21-117)/2
    d) 

#6
    a) Falso, un algoritmo puede ser implementado en cualquier lenguaje de programación.
    b) Verdadero
    c) Falso, la computadora necesita instrucciones muy específicas.
    d) Verdadero.

#7
    Una definición apropiada es la b.

#8
    a) Utilizaría el tipo de dato Entero para calcular los días. También pueden ser flotantes.
    b) Utilizaría el tipo de dato Entero para calcular los días. También pueden ser flotantes.
    c) Utilizaría el tipo de dato String.
    d) Utilizaría el tipo de dato Float.
    e) Utilizatía el tipo de dato Entero.
    f) Utilizaría el tipo de dato Float.
    g) Utilizatía el tipo de dato String.
    h) Utilizatía el tipo de dato Entero.

#9
    Si el resto de la división de n es igual a cero Entonces
        Mostrar: n es un número par
    Sino
        Mostrar: n es un número impar

#10
n = int(input("Ingrese un número para determinar si es par o impar: "))
if n%2 == 0:
    print(f"{n} es un número par.")
else:
    print(f"{n} es un número impar.")
    
#11
    Primero pediría al usuario ingresar los nombres y guardarlos en una lista.
    Luego crearía una función que tome los nombres de la lista que empiezan con 
    la letra M y los guardaría en una lista nueva.
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
   
   
#12
birthDay = int(input("Ingrese su día de nacimiento: "))
if birthDay > 31 or birthDay < 1:
    print("Error: Día de cumpleaños incorrecto.")
month = str(input("Ingrese su mes de nacimiento: "))
   
if month == "Enero" and birthDay >= 23 :
    print("Su signo es Auarius")
elif month == "Enero" and birthDay < 23:
    print("Su signo es Capricornio")
elif month == "Febrero" and birthDay >= 21 :
    print("Su signo es Piscis")
elif month == "Febrero" and birthDay < 21:
    print("Su signo es Aquiario")
elif month == "Marzo" and birthDay >= 21 :
    print("Su signo es Aries")
elif month == "Marzo" and birthDay < 21:
    print("Su signo es Piscis")
elif month == "Abril" and birthDay >= 20 :
    print("Su signo es Tauro")
elif month == "Abril" and birthDay < 20:
    print("Su signo es Aries")
elif month == "Mayo" and birthDay >= 21 :
    print("Su signo es Geminis")
elif month == "Mayo" and birthDay < 21:
    print("Su signo es Tauro")
elif month == "Junio" and birthDay >= 21 :
    print("Su signo es Cancer")
elif month == "Junio" and birthDay < 21:
    print("Su signo es Geminis")
elif month == "Julio" and birthDay >= 21 :
    print("Su signo es Leo")
elif month == "Julio" and birthDay < 21:
    print("Su signo es Cancer")
elif month == "Agosto" and birthDay >= 23 :
    print("Su signo es Virgo")
elif month == "Agosto" and birthDay < 23:
    print("Su signo es Leo")
elif month == "Septiembre" and birthDay >= 24 :
    print("Su signo es Libra")
elif month == "Septiembre" and birthDay < 24:
    print("Su signo es Virgo")
elif month == "Octubre" and birthDay >= 24 :
    print("Su signo es Escorpio")
elif month == "Octubre" and birthDay < 24:
    print("Su signo es Libra")
elif month == "Noviembre" and birthDay >= 23 :
    print("Su signo es Sagitario")
elif month == "Noviembre" and birthDay < 23:
    print("Su signo es Escorpio")
elif month == "Diciembre" and birthDay >= 23 :
    print("Su signo es Capricornio")
elif month == "Diciembre" and birthDay < 23:
    print("Su signo es Sagitario")
   
#13
    1. La alimentación.
    2. Nombres de alumnos en una escuela.
    3. Las palabras.
    4. El código.
    5. Hojas de materias.
  
#14
    Podría ordenar números de menor a mayor, de mayor a menor, primero los pares luego los impares, o primero los impares y luego los pares.
#Primero los pares luego los impares en Python:
pares = []
impares = []
x=1
while x <=4:
    num = int(input("Ingresa un número: "))
    if num%2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    x += 1
numeros = [*pares, *impares]
print(numeros)

#15
x=1
nums = []
while x <= 4:
    n = int(input("Ingrese un número: "))
    nums.append(n)
    x += 1
print(sorted(nums))
"""