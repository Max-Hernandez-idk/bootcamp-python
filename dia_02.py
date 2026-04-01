# ============================================================
# DÍA 2 — Variables y Tipos de Datos
# Programador: Max
# ============================================================

# ── STRING (texto) ──────────────────────────────────────────
# Un string es cualquier texto entre comillas.
# Python lo identifica como tipo 'str'.

nombre = "Max"
ciudad = "Pachuca"
lenguaje = "Python"


# ── INTEGER (número entero) ─────────────────────────────────
# Un integer es un número sin decimales.
# Python lo identifica como tipo 'int'.


edad = 17
año_inicio = 2026
horas_practica = 2

# ── FLOAT (número decimal) ──────────────────────────────────
# Un float es un número con punto decimal.
# Python lo identifica como tipo 'float'.

promedio = 9.5
temperatura = 23.8
version_python = 3.14


# ── BOOLEAN (verdadero o falso) ─────────────────────────────
# Un boolean solo puede ser True o False.
# Se usa para representar estados: ¿está activo? ¿es válido?

es_estudiante = True
tiene_experiencia = False
bootcamp_completado = False


# ── IMPRIMIR LAS VARIABLES ──────────────────────────────────
# Ahora usamos print() para mostrar el valor de cada variable.
# Nota: no ponemos comillas alrededor del nombre de la variable.
# Si pusieras comillas, imprimiría la palabra, no el valor.


print(nombre)           # imprime: Max
print(edad)             # imprime: 17
print(promedio)         # imprime: 9.5
print(es_estudiante)    # imprime: True

# ── VER EL TIPO DE UNA VARIABLE ─────────────────────────────
# type() es una función que te dice qué tipo de dato es.
# Muy útil para debuggear cuando no sabes qué contiene algo.

print(type(nombre))
print(type(edad))           # <class 'int'>
print(type(promedio))       # <class 'float'>
print(type(es_estudiante))  # <class 'bool'>

#PARTE 4 — Print con variables (f-strings)

# Sin f-string — incómodo
print("Hola, me llamo " + nombre + " y tengo " + str(edad) + " años")

# Con f-string — así trabajan los profesionales
print(f"Hola, me llamo {nombre} y tengo {edad} años")

# ── F-STRINGS ───────────────────────────────────────────────
# La f antes de las comillas activa el modo f-string.
# Las llaves {} son donde metes las variables.

print(f"Mi nombre es {nombre}")
print(f"Tengo {edad} años y vivo en {ciudad}")
print(f"Estudio {lenguaje} y llevo {horas_practica} horas de práctica")
print(f"¿Soy estudiante? {es_estudiante}")
print(f"Mi promedio es {promedio}")

#🔑 Convención profesional — snake_case:

# Así nombran variables los profesionales en Python
nombre_completo = "Max Hernandez"
año_de_nacimiento = 2009
es_mayor_de_edad = False
horas_de_practica_diaria = 2