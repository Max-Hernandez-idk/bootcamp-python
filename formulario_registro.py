# =========================================
# FORMULARIO DE REGISTRO
# =========================================

# -------- VALIDACIONES --------

def validar_nombre(nombre):
    if len(nombre) < 3:
        raise ValueError("❌ El nombre debe tener al menos 3 caracteres")
    return nombre


def validar_edad(edad):
    try:
        edad = int(edad)
    except ValueError:
        raise ValueError("❌ Debes escribir un número")

    if edad < 18:
        raise ValueError("❌ Debes tener al menos 18 años")
    if edad > 99:
        raise ValueError("❌ Edad no válida")

    return edad


def validar_email(email):
    if "@" not in email or "." not in email:
        raise ValueError("❌ Email inválido")
    return email


def validar_password(password):
    if len(password) < 6:
        raise ValueError("❌ La contraseña debe tener al menos 6 caracteres")
    return password


# -------- PROGRAMA PRINCIPAL --------

print("========================================")
print("       FORMULARIO DE REGISTRO")
print("========================================")

# Nombre
while True:
    nombre = input("Nombre (mínimo 3 caracteres): ")
    try:
        nombre = validar_nombre(nombre)
        print("✅ Nombre válido\n")
        break
    except ValueError as e:
        print(e)
        print()

# Edad
while True:
    edad = input("Edad (18-99): ")
    try:
        edad = validar_edad(edad)
        print("✅ Edad válida\n")
        break
    except ValueError as e:
        print(e)
        print()

# Email
while True:
    email = input("Email (debe contener @ y .): ")
    try:
        email = validar_email(email)
        print("✅ Email válido\n")
        break
    except ValueError as e:
        print(e)
        print()

# Contraseña
while True:
    password = input("Contraseña (mínimo 6 caracteres): ")
    try:
        password = validar_password(password)
        print("✅ Contraseña válida\n")
        break
    except ValueError as e:
        print(e)
        print()

# -------- RESULTADO --------

print("========================================")
print("REGISTRO EXITOSO 🎉")
print(f"Nombre : {nombre}")
print(f"Edad   : {edad}")
print(f"Email  : {email}")
print("========================================")