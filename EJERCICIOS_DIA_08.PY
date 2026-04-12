#Crea un diccionario con tu información personal (mínimo 6 claves) e imprímelo clave por clave con un loop

diccionario = {
    "nombre": "Max",
    "edad": 17,
    "ciudad": "Pachuca",
    "gmail": "maximilianohernandez@gmail.com",
    "telefono": 123456789,
    "ocupacion": "estudiante"
}

for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")

#Agrega 2 claves nuevas a ese diccionario y modifica 2 existentes

diccionario["hobby"] = "Programar"
diccionario["Musica"] = "Tyler the creator"
diccionario["edad"] = 22
diccionario["telefono"] = 7711217957
print(diccionario)

#Verifica si la clave "email" existe en tu diccionario — imprime un mensaje según el resultado

print("gmail" in diccionario)


#Crea una función mostrar_diccionario(dic) que imprima cada clave y valor formateado

def mostrar_diccionario(dic):
    for clave, valor in dic.items():
        print(f"{clave}: {valor}")


# Ejemplo de uso
mi_dic = {
    "API": "N/A",
    "DINERO": 1500,
    "Nombre": "Max"
}

mostrar_diccionario(mi_dic)


#Crea un diccionario de un producto con: nombre, precio, categoría, disponible. Imprime una ficha del producto
producto = {
    "nombre": "Laptop Gamer",
    "precio": 15000,
    "categoria": "Tecnología",
    "disponible": True
}

print("=================================")
print("        FICHA DEL PRODUCTO       ")
print("=================================")
print("Nombre:", producto["nombre"])
print("Precio: $", producto["precio"])
print("Categoría:", producto["categoria"])
print("Disponible:", producto["disponible"])
print("=================================")


#Usa .get() para acceder a una clave que no existe con un valor por defecto

celular = {
    "Marca": "Iphone",
    "Modelo": "17 Pro",
    "Uso": "Muy frecuente"
}

print(celular.get("precio", "$17,000"))

#Crea un diccionario donde las claves son números del 1 al 5 y los valores son sus cuadrados

numeros_cuad = {
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}

for clave, valor in numeros_cuad.items():
    print(f"{clave}: {valor}")


#Dado un diccionario de calificaciones {"matematicas": 9, "español": 8, "historia": 7}, imprime la materia con mayor calificación

dicc_calif = {
    "matematicas": 9,
    "español": 8,
    "historia": 7
}

mayor = max(dicc_calif, keys=dicc_calif.get)

print("La materia con mayor calificación es:", mayor)

# ================================
# SISTEMA COMPLETO - DÍA 8
# ================================

# ----------- DATOS INICIALES -----------

# Estudiantes
estudiantes = [
    {"nombre": "Max", "edad": 17, "promedio": 9},
    {"nombre": "Luis", "edad": 18, "promedio": 7},
    {"nombre": "Ana", "edad": 16, "promedio": 8.5}
]

# Productos
productos = [
    {"nombre": "Laptop", "precio": 15000},
    {"nombre": "Mouse", "precio": 300},
    {"nombre": "Teclado", "precio": 800}
]

# Agenda
agenda = []

# ----------- FUNCIONES -----------

def mostrar_estudiantes_destacados():
    print("\n🎓 Estudiantes con promedio mayor a 8:")
    for est in estudiantes:
        if est["promedio"] > 8:
            print(est["nombre"], "-", est["promedio"])


def buscar_producto(productos, nombre):
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            return producto
    return None


def duplicar_diccionario():
    dic = {"a": 1, "b": 2, "c": 3, "d": 4}
    nuevo = {}

    for clave, valor in dic.items():
        nuevo[clave] = valor * 2

    print("\n📦 Diccionario duplicado:", nuevo)


def actualizar_precio(productos, nombre, nuevo_precio):
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            producto["precio"] = nuevo_precio
            print("✅ Precio actualizado")
            return
    print("❌ Producto no encontrado")


def promedio_estudiante():
    estudiante = {
        "nombre": "Max",
        "materias": ["mate", "español", "historia"],
        "calificaciones": {
            "mate": 9,
            "español": 8,
            "historia": 7
        }
    }

    total = sum(estudiante["calificaciones"].values())
    cantidad = len(estudiante["calificaciones"])
    promedio = total / cantidad

    print(f"\n📊 Promedio de {estudiante['nombre']}: {promedio}")


# ----------- AGENDA -----------

def ver_contactos():
    if not agenda:
        print("📭 No hay contactos")
        return

    for contacto in agenda:
        print(f"\n👤 {contacto['nombre']}")
        print("Teléfono:", contacto["telefono"])
        print("Email:", contacto["email"])


def agregar_contacto():
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")

    agenda.append({
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    })

    print("✅ Contacto agregado")


def buscar_contacto():
    nombre = input("Buscar: ")

    for contacto in agenda:
        if contacto["nombre"].lower() == nombre.lower():
            print("\n👤 CONTACTO ENCONTRADO:")
            print("Nombre   :", contacto["nombre"])
            print("Teléfono :", contacto["telefono"])
            print("Email    :", contacto["email"])
            return

    print("❌ No encontrado")


def eliminar_contacto():
    nombre = input("Eliminar: ")

    for contacto in agenda:
        if contacto["nombre"].lower() == nombre.lower():
            agenda.remove(contacto)
            print("🗑️ Eliminado")
            return

    print("❌ No encontrado")


# ----------- MENÚ PRINCIPAL -----------

while True:
    print("\n========================================")
    print("         SISTEMA COMPLETO 🔥")
    print("========================================")
    print("1. Ver estudiantes destacados")
    print("2. Buscar producto")
    print("3. Duplicar diccionario")
    print("4. Actualizar precio")
    print("5. Ver promedio estudiante")
    print("6. Agenda de contactos")
    print("7. Salir")
    print("========================================")

    opcion = input("Opción: ")

    if opcion == "1":
        mostrar_estudiantes_destacados()

    elif opcion == "2":
        nombre = input("Producto a buscar: ")
        resultado = buscar_producto(productos, nombre)
        print(resultado if resultado else "❌ No encontrado")

    elif opcion == "3":
        duplicar_diccionario()

    elif opcion == "4":
        nombre = input("Producto: ")
        precio = float(input("Nuevo precio: "))
        actualizar_precio(productos, nombre, precio)

    elif opcion == "5":
        promedio_estudiante()

    elif opcion == "6":
        while True:
            print("\n====== AGENDA ======")
            print("1. Ver contactos")
            print("2. Buscar contacto")
            print("3. Agregar contacto")
            print("4. Eliminar contacto")
            print("5. Volver")

            op = input("Opción: ")

            if op == "1":
                ver_contactos()
            elif op == "2":
                buscar_contacto()
            elif op == "3":
                agregar_contacto()
            elif op == "4":
                eliminar_contacto()
            elif op == "5":
                break

    elif opcion == "7":
        print("👋 Saliendo...")
        break

    else:
        print("❌ Opción inválida")