# ============================================================
# DÍA 7 — Listas
# Programador: Max
# ============================================================

# ── CREAR LISTAS ─────────────────────────────────────────────
estudiantes = ["Max", "Ana", "Luis", "María", "Carlos"]
calificaciones = [85, 92, 78, 95, 88]
mixta = ["Python", 3.14, True, 17]

# ── ACCEDER A ELEMENTOS ──────────────────────────────────────
print(f"Primer estudiante: {estudiantes[0]}")
print(f"Último estudiante: {estudiantes[-1]}")
print(f"Tercer estudiante: {estudiantes[2]}")

# ── MODIFICAR ────────────────────────────────────────────────
estudiantes.append("Pedro")           # agrega al final
estudiantes.insert(0, "Sofía")        # inserta al inicio
estudiantes.remove("Luis")            # elimina por valor
print(f"Lista modificada: {estudiantes}")

# ── INFORMACIÓN ──────────────────────────────────────────────
print(f"Total estudiantes: {len(estudiantes)}")
print(f"Mejor calificación: {max(calificaciones)}")
print(f"Peor calificación: {min(calificaciones)}")
print(f"Promedio: {sum(calificaciones) / len(calificaciones)}")

# ── RECORRER CON FOR ─────────────────────────────────────────
print("\n── Lista de estudiantes ──")
for i, estudiante in enumerate(estudiantes):
    print(f"{i + 1}. {estudiante}")

# ── BUSCAR EN LISTA ──────────────────────────────────────────
buscar = "Max"
if buscar in estudiantes:
    print(f"{buscar} está en la lista")
else:
    print(f"{buscar} NO está en la lista")

# ── SLICING ──────────────────────────────────────────────────
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Primeros 3: {numeros[:3]}")
print(f"Últimos 3: {numeros[-3:]}")
print(f"Al revés: {numeros[::-1]}")