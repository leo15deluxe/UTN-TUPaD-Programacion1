# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.


print ("Hola Mundo!")


# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.


nombre = input("¿Cuál es tu nombre? ")
print(f"Hola {nombre}!")


# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.


nombre = input("¿Cuál es tu nombre?: ")
apellido = input("¿Cuál es tu Apellido?: ")
edad = int(input("¿Cuál es tu edad: "))
residencia = input(" Cual es tu lugar de residencia?: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

import math
radio = float(input("Ingrese el radio del circulo: "))
area = math.pi * radio ** 2 
perimetro = 2 * math.pi * radio
print(f"Area:", {area})
print("Perimetro:", {perimetro})

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

segundos = int(input("Ingrese la cantidad de segundos: "))
hora = segundos // 3600
minutos = (segundos % 3600) // 60
print(f"Equivale a: {hora} hora y {minutos} minutos")


#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

numero = int(input("Ingrese un numero: "))
print("Tabla de multiplicar del", numero)
print(numero, "x 1 =", numero * 1)
print(numero, "x 2 =", numero * 2)
print(numero, "x 3 =", numero * 3)
print(numero, "x 4 =", numero * 4)
print(numero, "x 5 =", numero * 5)
print(numero, "x 6 =", numero * 6)
print(numero, "x 7 =", numero * 7)
print(numero, "x 8 =", numero * 8)
print(numero, "x 9 =", numero * 9)
print(numero, "x 10 =", numero * 10)

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("Ingrese el primer número distinto de 0: "))
num2 = int(input("Ingrese el segundo número distinto de 0: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicacion", multiplicacion)
print("Division", division)


#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:

altura = float(input("Ingresa tu Altura en Metros: "))
peso = float(input("Ingresa tu peso en Kilogramos: "))
imc = peso / (altura **2)
print("Tu indice de masa corporal es: ", imc)

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

celsius = float(input("Ingrese la temperatura en Grados Celsius: "))
fahrenheit = (9 / 5) * celsius + 32
print("La temperatura en grado Fahrenheit es: ", fahrenheit)

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))
promedio = (num1 + num2 + num3) / 3
print("El Promediode los tres numero es: ",promedio)



