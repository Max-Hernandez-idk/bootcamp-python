# ============================================================
# DÍA 3 — input() y Operadores
# Programador: Max
# ============================================================

# ── INPUT BÁSICO ─────────────────────────────────────────────
# input() pausa el programa y espera que el usuario escriba.
# Lo que el usuario escribe queda guardado en la variable.
# SIEMPRE devuelve un string.

nombre = input("¿Cuál es tu nombre?")
print(f"Hola, {nombre}. Bienvenido al bootcamp")

# ── INPUT CON CONVERSIÓN ─────────────────────────────────────
# Convertimos a int porque vamos a hacer matemáticas con la edad.
# Si no convirtiéramos, Python lanzaría un TypeError.

edad = int(input("¿Cuantos años tienes?"))
año_actual = 2026
año_nacimiento = año_actual - edad
print(f"Naciste aproximadamente en {año_nacimiento}")

# ── OPERADORES ARITMÉTICOS ───────────────────────────────────
numero1 = float(input("Escribe el primer numero: "))
numero2 = float(input("Escribe el segundo numero: "))

suma        = numero1 + numero2
resta       = numero1 - numero2
multiplicacion = numero1 * numero2
division    = numero1 / numero2
potencia    = numero1 ** numero2
modulo      = numero1 % numero2

print()
print(f"Suma:           {numero1} + {numero2} = {suma}")
print(f"Resta:          {numero1} - {numero2} = {resta}")
print(f"Multiplicación: {numero1} * {numero2} = {multiplicacion}")
print(f"División:       {numero1} / {numero2} = {division}")
print(f"Potencia:       {numero1} ** {numero2} = {potencia}")
print(f"Módulo:         {numero1} % {numero2} = {modulo}")

# ── OPERADORES DE COMPARACIÓN ────────────────────────────────
# Estos operadores comparan dos valores y devuelven True o False.

print()
print(f"¿{numero1} es mayor que {numero2}?        {numero1 > numero2}")
print(f"¿{numero1} es menor que {numero2}?        {numero1 < numero2}")
print(f"¿{numero1} es igual a {numero2}?          {numero1 == numero2}")
print(f"¿{numero1} es diferente de {numero2}?     {numero1 != numero2}")