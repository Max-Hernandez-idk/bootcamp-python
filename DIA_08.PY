# ============================================================
# DÍA 8 — Diccionarios
# Programador: Max
# ============================================================

# ── CREAR DICCIONARIO ────────────────────────────────────────
# Las llaves {} delimitan el diccionario.
# Cada par es "clave": valor separado por coma.

perfil = {
    "nombre": "Max",
    "edad": 17,
    "ciudad": "Pachuca",
    "lenguaje": "Python",
    "activo": True,
    "calificaciones": [9, 8, 10, 7, 9]
}

# ── ACCEDER A VALORES ────────────────────────────────────────
print(perfil["nombre"])
print(perfil["edad"])
print(perfil.get("email", "Sin email"))   # clave que no existe

# ── MODIFICAR ────────────────────────────────────────────────
perfil["email"] = "max@gmail.com"         # agregar
perfil["edad"] = 18                        # modificar
del perfil["activo"]                       # eliminar

# ── RECORRER ─────────────────────────────────────────────────
print("\n── Perfil completo ──")
for clave, valor in perfil.items():
    print(f"{clave:15}: {valor}")
# El :15 alinea las claves en 15 caracteres — detalle profesional

# ── LISTA DE DICCIONARIOS ────────────────────────────────────
productos = [
    {"nombre": "Laptop",  "precio": 15000, "stock": 5},
    {"nombre": "Mouse",   "precio": 350,   "stock": 20},
    {"nombre": "Teclado", "precio": 800,   "stock": 12},
    {"nombre": "Monitor", "precio": 5000,  "stock": 3}
]

print("\n── Inventario ──")
for producto in productos:
    print(f"{producto['nombre']:10} | ${producto['precio']:>6} | Stock: {producto['stock']}")

# ── BUSCAR EN LISTA DE DICCIONARIOS ──────────────────────────
buscar = "Mouse"
for producto in productos:
    if producto["nombre"] == buscar:
        print(f"\nEncontrado: {producto}")
        break