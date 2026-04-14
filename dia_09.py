# ============================================================
# DÍA 9 — Manejo de Errores y Excepciones
# Programador: Max
# ============================================================

# ── TRY / EXCEPT BÁSICO ──────────────────────────────────────
print("── Ejemplo 1: ValueError ──")
try:
    numero = int(input("Escribe un número: "))
    print(f"Tu número es: {numero}")
except ValueError:
    print("❌ Eso no es un número entero")

# ── MÚLTIPLES EXCEPT ─────────────────────────────────────────
print("\n── Ejemplo 2: Múltiples errores ──")
try:
    numero = int(input("Escribe un número: "))
    resultado = 100 / numero
    print(f"100 / {numero} = {resultado}")
except ValueError:
    print("❌ Debes escribir un número")
except ZeroDivisionError:
    print("❌ No puedes dividir entre cero")

# ── ELSE Y FINALLY ───────────────────────────────────────────
print("\n── Ejemplo 3: else y finally ──")
try:
    edad = int(input("Escribe tu edad: "))
except ValueError:
    print("❌ Edad inválida")
else:
    print(f"✅ Edad válida: {edad}")
finally:
    print("── Proceso terminado ──")

# ── INDEXERROR ───────────────────────────────────────────────
print("\n── Ejemplo 4: IndexError ──")
lista = [1, 2, 3]
try:
    indice = int(input("¿Qué índice quieres ver? "))
    print(f"El elemento es: {lista[indice]}")
except IndexError:
    print(f"❌ Índice fuera de rango. La lista tiene {len(lista)} elementos")
except ValueError:
    print("❌ Debes escribir un número")

# ── KEYERROR ─────────────────────────────────────────────────
print("\n── Ejemplo 5: KeyError ──")
usuario = {"nombre": "Max", "edad": 17}
try:
    clave = input("¿Qué dato quieres ver? ")
    print(f"{clave}: {usuario[clave]}")
except KeyError:
    print(f"❌ La clave '{clave}' no existe")

# ── VALIDACIÓN CON LOOP ──────────────────────────────────────
print("\n── Ejemplo 6: Validación robusta ──")
while True:
    try:
        nota = float(input("Ingresa una nota (0-10): "))
        if nota < 0 or nota > 10:
            print("❌ La nota debe estar entre 0 y 10")
            continue
        break
    except ValueError:
        print("❌ Debes escribir un número")

print(f"✅ Nota registrada: {nota}")

# ── RAISE ────────────────────────────────────────────────────
print("\n── Ejemplo 7: Raise ──")
def calcular_promedio(calificaciones):
    if len(calificaciones) == 0:
        raise ValueError("La lista no puede estar vacía")
    return sum(calificaciones) / len(calificaciones)

try:
    print(calcular_promedio([8, 9, 7]))    # funciona
    print(calcular_promedio([]))            # lanza error
except ValueError as e:
    print(f"❌ {e}")