# Ejercicio 1 - "Caja del Kiosco"

# Requisitos
# 1. Pedir nombre del cliente (Solo letras, validar con .isalpha () en while)
# 2. Pedir cantidad de productos a comprar (numero entero positivo, validar con .isdigit() en while)
# 3. Por cada producto (usar for):
#   Pedir Precio (entero, validar .isdigit())
#   pedir si tiene descuento S/N (validar con while, aceptar s o n en cualquier mayúscula/minúscula). 
#   Si tiene descuento: aplicar 10% al precio de ese producto.
# 4. Al final mostar:
#   Total sin descuento
#   Total con descuentos 
#   Ahorro total
#   Promedio por producto (usar float y formatear con :.2f, ejem:)
# x = 3.14159
# print(f"{x:.2f}")


# Nombre del cliente
nombre = input("Ingrese el nombre del cliente: ")
while not nombre.isalpha():
    nombre = input("Ingrese el nombre del cliente: ")

# Cantidad de productos
cantidad = input("Cantidad de productos: ")
while not cantidad.isdigit() or int(cantidad) == 0:
    cantidad = input("Cantidad de productos: ")
cantidad = int(cantidad)

# 3. Productos
total_sin = 0
total_con = 0

for i in range(1, cantidad + 1):
    precio = input(f"Producto {i} - Precio: ")
    while not precio.isdigit():
        precio = input(f"Producto {i} - Precio: ")
    precio = int(precio)

    desc = input(f"Producto {i} - Descuento (S/N): ")
    while desc.lower() not in ("s", "n"):
        desc = input(f"Producto {i} - Descuento (S/N): ")

    total_sin += precio
    if desc.lower() == "s":
        total_con += precio * 0.9
    else:
        total_con += precio

# 4. Resultados
ahorro = total_sin - total_con
promedio = total_con / cantidad

print(f"\nTotal sin descuentos: ${total_sin}")
print(f"Total con descuentos: ${total_con:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")




# Ejercicio 2 — “Acceso al Campus y Menú Seguro”

# Objetivo: Login con intentos + menú de acciones con validación estricta.
# Requisitos
# 1. Definir credenciales fijas en el código:
#   o usuario correcto: "alumno"
#   o clave correcta: "python123"
# 2. Permitir máximo 3 intentos para ingresar usuario y clave.
# 3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar.
# 4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir:
#   1. Ver estado de inscripción (mostrar “Inscripto”)
#   2. Cambiar clave (pedir nueva clave y confirmación; deben coincidir)
#   3. Mostrar mensaje motivacional (1 frase)
#   4. Salir
# 5. Validación del menú:
#   o Debe ser número (.isdigit())
#   o Debe estar entre 1 y 4


# Credenciales
usuario_correcto = "alumno"
clave_correcta = "Clave2026"

intentos = 0
login_exitoso = False

# Permitir con máximo 3 intentos
while intentos < 3:
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso Concedido\n")
        login_exitoso = True
        break
    else:
        intentos += 1
        print("Credenciales invalidadas\n")

# Si falla 3 veces
if not login_exitoso:
    print("Cuenta bloqueada")
else:
    # Menú
    while True:
        print("\n--- MENÚ ---")
        print("1. Ver estado de inscripción")
        print("2. Cambiar clave")
        print("3. Mensaje motivacional")
        print("4. Salir")

        opcion = input("Elegí una opción: ")

        # Validación: debe ser número
        if not opcion.isdigit():
            print("Error: Debe ingresar un número")
            continue

        opcion = int(opcion)

        # Validación: rango
        if opcion < 1 or opcion > 4:
            print("Error: Opción fuera de rango")
            continue

        # Opciones
        if opcion == 1:
            print("Estado: Inscripto")

        elif opcion == 2:
            while True:
                nueva_clave = input("Nueva clave: ")
                
                if len(nueva_clave) < 6:
                    print("Error: mínimo 6 caracteres")
                    continue
                confirmar = input("Confirmar clave: ")
                if nueva_clave == confirmar:
                    clave_correcta = nueva_clave
                    print("Clave cambiada Correctamente\n")
                    break
                else:
                    print("Error: las claves deben coincidir\n")



        elif opcion == 3:
            print("Cada día es una nueva oportunidad para superarte.")

        elif opcion == 4:
            print("Saliendo del sistema...")
            break









#  Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”

# Contexto
# Hay 2 días de atención: Lunes y Martes.
# Cada día tiene cupos fijos:
#   • Lunes: 4 turnos
#   • Martes: 3 turnos

