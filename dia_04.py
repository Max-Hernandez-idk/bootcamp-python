#===========================================================
# DÍA 4 — Condicionales if / elif / else
# Programador: Max
# ============================================================

# ── IF BÁSICO ────────────────────────────────────────────────
# Verificamos si un número es positivo.
# Si la condición es True, ejecuta el bloque indentado.


numero = int(input("Escribe un numero: "))

if numero > 0:
    print("El numero es positivo")


# ── IF / ELSE ────────────────────────────────────────────────
# Ahora manejamos dos casos: positivo o no positivo.

if numero > 0:
    print("El numero es positivo")
else:
    print("El numero NO es positivo")

# ── IF / ELIF / ELSE ─────────────────────────────────────────
# Manejamos tres casos: positivo, negativo o cero.

if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("El numero es 0")

# ── OPERADORES LÓGICOS ───────────────────────────────────────
# Verificamos múltiples condiciones al mismo tiempo.


edad = int(input("¿Cuántos años tienes? "))
dinero = float(input("¿Cuánto dinero tienes? "))


if edad >= 18 and dinero >= 100:
    print("Puedes entrar al evento VIP")
elif edad >= 18 and dinero < 100:
    print("Eres mayor de edad pero no tienes suficiente dinero")
elif edad < 18 and  dinero >= 100:
    print("Tienes dinero pero eres menor de edad")
else:
    print("No pudes entrar - menor de edad y sin dinero")

# ── CONDICIONAL CON STRING ───────────────────────────────────
# También podemos comparar texto, no solo números.

idioma = input("¿Qué idioma hablas? ").lower()
# .lower() convierte todo a minúsculas para comparar sin importar
# si el usuario escribió "Español", "ESPAÑOL" o "español"

if idioma == "español":
    print("Hola, bienvenido")
elif idioma == "english" or idioma == "ingles":
    print("Hello, welcome")
elif idioma == "français" or idioma == "frances":
    print("Bonjour, bienvenue")
else:
    print(f"Lo siento, no conozco el idioma: {idioma}")

    