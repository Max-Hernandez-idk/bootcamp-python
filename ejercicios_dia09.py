#Pide un número al usuario con validación — si escribe texto muestra error y vuelve a pedir
try:
    numero = int(input("Escribe un numero o numeros: "))
    print(f"Tu numeor o numeros es: {numero}")
except ValueError:
    print("❌ Error: debes de escribir un número")

#Pide dos números y divídelos — maneja ValueError y ZeroDivisionError por separado

try: 
    numero_uno = int(input("Escribe el primer numero: "))
    numero_dos = int(input("Escribe el segundo numero: "))

    resultado = numero_uno / numero_dos
    print(f"La division de tus dos numeros es de: {resultado}")
except ValueError:
    print("❌ Error: Escribe numeros y no texto.")
except ZeroDivisionError:
    print("❌ Error: No se puede dividir entre 0 ")

#Crea una lista de 3 elementos y pide un índice al usuario — maneja IndexErro
lista = ["PC GAMER", "API KEYS", "PIZZA"]

try:
    indice = int(input("Escribe un índice (0, 1, 2): "))
    print(lista[indice])    # aquí puede explotar con IndexError
except ValueError:
    print("❌ Debes escribir un número")
except IndexError:
    print(f"❌ Ese índice no existe, la lista solo tiene {len(lista)} elementos")

#Crea un diccionario y pide una clave al usuario — maneja KeyError

diccionario = {
    "dinero": 20,
    "poder": "Mucho",
    "pc gamer": "No"
}

clave = input("Ingresa una clave: ")

try:
    print(f"{clave}: {diccionario[clave]}")
except KeyError:
    print("⚠️ Error: La clave no existe")

#Pide una edad entre 0 y 120 con validación completa — loop hasta que sea válida

while True: 
    try:
        edad = int(input("Ingresa tu edad 0-120: "))
        if edad >= 0 or edad <= 120:
            print("Tu edad debe estar entre 0 y 120 , porfavor vuelve a intentarlo, gracias xdxd")
            continue
        break
    except ValueError:
        print("Debes escribir un numero")

def convertir_entero(texto):
    try:
        return int(texto)
    except ValueError:
        return None
print(convertir_entero("123"))   # 123
print(convertir_entero("hola"))  # None

#Pide un número positivo — rechaza negativos con un mensaje, sigue pidiendo hasta obtener uno válido

while True:
    try:
        numero_pos = int(input("Escribe un número positivo: "))

        if numero_pos < 0:
            print("❌ El número es negativo, intenta de nuevo")
            continue

        print(f"✅ Tu número {numero_pos} es positivo")
        break

    except ValueError:
        print("⚠️ Eso no es un número válido")

        print("¡¡El programa esta funcionando con exito!!")


#Usa finally para imprimir "── Proceso completado ──" siempre, haya error o no

try:
    numero = int(input("Escribe un numero: "))
except ValueError:
    print("Ese no es un numero")
else:
    print(f"Numero valido: {numero}")
finally:
    print("── Proceso completado ──")

#dividir_seguro(a, b)
def dividir_seguro(a, b):
    try:
        return a / b
    except Exception:
        return None
    
# =========================================
# EJERCICIO 1
# Función dividir_seguro(a, b)
# =========================================
def dividir_seguro(a, b):
    try:
        return a / b
    except Exception:
        return None


# =========================================
# EJERCICIO 2
# Pedir 5 números válidos
# =========================================
numeros = []

while len(numeros) < 5:
    try:
        num = float(input("Ingresa un número: "))
        numeros.append(num)
    except ValueError:
        print("Entrada inválida")

print("Números:", numeros)


# =========================================
# EJERCICIO 3
# Función validar_email(email)
# =========================================
def validar_email(email):
    if "@" not in email or "." not in email:
        raise ValueError("Email inválido")
    return True


# =========================================
# EJERCICIO 4
# Función obtener_elemento(lista, indice)
# =========================================
def obtener_elemento(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        return "Índice fuera de rango"
    except TypeError:
        return "Índice inválido"


# =========================================
# EJERCICIO 5
# Programa hasta que el usuario escriba "fin"
# =========================================
numeros = []

while True:
    entrada = input("Número o 'fin': ")

    if entrada.lower() == "fin":
        break

    try:
        num = float(entrada)
        numeros.append(num)
    except ValueError:
        print("Entrada inválida")

if numeros:
    print("Suma:", sum(numeros))
    print("Promedio:", sum(numeros) / len(numeros))
    print("Mayor:", max(numeros))
    print("Menor:", min(numeros))
else:
    print("No hay números válidos")


# =========================================
# EJERCICIO 6
# Función buscar_clave(diccionario, clave)
# =========================================
def buscar_clave(diccionario, clave):
    return diccionario.get(clave, "No encontrado")


# =========================================
# EJERCICIO 7
# Calculadora con manejo de errores
# =========================================
while True:
    try:
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))
    except ValueError:
        print("Debes ingresar números válidos")
        continue

    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        print(a + b)
    elif opcion == "2":
        print(a - b)
    elif opcion == "3":
        print(a * b)
    elif opcion == "4":
        if b == 0:
            print("No se puede dividir entre cero")
        else:
            print(a / b)
    elif opcion == "5":
        break
    else:
        print("Opción inválida")