# Reglas
# 1. Pedir nombre del operador (solo letras).
# 2. Menú repetitivo hasta salir:
#       1. Reservar turno
#       2. Cancelar turno (por nombre)
#       3. Ver agenda del día
#       4. Ver resumen general
#       5. Cerrar sistema

# 3. Reservar:
#       o Elegir día (1=Lunes, 2=Martes).
#       o Pedir nombre del paciente (solo letras).
#       o Verificar que no esté repetido en ese día (comparando con las variables ya cargadas).
#       o Guardar en el primer espacio libre (ej. lunes1, lunes2…).
# 4. Cancelar:
#       o Elegir día.
#       o Pedir nombre del paciente (solo letras).
#       o Si existe, cancelar y dejar el espacio vacío ("").

# 5. Ver agenda del día:
#       o Mostrar los turnos del día en orden (Turno 1..N), indicando “(libre)” si está vacío.
# 6. Resumen general:
#       o Turnos ocupados y disponibles por día.
#       o Día con más turnos (o empate).

# Restricciones
#       •  No listas, no diccionarios, no sets, no tuplas.
#       •  Se permite usar "" como “vacío”.
#       •  Validaciones con .isalpha() y .isdigit() (sin try/except).

# Agenda
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

# Operador ---
operador = input("Ingrese nombre del operador: ")

while not operador.isalpha():
    print("Error. Solo letras.")
    operador = input("Ingrese nombre del operador: ")

# Menú 
opcion = ""

while opcion != "5":
    print("\n--- MENÚ ---")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("Seleccione opción: ")

# RESERVAR
    if opcion == "1":
        dia = input("Día (1=Lunes, 2=Martes): ")

        while dia != "1" and dia != "2":
            print("Error. Día inválido.")
            dia = input("Día (1=Lunes, 2=Martes): ")

        nombre = input("Nombre del paciente: ")
        while not nombre.isalpha():
            print("Error. Solo letras.")
            nombre = input("Nombre del paciente: ")

        if dia == "1":
# repetido
            if nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre == lunes4:
                print("Paciente ya tiene turno en Lunes.")
            else:
                if lunes1 == "":
                    lunes1 = nombre
                elif lunes2 == "":
                    lunes2 = nombre
                elif lunes3 == "":
                    lunes3 = nombre
                elif lunes4 == "":
                    lunes4 = nombre
                else:
                    print("No hay cupos en Lunes.")
        else:
            if nombre == martes1 or nombre == martes2 or nombre == martes3:
                print("Paciente ya tiene turno en Martes.")
            else:
                if martes1 == "":
                    martes1 = nombre
                elif martes2 == "":
                    martes2 = nombre
                elif martes3 == "":
                    martes3 = nombre
                else:
                    print("No hay cupos en Martes.")

# CANCELAR 
    elif opcion == "2":
        dia = input("Día (1=Lunes, 2=Martes): ")

        while dia != "1" and dia != "2":
            print("Error. Día inválido.")
            dia = input("Día (1=Lunes, 2=Martes): ")

        nombre = input("Nombre del paciente: ")
        while not nombre.isalpha():
            print("Error. Solo letras.")
            nombre = input("Nombre del paciente: ")

        encontrado = False

        if dia == "1":
            if lunes1 == nombre:
                lunes1 = ""
                encontrado = True
            elif lunes2 == nombre:
                lunes2 = ""
                encontrado = True
            elif lunes3 == nombre:
                lunes3 = ""
                encontrado = True
            elif lunes4 == nombre:
                lunes4 = ""
                encontrado = True
        else:
            if martes1 == nombre:
                martes1 = ""
                encontrado = True
            elif martes2 == nombre:
                martes2 = ""
                encontrado = True
            elif martes3 == nombre:
                martes3 = ""
                encontrado = True

        if encontrado:
            print("Turno cancelado.")
        else:
            print("Paciente no encontrado.")

# AGENDA
    elif opcion == "3":
        dia = input("Día (1=Lunes, 2=Martes): ")

        while dia != "1" and dia != "2":
            print("Error. Día inválido.")
            dia = input("Día (1=Lunes, 2=Martes): ")

        if dia == "1":
            print("\nAgenda Lunes:")
            print("1:", lunes1 if lunes1 != "" else "(libre)")
            print("2:", lunes2 if lunes2 != "" else "(libre)")
            print("3:", lunes3 if lunes3 != "" else "(libre)")
            print("4:", lunes4 if lunes4 != "" else "(libre)")
        else:
            print("\nAgenda Martes:")
            print("1:", martes1 if martes1 != "" else "(libre)")
            print("2:", martes2 if martes2 != "" else "(libre)")
            print("3:", martes3 if martes3 != "" else "(libre)")

