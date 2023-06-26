#Descomentar la parte que se quiera probar

"""
#1
print("Hola Mundo")

#2
n = 5
print(n)

#3
a=15
print(A) #Genera un error ya que la variable A no existe

#4
a = int(input("Variable a: "))
b = int(input("Variable b: "))
n = int(input("Variable n: "))
x = int(input("Variable x: "))
y = int(input("Variable y: "))
print(f"a) {5*a+10*b}")
print(f"b) {b**2}")
print(f"c) {(2*n-1)/(2*n+1)}")
print(f"d) {1*(n**0.5)}")
print(f"e) {2*x-y}")
print(f"f) {(x-y)/(x+y)}")

#5
nombre = input("Ingrese un nombre: ")
print(f"Hola {nombre}, bienvenido!")

#6
print("Ingrese dos números: ")
n1 = input()
n2 = input()
print(n2,n1)

#7
n3 = int(input("Ingrese un número: "))
print(f" Has introducido el número {n3} gracias")

#8
print("Ingrese dos números:")
n4=int(input())
n5=int(input())
print(f"Suma: {n4+n5}")
print(f"Resta: {n4-n5}")
print(f"Multiplicación: {n4*n5}")
print(f"División: {n4/n5}")

#9
print("Ingrese dos números reales:")
n1 = int(input())
n2 = int(input())
division = n1/n2
print(f"Resultado de la división: {division:.2}")

#10
palabra = input("Ingrese una palabra: ")
caracteres= len("hola")
print(f"La cantidad de caracteres de la palabra '{palabra}' es {caracteres} " )

#11 - 12
print("Ingrese dos números: ")
n1= int(input())
n2= int(input())
if n1 == n2:
    print("Iguales")
else:
    print("Distintos")
#En Pseudocódigo habría que utilizar un "Si Enonces FinSi" y verificar si los números ingresados son iguales

#13
print("Ingrese dos números: ")
n1= int(input())
n2= int(input())
if n1 > n2:
    print(f"El número {n1} es el mayor")
else:
    print(f"El número {n2} es el mayor")

#14
montoUSD = float(input("Ingresa el monto el dólares: "))
valorUSD = float(input("Valor del dolar al día de la fecha: "))
montoTotalpesos = valorUSD*montoUSD
comision = (montoTotalpesos*4)/100
print(f"La transacción será de ${montoTotalpesos} y el banco se dejaŕa ${comision} (4% comisión)")

#15
print("Ingrese dos números enteros: ")
n1 = int(input())
n2 = int(input())
if n1>n2:
    print(f"{n1} es mayor")
elif n2>n1:
    print(f"{n2} es mayor")
else:
    print("Los números son iguales")

#16
n1 = int(input("Ingresa un número real: "))
if n1 <= 0:
    print(f"|{n1}|={-n1}")
else:
    print(f"|{n1}|={n1}")

#17
print("Ingresa dos palabras: ")
p1 = input()
p2 = input()
lenp1= len(p1)
lenp2= len(p2)
if lenp1 > lenp2:
    print(f"'{p1}' tiene una mayor longitud")
elif lenp1 < lenp2:
    print(f"'{p2}' tiene una mayor longitud")
else:
    print("Las palabras tienen la misma longitud")

#18
n1 = float(input("Ingrese un número: "))
if n1 >=0:
    print("Positivo")
else:
    print("Negativo")

#19
print("Ingrese dos números: ")
n1 = int(input())
n2 = int(input())
if n1 > n2:
    print(n2,n1)
else:
    print(n1,n2)

#20
print("Ingresa 3 números")
n1 = int(input())
n2 = int(input())
n3 = int(input())
if n1>n2 and n1>n3 and n2>n3:
    print(n3,n2,n1)
elif n2>n1 and n2>n3 and n1>n3:
    print(n3,n1,n2)
elif n3>n1 and n3>n2 and n2>n1:
    print(n1,n2,n3)
elif n1>n2 and n1>n3 and n3>n2:
    print(n2,n3,n1)
elif n2>n1 and n2>n3 and n3>n1:
    print(n1,n3,n2)
elif n3>n1 and n3>n2 and n1>n2:
    print(n2,n1,n3)
"""