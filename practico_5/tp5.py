"""
#1
def cuadrado(n):
    print(locals())
    print(n**2)
cuadrado(2)
# a) Se imprime la variable local n.
# b) Si, hubo cambios, se imprimiero las variables locales dentro de la función.
def cuadrado2(n):
    nombre = "Valentino"
    apellido = "Araya"
    print(locals())
    print(n**2)
cuadrado2(2)

#2
n = 15
def cuadrado(num):
    n = 2
    print(n**2)
    print(locals())
cuadrado(12)

# 3 El código va a imprimir "Es un lindo día", frase es una varibale global.

# 4 El código imprimirá, primero, "3", y luego imprimirá "4" y "1"
x=3
def f():
    y = x+1
    print(x)
    def g():
        x=1
        print(y)
        print(x)
    g()
f()

#5
def areaCuadrado(lado):
    return {"perímetro": lado*4, "área": lado**2 }
n = float(input("Ingrese el lado del cuadrado: "))
print(areaCuadrado(n))

#6 No es una Función es un Procedimiento
def escribir_tabla_multiplicar(n):
    for i in range(11):
        print(f"{n}x{i} = {n*i}")
num = int(input("Ingrese un número entero: "))
escribir_tabla_multiplicar(num)

#7
def cuadrante(x,y):
    if x == 0 and y == 0:
        return 0
    elif x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
num1 = int(input("Ingrese X: "))
num2 = int(input("Ingrese Y: "))
cuadrante = cuadrante(num1, num2)
if cuadrante == 0:
    print("El punto está en el origen.")
elif cuadrante == 1:
    print("El punto está en el primer cuadrante.")
elif cuadrante == 2:
    print("El punto está en el segundo cuadrante.")
elif cuadrante == 3:
    print("El punto está en el tercer cuadrante.")
elif cuadrante == 4:
    print("El punto está en el cuarto cuadrante.")

----- ARCHIVOS DE TEXTO -----

#8
archivo = open("punto8.txt", "r")
lineas = archivo.readlines()
archivo.close()
cantidadLineas = 0
for element in lineas:
    cantidadLineas += 1
    print(element)
print(f"El en archivo hay {cantidadLineas} lúneas.")

#9
archivo = open("numeros.txt", "a")
for i in range(10):
    n = int(input("Ingrese un número entero: "))
    archivo.write(f"{n}n")
archivo.close()

#10
archivo = open("colores.txt", "a")
for i in range(5):
    color = str(input("Ingrese un color: "))
    archivo.write(f"{color}\n")
archivo.close()

#11
import random
contadorCincos = 0
archivoNumeros = open("números_punto11.txt", "w")
for i in range(10):
    archivoNumeros.write(f"{random.randint(1,10)} ")
archivoNumeros.close()
newArchivoNumeros = open("números_punto11.txt", "r")
numerosString = newArchivoNumeros.read()
newArchivoNumeros.close()
numeros = numerosString.split(" ")
for n in numeros:
    if n == "5":
        contadorCincos += 1
if contadorCincos == 1:
    print(f"El número 5 se repite {contadorCincos} vez.")
else:
    print(f"El número 5 se repite {contadorCincos} veces.")

#12
import random
archivoNumeros = open("números_punto11.txt", "w")
fin = int(input("Cuántos números desea generar? --> "))
for i in range(fin):
    archivoNumeros.write(f"{random.randint(1,10)} ")
archivoNumeros.close()
newArchivoNumeros = open("números_punto11.txt", "r")
numerosString = newArchivoNumeros.read()
newArchivoNumeros.close()
numeros = numerosString.split(" ")
newNumeros = []
for n in range(len(numeros)-1):
    newNumeros.append(int(numeros[n]))
sumaTotal = 0
for n in newNumeros:
    sumaTotal = sumaTotal + n
promedio = sumaTotal/len(newNumeros)
print(f"La suma de todos ellos es {sumaTotal} y el promedio {promedio}")

----- FUNCIONES -----

#13
def potencia(base, exponente):
    return base**exponente
b = float(input("Ingrese la base: "))
e = float(input("Ingrese el exponente: "))
print(potencia(b,e))

#14
def cantidadLetra(frase,letra):
    contador = 0
    for l in frase:
        if l == letra.upper() or l == letra.lower():
            contador += 1
    return contador
f = str(input("Ingrese una frase: "))
l = str(input("Ingrese una letra: "))
print(f"La letra {l} aparece {cantidadLetra(f,l)} veces en la frase ingresada.")

#15
def cantidadCaracter(listaPalabras, caracter):
    listaCantidad = []
    for palabra in listaPalabras:
        contadorCaracter = 0
        for c in palabra:
            if c == caracter:
                contadorCaracter += 1
        texto = f"{palabra}: {contadorCaracter}"
        listaCantidad.append(texto)
    return listaCantidad

print("Ingrese 10 palabras (1 por línea y sin espacios): ")
palabras = []
for i in range(10):
    palabra = str(input(f"{i+1}°: "))
    if " " in palabra:
        print("Error: Debe ingresar una palabra sin espacios.")
    else:
        palabras.append(palabra)
car = str(input("Ingrese el caracter: "))
print(cantidadCaracter(palabras, car))

#16
def parImpar(n):
    if n %2 == 0:
        return True
    else:
        return False    
num = int(input("Ingrese un número: "))
print(parImpar(num))

#17
def triangulo(car, veces):
    cantidad = veces
    for n in range(veces):
        print(car*cantidad)
        cantidad -= 1
caracter = str(input("Ingrese un caracter: "))
cantidad = int(input("Ingrese el ancho del triángulo: "))
triangulo(caracter, cantidad)

#18
def es_primo(num):
    divisores = [2,3,4,5,6,7,8,9]
    newDivisors = []
    restos = []
    if num in divisores:
        for n in divisores:
            if num != n:
                newDivisors.append(n)
        for i in newDivisors:
            restos.append(num%i)
        if 0 in restos:
            return False
        else:
            return True
    else:
        for i in divisores:
            restos.append(num%i)
        if 0 in restos:
            return False
        else:
            return True
n = int(input("Ingrese un número para determinar si es primo o no: "))
print(es_primo(n))

#19
def mayorMenor(n1,n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return "="
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
print(mayorMenor(num1,num2))

#20
def promedio(numbers):
    sumaTotal = 0
    for n in numbers:
        sumaTotal = sumaTotal + n
    promedio = sumaTotal/len(numbers)
    return promedio
numeros = []
fin = int(input("Cuántos números desea agregar? --> "))
for i in range(fin):
    n = int(input("Ingrese un número: "))
    numeros.append(n)
print(promedio(numeros))

#21
def binarios(b):
    ceros = 0
    unos = 0
    for c in b:
        if c == "0":
            ceros += 1
        if c == "1":
            unos += 1
    if ceros == unos:
        return True
    else:
        return False
binario = str(input("Ingrese el número: "))
binarioFilter = ""
for n in binario:
    if n == "0" or n == "1":
        binarioFilter += n 
print("Si has introducido números disitntos de 0 o 1, se filtran y quedan solo ceros y unos.")
print(binarios(binarioFilter))

#22
def posicionCaracter(frase,caracter):
    posicion = -1
    for i in range(len(frase)):
        if frase[i] == caracter:
            posicion = i
            break
    return posicion
frase = str(input("Ingrese una frase: "))
caracter = str(input("Ingrese un caracter: "))
print(posicionCaracter(frase, caracter))

#23
import random
def crearArchivo(nombre):
    archivo = open(f"{nombre}.txt", "a+")
    for n in range(250):
        archivo.write(f"{random.randint(0,100)} ")
    archivo.close()
name = str(input("Ingresa el nombre del archivo: "))
crearArchivo(name)

#24
import random
def crearArchivo(nombre, a, b):
    archivo = open(f"{nombre}.txt", "a+")
    for n in range(250):
        archivo.write(f"{random.randint(a,b)} ")
    archivo.close()
name = str(input("Ingresa el nombre del archivo: "))
num1 = int(input("Ingresa el numero: "))
num2 = int(input("Ingresa el numero: "))
crearArchivo(name, num1, num2)

#25
def rectangulo(longitud):
    print("#"*longitud)
    cantidadEspacios = longitud-2
    for n in range(longitud-1):
        print("#"+f"{' '*cantidadEspacios}"+"#")
    print("#"*longitud)
leng = int(input("Ingrese la longitud del rectángulo"))
rectangulo(leng)

#26
def cobrar(monto, metodo_pago):
    newMetodo = metodo_pago.upper()
    newMonto = monto
    descuento = 0
    if newMetodo == "DÉBITO" or newMetodo == "DEBITO":
        newMonto = monto-((10/100)*monto)
        descuento = 10
        return [newMonto, descuento]
    elif newMetodo == "CONTADO-EFECTIVO" or newMetodo == "CONTADO" or newMetodo == "EFECTIVO" or newMetodo == "CONTADO EFECTIVO":
        newMonto = monto-((13/100)*monto)
        descuento = 13
        return [newMonto, descuento]
    elif newMetodo == "TARJETA":
        newMonto = monto+((4/100)*monto)
        descuento = 4
        return [newMonto, descuento]
    else:
        print("El Método de pago no existe.")
print(" ")
print(" ")
total = float(input("Ingrese el monto de su compra: $"))
print(" ")
print("---- FORMAS DE PAGO ----")
print("Débito --> 10% descuento.")
print("Contado-Efectivo --> 13% descuento.")
print("Tarjeta --> 4% recargo.")
print(" ")
fomraDePago = str(input("Ingrese el método de pago: "))
print(" ")
descuento = cobrar(total, fomraDePago)
if descuento[1] >= 10:
    print(f"El total de su compra es de ${descuento[0]} con un descuento de {descuento[1]}%")
elif descuento[1] < 10:
    print(f"El total de su compra es de ${descuento[0]} con un aumento de {descuento[1]}% debido a que su pago fué con tarjeta.")

#27 
def cobrar(monto, metodo_pago):
    newMetodo = metodo_pago.upper()
    newMonto = monto
    descuento = 0
    if newMetodo == "DÉBITO" or newMetodo == "DEBITO":
        newMonto = monto-((10/100)*monto)
        descuento = 10
        return [newMonto, descuento]
    elif newMetodo == "CONTADO-EFECTIVO" or newMetodo == "CONTADO" or newMetodo == "EFECTIVO" or newMetodo == "CONTADO EFECTIVO":
        newMonto = monto-((13/100)*monto)
        descuento = 13
        return [newMonto, descuento]
    elif newMetodo == "TARJETA":
        print(" ")
        print("---- SELECCIONE TIPO DE TARJETA ----")
        print("Visa --> 5% recargo.")
        print("Master --> 7% recargo.")
        print("American Express --> 9% recargo.")
        print(" ")
        tipoTarjeta = str(input("Tipo de tarjeta: "))
        if tipoTarjeta.upper() == "VISA":
            newMonto = monto+((5/100)*monto)
            descuento = 5
        elif tipoTarjeta.upper() == "MASTER":
            newMonto = monto+((7/100)*monto)
            descuento = 7
        elif tipoTarjeta.upper() == "AMERICAN EXPRESS" or tipoTarjeta.upper() == "AMERICAN":
            newMonto = monto+((9/100)*monto)
            descuento = 9
        return [newMonto, descuento]
    else:
        print("El Método de pago no existe.")
print(" ")
print(" ")
total = float(input("Ingrese el monto de su compra: $"))
print(" ")
print("---- FORMAS DE PAGO ----")
print("Débito --> 10% descuento.")
print("Contado-Efectivo --> 13% descuento.")
print("Tarjeta --> 4% recargo.")
print(" ")
fomraDePago = str(input("Ingrese el método de pago: "))
print(" ")
descuento = cobrar(total, fomraDePago)
if descuento[1] >= 10:
    print(f"El total de su compra es de ${descuento[0]} con un descuento de {descuento[1]}%")
elif descuento[1] < 10:
    if descuento[1] == 5:
        print(f"El total de su compra es de ${descuento[0]} con un aumento de {descuento[1]}% debido a que su pago fué con tarjeta Visa.")
    elif descuento[1] == 7:
        print(f"El total de su compra es de ${descuento[0]} con un aumento de {descuento[1]}% debido a que su pago fué con tarjeta Master.")
    elif descuento[1] == 9:
        print(f"El total de su compra es de ${descuento[0]} con un aumento de {descuento[1]}% debido a que su pago fué con tarjeta American Express.")

#28
def intereses(monto, tarjeta, cuotas):
    montoMensual = 0
    recargo = 0
    total = 0
    tasaMensual = 0
    if tarjeta == "1" and cuotas == "3":
        montoMensual = ((4/100)*monto)
        tasaMensual = (monto/int(cuotas)) + montoMensual
        recargo = 4
        total = monto + montoMensual*3
    elif tarjeta == "1" and cuotas == "6":
        montoMensual = ((4.5/100)*monto)
        tasaMensual = (monto/int(cuotas)) + montoMensual
        recargo = 4.5
        total = monto + montoMensual*6
    elif tarjeta == "1" and cuotas == "12":
        montoMensual = ((5/100)*monto)
        tasaMensual = (monto/int(cuotas)) + montoMensual
        recargo = 5
        total = monto + montoMensual*12
    elif tarjeta == "2" and cuotas == "3":
        montoMensual = ((3/100)*monto)
        tasaMensual = (monto/int(cuotas)) + montoMensual
        recargo = 3
        total = monto + montoMensual*3
    elif tarjeta == "2" and cuotas == "6":
        montoMensual = ((4/100)*monto)
        tasaMensual = (monto/int(cuotas)) + montoMensual
        recargo = 4
        total = monto + montoMensual*6
    elif tarjeta == "2" and cuotas == "12":
        montoMensual = ((5/100)*monto)
        tasaMensual = (monto/int(cuotas)) + montoMensual
        recargo = 5
        total = monto + montoMensual*12
    elif tarjeta == "3" and cuotas == "3":
        montoMensual = ((3.8/100)*monto)
        tasaMensual = (monto/int(cuotas)) + montoMensual
        recargo = 3.8
        total = monto + montoMensual*3
    elif tarjeta == "3" and cuotas == "6":
        montoMensual = ((5/100)*monto)
        tasaMensual = (monto/int(cuotas)) + montoMensual
        recargo = 5
        total = monto + montoMensual*6
    elif tarjeta == "3" and cuotas == "12":
        montoMensual = ((5.3/100)*monto)
        tasaMensual = (monto/int(cuotas)) + montoMensual
        recargo = 5.3
        total = monto + montoMensual*12
    return [total, recargo, tasaMensual, monto, montoMensual]

tarjetasAceptadas = ["1","2","3"]
cuotasAceptadas = ["3","6","12"]
print(" ")
print("---> TARJETAS ACEPTADAS <---")
print("Tarjeta 1 --> 3 cuotas = +4% mensual, 6 cuotas = +4.5% mensual, 12 cuotas = +5% menusal.")
print("Tarjeta 2 --> 3 cuotas = +3% mensual, 6 cuotas = +4% mensual, 12 cuotas = +5% mensual.")
print("Tarjeta 3 --> 3 cuotas = +3.8% mensual, 6 cuotas = +5% mensual, 12 cuotas = +5.3% mensual.")
print(" ")
total = float(input("Ingrese el monto de su compra: $"))
tipoTarjeta = str(input("Ingrese el tipo de tarjeta: "))
cuotas = str(input("Ingrese en la cantidad de cuotas que desea: "))
print(" ")
if tipoTarjeta not in tarjetasAceptadas or cuotas not in cuotasAceptadas:
    print("ERROR: Selección de tarjeta o cuotas incorrecta.")
else:
    monto = intereses(total, tipoTarjeta, cuotas)
    print("---> PARA LA TARJETA ELEGIDA CON LAS CUOTAS ELEGIDAS <---")
    print(f"- Total del producto SIN intereses = ${monto[3]}")
    print(f"- Cuotas = {cuotas}")
    print(f"- Tasa Mensual = {monto[1]}% = ${monto[4]} del total ---> ${monto[2]} x mes ---> ${monto[4]*int(cuotas)} de intereses.")
    print(f"- Total del producto CON intereses = ${monto[0]}")
    print(" ")

    

#29
def intereses(monto, tarjeta, cuotas):
    montoMensual = 0
    recargo = 0
    total = 0
    tasaMensual = 0
    if tarjeta.upper() == "VISA" and cuotas == "3":
        montoMensual = ((4/100)*monto)
        tasaMensual = (monto/int(cuotas)) + montoMensual
        recargo = 4
        total = monto + montoMensual*3
    elif tarjeta.upper() == "VISA" and cuotas == "6":
        montoMensual = ((4.5/100)*monto)
        tasaMensual = (monto/int(cuotas)) + montoMensual
        recargo = 4.5
        total = monto + montoMensual*6
    elif tarjeta.upper() == "VISA" and cuotas == "12":
        montoMensual = ((5/100)*monto)
        tasaMensual = (monto/int(cuotas)) + montoMensual
        recargo = 5
        total = monto + montoMensual*12
    elif tarjeta.upper() == "MASTER" and cuotas == "3":
        montoMensual = ((3/100)*monto)
        tasaMensual = (monto/int(cuotas)) + montoMensual
        recargo = 3
        total = monto + montoMensual*3
    elif tarjeta.upper() == "MASTER" and cuotas == "6":
        montoMensual = ((4/100)*monto)
        tasaMensual = (monto/int(cuotas)) + montoMensual
        recargo = 4
        total = monto + montoMensual*6
    elif tarjeta.upper() == "MASTER" and cuotas == "12":
        montoMensual = ((5/100)*monto)
        tasaMensual = (monto/int(cuotas)) + montoMensual
        recargo = 5
        total = monto + montoMensual*12
    elif (tarjeta.upper() == "AMERICAN EXPRESS" or tarjeta.upper() == "AMERICAN") and cuotas == "3":
        montoMensual = ((3.8/100)*monto)
        tasaMensual = (monto/int(cuotas)) + montoMensual
        recargo = 3.8
        total = monto + montoMensual*3
    elif (tarjeta.upper() == "AMERICAN EXPRESS" or tarjeta.upper() == "AMERICAN") and cuotas == "6":
        montoMensual = ((5/100)*monto)
        tasaMensual = (monto/int(cuotas)) + montoMensual
        recargo = 5
        total = monto + montoMensual*6
    elif (tarjeta.upper() == "AMERICAN EXPRESS" or tarjeta.upper() == "AMERICAN") and cuotas == "12":
        montoMensual = ((5.3/100)*monto)
        tasaMensual = (monto/int(cuotas)) + montoMensual
        recargo = 5.3
        total = monto + montoMensual*12
    return [total, recargo, tasaMensual, monto, montoMensual]

def cobrar(monto, metodo_pago):
    newMetodo = metodo_pago.upper()
    newMonto = monto
    descuento = 0
    if newMetodo == "DÉBITO" or newMetodo == "DEBITO":
        newMonto = monto-((10/100)*monto)
        descuento = 10
        return [newMonto, descuento]
    elif newMetodo == "CONTADO-EFECTIVO" or newMetodo == "CONTADO" or newMetodo == "EFECTIVO" or newMetodo == "CONTADO EFECTIVO":
        newMonto = monto-((13/100)*monto)
        descuento = 13
        return [newMonto, descuento]
    elif newMetodo == "TARJETA":
        tarjetasAceptadas = ["VISA","MASTER","AMERICAN", "AMERICAN EXPRESS"]
        cuotasAceptadas = ["3","6","12"]
        print(" ")
        print("---- SELECCIONE TIPO DE TARJETA ----")
        print("Visa --> 3 cuotas = +4% mensual, 6 cuotas = +4.5% mensual, 12 cuotas = +5% menusal.")
        print("Master --> 3 cuotas = +3% mensual, 6 cuotas = +4% mensual, 12 cuotas = +5% mensual.")
        print("American Express --> 3 cuotas = +3.8% mensual, 6 cuotas = +5% mensual, 12 cuotas = +5.3% mensual.")
        print(" ")
        tipoTarjeta = str(input("Tipo de tarjeta: "))
        cuotas = str(input("Ingrese en la cantidad de cuotas que desea: "))
        if tipoTarjeta.upper() not in tarjetasAceptadas or cuotas not in cuotasAceptadas:
            print("ERROR: Selección de tarjeta o cuotas incorrecta.")
        else:
            newTotal = intereses(monto, tipoTarjeta, cuotas)
            print(" ")
            print(f"---> PARA TARJETA {tipoTarjeta.upper()} EN {cuotas} CUOTAS <---")
            print(f"- Total del producto SIN intereses = ${newTotal[3]}")
            print(f"- Cuotas = {cuotas}")
            print(f"- Tasa Mensual = {newTotal[1]}% = ${newTotal[4]} del total ---> ${newTotal[2]} x mes ---> ${newTotal[4]*int(cuotas)} de intereses.")
            print(f"- Total del producto CON intereses = ${newTotal[0]}")
            print(" ")
    else:
        print("El Método de pago no existe.")
print(" ")
total = float(input("Ingrese el monto de su compra: $"))
print(" ")
print("---- FORMAS DE PAGO ----")
print("Débito --> 10% descuento.")
print("Contado-Efectivo --> 13% descuento.")
print("Tarjeta --> Dependiendo de la tarjeta y cuotas.")
print(" ")
fomraDePago = str(input("Ingrese el método de pago: "))
print(" ")
if fomraDePago.upper() == "DÉBITO" or fomraDePago.upper() == "DEBITO" or fomraDePago.upper() == "CONTADO-EFECTIVO" or fomraDePago.upper() == "CONTADO" or fomraDePago.upper() == "EFECTIVO" or fomraDePago.upper() == "CONTADO EFECTIVO":
    descuento = cobrar(total, fomraDePago)
    if descuento[1] >= 10:
        print(f"El total de su compra es de ${descuento[0]} con un descuento de {descuento[1]}%")
elif fomraDePago.upper() == "TARJETA":
    cobrar(total, fomraDePago)
"""

#6 No es una Función es un Procedimiento
def escribir_tabla_multiplicar(n):
    for i in range(11):
        print(f"{n}x{i} = {n*i}")
num = int(input("Ingrese un número entero: "))
escribir_tabla_multiplicar(num)