# RESUMEN
    elif opcion == "4":
        ocupados_lunes = 0
        ocupados_martes = 0

        if lunes1 != "": ocupados_lunes += 1
        if lunes2 != "": ocupados_lunes += 1
        if lunes3 != "": ocupados_lunes += 1
        if lunes4 != "": ocupados_lunes += 1

        if martes1 != "": ocupados_martes += 1
        if martes2 != "": ocupados_martes += 1
        if martes3 != "": ocupados_martes += 1

        print("\n--- RESUMEN ---")
        print("Lunes: ocupados =", ocupados_lunes, "| libres =", 4 - ocupados_lunes)
        print("Martes: ocupados =", ocupados_martes, "| libres =", 3 - ocupados_martes)

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Hay empate en cantidad de turnos.")

# INVÁLIDA 
    elif opcion != "5":
        print("Opción inválida.")

print("Sistema cerrado.")




# Ejercicio 4 — “Escape Room: La Bóveda”
# Historia
# Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo limitados.
# Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.


# Variables iniciales (NO se piden por teclado)
#       • energia = 100
#       • tiempo = 12
#       • cerraduras_abiertas = 0
#       • alarma = False
#       • codigo_parcial = ""
# Validaciones obligatorias
#       • No usar try/except.
#       • Pedir nombre del agente y validar con .isalpha() en un while.
#       • Validar opciones del menú y cualquier número pedido con .isdigit() en un while.
#       • El juego debe funcionar con estructuras secuenciales, condicionales y 
#           repetitivas (puede usar funciones propias del lenguaje como .lower(), len(), formateo, etc.).


# Regla anti-spam (muy importante)
# Para evitar que el jugador gane eligiendo “Forzar cerradura” 3 veces seguidas al 
# iniciar:

#  Si el jugador elige Forzar cerradura (opción 1) 3 veces seguidas, entonces:
#       • se cobra el costo normal (-20 energía, -2 tiempo),
#       • NO abre cerradura, y
#       • se activa la alarma automáticamente (alarma = True) porque “la cerradura se trabó”.
# Si el jugador elige opción 2 o 3, se corta la racha de “forzar seguidas”.

# Menú de acciones (se repite mientras el juego siga)
# El juego continúa mientras:
#       • energia > 0, tiempo > 0, cerraduras_abiertas < 3
#       • y no esté bloqueado por alarma.
# En cada turno mostrar el estado y el siguiente menú:
# 1. Forzar cerradura (costo: -20 energía, -2 tiempo)
#       o Si la energía está por debajo de 40, hay “riesgo de alarma”:
#           ▪ pedir un número 1-3 (validado). Si elige 3 → alarma=True.
#       o Si no hay alarma, abre 1 cerradura.
#       o Regla anti-spam: si es la 3ra vez seguida forzando, se activa alarma y no abre.
# 2. Hackear panel (costo: -10 energía, -3 tiempo)
#       o Debe usar un for de 4 pasos mostrando progreso.
#       o En cada paso sumar una letra al codigo_parcial (por ejemplo “A”).
#       o Si len(codigo_parcial) >= 8, se abre automáticamente 1 cerradura si todavía faltan.
# 3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra)
# Regla de bloqueo por alarma
#       • Si alarma == True y tiempo <= 3 y todavía no se abrió la bóveda, el sistema se bloquea y se pierde.

# Condiciones de fin
#       • Si cerraduras_abiertas == 3 → VICTORIA
#       • Si energia <= 0 o tiempo <= 0 → DERROTA
#       • Si se bloquea por alarma → DERROTA (bloqueo)


energia = 100
tiempo = 12
cerraduras = 0
alarma = False
codigo = ""
racha_forzar = 0

# Nombre del agente
nombre = input("Nombre del agente: ")
while not nombre.isalpha():
    nombre = input("Solo letras. Ingresá tu nombre: ")

