# ============================================================
# DÍA 5 — Loops: while y for
# Programador: Max
# ============================================================

# ── WHILE BÁSICO ─────────────────────────────────────────────
# Cuenta del 1 al 5 usando while.
# La variable 'contador' cambia en cada iteración.
# Sin el contador += 1 el loop sería infinito.

print("── WHILE: contando del 1 al 5 ──")
contador = 1

while contador <= 5:
    print(f"Número: {contador}")
    contador += 1

# ── WHILE CON INPUT ──────────────────────────────────────────
# El loop continúa hasta que el usuario escriba 'salir'.
# Esto es un patrón muy común en programas reales.

print()
print("── WHILE CON INPUT ──")
respuesta = ""

while respuesta != "salir":
    respuesta = input("Escribe algo (o 'salir' para terminar): ").lower()
    if respuesta != "salir":
        print(f"Escribiste: {respuesta}")

print("Saliste del loop")

# ── FOR CON RANGE ─────────────────────────────────────────────
# range(1, 11) genera números del 1 al 10.
# La variable 'i' toma cada valor en orden.

print()
print("── FOR: números del 1 al 10 ──")
for i in range(1, 11):
    print(i)

# ── FOR CON PASO ─────────────────────────────────────────────
# range(0, 21, 2) genera pares del 0 al 20.

print()
print("── FOR: números pares del 0 al 20 ──")
for i in range(0, 21, 2):
    print(i)

# ── FOR AL REVÉS ─────────────────────────────────────────────
print()
print("── FOR: cuenta regresiva ──")
for i in range(10, 0, -1):
    print(i)
print("¡Despegue! 🚀")

# ── BREAK Y CONTINUE ─────────────────────────────────────────
print()
print("── BREAK: para cuando encuentre el 5 ──")
for i in range(1, 11):
    if i == 5:
        print("Encontré el 5, saliendo...")
        break
    print(i)

print()
print("── CONTINUE: salta los pares ──")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)