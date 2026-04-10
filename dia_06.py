# ============================================================
# DÍA 6 — Funciones
# Programador: Max
# ============================================================

# ── FUNCIÓN BÁSICA ───────────────────────────────────────────
# def crea la función. Solo se ejecuta cuando la llamas.


def mostar_bienvenida():
    print("========================================")
    print("     BOOTCAMP PROFESIONAL DE PYTHON     ")
    print("========================================")

mostar_bienvenida() # llamada a la función


# ── FUNCIÓN CON PARÁMETROS ───────────────────────────────────
# Los parámetros son variables locales — solo existen dentro
# de la función.


def saludar(nombre, edad):
    print(f"Hola {nombre}m tienes {edad} años")

    saludar("Max", 17)
    saludar("Ana", 25)


# ── FUNCIÓN CON PARÁMETROS ───────────────────────────────────
# Los parámetros son variables locales — solo existen dentro
# de la función.

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b

# Usando las funciones
print(sumar(10, 5))           # 15
print(restar(10, 5))          # 5
print(multiplicar(10, 5))     # 50
print(dividir(10, 5))         # 2.0
print(dividir(10, 0))         # Error: no se puede dividir entre cero



# ── FUNCIÓN CON DEFAULT ──────────────────────────────────────
# Si no pasas el argumento, usa el valor por defecto.

def potencia(base, exponente=2):
    return base ** exponente

print(potencia(3))      # 9   — usa exponente=2 por defecto
print(potencia(3, 3))   # 27  — usa exponente=3

# ── FUNCIONES QUE LLAMAN A OTRAS FUNCIONES ───────────────────
# Las funciones pueden usar otras funciones adentro.
# Esto se llama composición de funciones.

def calcular_promedio(a, b, c):
    total = sumar(sumar(a, b), c)   # usa la función sumar
    return total / 3

print(calcular_promedio(7, 8, 9))   # 8.0