# Juego
while energia > 0 and tiempo > 0 and cerraduras < 3:

    print("\n--- ESTADO ---")
    print("Agente:", nombre)
    print("Energía:", energia, "| Tiempo:", tiempo)
    print("Cerraduras:", cerraduras, "| Alarma:", alarma)

    # Menú
    opcion = input("1-Forzar  2-Hackear  3-Descansar: ")
    while not opcion.isdigit() or opcion not in ["1", "2", "3"]:
        opcion = input("Elegí 1, 2 o 3: ")

    # OPCIÓN 1: FORZAR
    if opcion == "1":
        racha_forzar += 1

        # Anti-spam
        if racha_forzar == 3:
            print("¡Se trabó la cerradura!")
            energia -= 20
            tiempo -= 2
            alarma = True

        else:
            # Riesgo de alarma
            if energia < 40:
                num = input("Elegí un número (1-3): ")
                while not num.isdigit() or num not in ["1", "2", "3"]:
                    num = input("Número válido (1-3): ")
                if num == "3":
                    alarma = True
                    print("¡Se activó la alarma! ")

            energia -= 20
            tiempo -= 2

            if not alarma:
                cerraduras += 1
                print("Abriste una cerradura ")

    # OPCIÓN 2: HACKEAR
    elif opcion == "2":
        racha_forzar = 0
        energia -= 10
        tiempo -= 3

        print("Hackeando...")
        for i in range(4):
            print("Paso", i + 1)
            codigo += "A"

        if len(codigo) >= 8 and cerraduras < 3:
            cerraduras += 1
            print("¡Hackeo exitoso! ")

    # OPCIÓN 3: DESCANSAR
    elif opcion == "3":
        racha_forzar = 0
        energia += 15
        if energia > 100:
            energia = 100

        tiempo -= 1

        if alarma:
            energia -= 10

        print("Descansaste ")

    # Bloqueo por alarma
    if alarma and tiempo <= 3 and cerraduras < 3:
        print("\n sistema bloqueado por alarma")
        break

# RESULTADO FINAL
if cerraduras == 3:
    print("\n¡GANASTE!")
elif energia <= 0 or tiempo <= 0:
    print("\nPerdiste por falta de recursos")
else:
    print("\nPerdiste por bloqueo")





# Ejercicio 5 — “Escape Room:"La Arena del Gladiador" 
# 1. Descripción del Escenario 
# Vas a desarrollar un simulador de batalla por turnos en Python. El programa enfrentará a un 
# usuario (Gladiador) contra un oponente controlado por la computadora (Enemigo). El 
# objetivo es reducir los puntos de vida del oponente a cero antes de que él lo haga contigo. 
# Este ejercicio evalúa el uso de variables (int, float, string, boolean), estructuras de 
# control (if/elif/else), ciclos (while y for) y validación de datos estricta. 
# 2. Requerimientos Técnicos 
# A. Tipos de Datos 
# Debes utilizar obligatoriamente los siguientes tipos de datos para las variables del juego: 
#       • • String: Para el nombre del jugador. 
#       • • Int: Para los Puntos de Vida (HP) y cantidad de pociones. 
#       • • Float: Para el cálculo del daño (ej: un golpe crítico multiplica el ataque por 1.5). 
#       • • Boolean: Para controlar si el juego sigue activo o quién tiene el turno. 

# B. Reglas de Validación (¡Importante!) 
#       • • No está permitido usar bloques try / except. 
#       • • Para validar texto, debes usar el método .isalpha() dentro de un ciclo while. 
#       • • Para validar números, debes usar el método .isdigit() dentro de un ciclo while. 

# 3. Flujo del Programa 
# Paso 1: Configuración del Personaje 
# El programa inicia pidiendo el nombre del Gladiador. 
#       • • Validación: El nombre solo puede contener letras. Si el usuario ingresa números, 
# símbolos o lo deja vacío, el programa debe decir "Error: Solo se permiten letras" y volver a 
# preguntar hasta que sea válido. 

# Paso 2: Inicialización de Estadísticas 

# El programa debe definir las variables iniciales (sin preguntar al usuario): 
#       • • Vida del Gladiador: 100 (int) 
#       • • Vida del Enemigo: 100 (int) 
#       • • Pociones de Vida: 3 (int) 
#       • • Daño base "Ataque Pesado": 15 (int) 
#       • • Daño base del enemigo: 12 (int) 
#       • • Turno Gladiador : True (booleano) 
# Paso 3: El Ciclo de Combate 
# El juego entra en un ciclo que se repite mientras ambos combatientes tengan más de 0 
# puntos de vida. 
# Turno del Jugador: 
# Muestra la vida actual de ambos y las pociones restantes. Luego, ofrece un menú con 3 
# opciones: 
#   1. Ataque Pesado 
#   2. Ráfaga Veloz (Requiere uso de for) 
#   3. Curar 
#           • Validación del Menú: El programa debe pedir la opción al usuario. 1. Verificar que lo 
# ingresado sea un número (.isdigit()). 
# 2. Verificar que el número sea 1, 2 o 3. 
#   o Si falla alguna validación, mostrar mensaje de error y volver a pedir. 

# Lógica de las Acciones: 
# Acción A: Ataque Pesado (Opción 1) 
#       • • Calcula el daño final. Si la vida del enemigo es menor a 20 puntos, el jugador 
# realiza un "Golpe Crítico" multiplicando su daño base por 1.5 (resultado float). 
#       • • Resta el daño a la vida del enemigo. 
#       • • Muestra un mensaje: "¡Atacaste al enemigo por X puntos de daño!" 
# Acción B: Ráfaga Veloz (Opción 2) 
#       • • Esta acción realiza una serie de golpes rápidos. Debes implementar un bucle for. 
#       • • El bucle debe repetirse 3 veces (usando range). 
#       • • Dentro del bucle, en cada repetición: 1. Resta 5 puntos de daño a la vida del enemigo. 
#       • 2. Muestra el mensaje: " > Golpe conectado por 5 de daño". 
# Acción C: Curar (Opción 3) 

# • Si tienes pociones (> 0): Suma 30 puntos a tu vida y resta 1 poción. 
#       • • Si NO tienes pociones: Muestra "¡No quedan pociones!" y pierdes el turno (el enemigo ataca igual). 
# Turno del Enemigo: 
# Justo después de tu acción, el enemigo ataca automáticamente. 
#       • • Resta el daño base del enemigo (12) a tu vida. 
#       • • Muestra un mensaje: "¡El enemigo te atacó por 12 puntos de daño!" 
# Paso 4: Fin del Juego 
# Cuando el ciclo termine (porque la vida de alguno llegó a 0 o menos), debes evaluar: 
#       • • Si vida_jugador > 0: Mostrar "¡VICTORIA! [Nombre] ha ganado la batalla." 
#       • • Si vida_jugador <= 0: Mostrar "DERROTA. Has caído en combate."

# 4. Ejemplo de Ejecución (Consola) 
# Plaintext 
# --- BIENVENIDO A LA ARENA ---
# Nombre del Gladiador: Leonidas1 
# Error: Solo se permiten letras. 
# Nombre del Gladiador: Leonidas 
# === INICIO DEL COMBATE === 
# Leonidas (HP: 100) vs Enemigo (HP: 100) | Pociones: 3 
# Elige acción: 
# 1. Ataque Pesado 
# 2. Ráfaga Veloz 
# 3. Curar 
# Opción: A 
# Error: Ingrese un número válido. 
# Opción: 2 
# >> ¡Inicias una ráfaga de golpes! 
# > Golpe conectado por 5 de daño 
# > Golpe conectado por 5 de daño 
# > Golpe conectado por 5 de daño 
# >> ¡El enemigo contraataca por 12 puntos! 
# === NUEVO TURNO === 
# Leonidas (HP: 88) vs Enemigo (HP: 85) | Pociones: 3 
# ... 


print("////////////////////////////////////////")
print ("Bienvenido a la Arena del Gladiador")
print("////////////////////////////////////////")


# NOMBRE 
nombre = input("Nombre del Gladiador: ")

while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

# VARIABLES 
vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_jugador = 15
danio_enemigo = 12
turno_jugador = True  # booleano

print("\n=== INICIO DEL COMBATE ===")

# COMBATE 
while vida_jugador > 0 and vida_enemigo > 0:


    print(nombre, "(HP:", vida_jugador, ") vs Enemigo (HP:", vida_enemigo, ") | Pociones:", pociones)

    # TURNO DEL JUGADOR 
    print("\nElige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    opcion = input("Opción: ")

    # VALIDACIÓN
    while not opcion.isdigit() or int(opcion) not in [1, 2, 3]:
        print("Error: Ingrese un número válido.")
        opcion = input("Opción: ")

    opcion = int(opcion)
    # ACCIONES 
    if opcion == 1:
        # ATAQUE PESADO
        danio = danio_jugador

        if vida_enemigo < 20:
            danio = danio * 1.5  # float
            print("¡Golpe crítico!")

        vida_enemigo -= int(danio)
        print("¡Atacaste al enemigo por", int(danio), "puntos de daño!")

    elif opcion == 2:
        # RÁFAGA VELOZ
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    elif opcion == 3:
        # CURAR
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print("¡Te curaste 30 puntos!")
        else:
            print("¡No quedan pociones!")

    # TURNO DEL ENEMIGO 
    if vida_enemigo > 0: 
        vida_jugador -= danio_enemigo
        print("¡El enemigo te atacó por 12 puntos de daño!")

# RESULTADO 
print("\n=== FIN DEL JUEGO ===")

if vida_jugador > 0:
    print("¡VICTORIA!", nombre, "ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")