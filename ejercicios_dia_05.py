#Imprime los números del 1 al 20 usando while

contador = 1
while contador < 21:
    print(f"Numero: {contador}")
    contador += 1

#Pide números al usuario hasta que escriba 0, luego imprime cuántos números escribió

numeros = 1
contador = 0
while numeros != 0:
    numeros = int(input("Escribe un número: "))
    if numeros != 0:
        contador +=1
        print(f"Cantidad de numeros: {contador}")

#Pide una contraseña al usuario. Si no escribe "python123" sigue pidiéndola. Cuando la acierte imprime "Acceso concedido"
contraseña = ""

while contraseña != "python123":
    contraseña = input("Ingresa la contraseña requerida: ")
    if contraseña != "python123":
        print("Ingresa la contraseña correcta")

print("Acceso concedido 🔓")

#Cuenta regresiva desde 10 hasta 1 usando while, al final imprime "¡Tiempo!"

conteo_reg = 10

while conteo_reg >= 1:
    print(f"Conteo regresivo: {conteo_reg}")
    conteo_reg -= 1

print("¡Tiempo! ⏰")


#Pide números al usuario y súmalos. Cuando escriba 0 para y muestra el total


numero = 1
total = 0

while numero != 0:
    numero = int(input(...))
    if numero != 0:
        total += numero

#Ejercicios con for
#Imprime la tabla de multiplicar del número que pida el usuario

print("TABLAS DE MULTIPLICAR")
print("Si buscas alguna tabla escribe: Tabla del 1... etc")

tablas = int(input("Que tabla buscas: "))

for i in range(1, 11):
    resultado = tablas * i
    print(f"{tablas} x {i} = {resultado}")

    #1️⃣ Impares del 1 al 50
for i in range(1, 51):
    if i % 2 != 0:
        print(i)
#2️⃣ Múltiplos de 7 del 1 al 100
for i in range(1, 101):
    if i % 7 == 0:
        print(i)
#3️⃣ Letras de tu nombre
nombre = input("Escribe tu nombre: ")

for letra in nombre:
    print(letra)
#4️⃣ Suma del 1 al 100
total = 0

for i in range(1, 101):
    total += i

print("Resultado:", total)
#🟡 INTERMEDIOS
#5️⃣ Factorial
numero = int(input("Ingresa un número: "))
factorial = 1

for i in range(1, numero + 1):
    factorial *= i

print("Factorial:", factorial)
#6️⃣ Número primo
numero = int(input("Ingresa un número: "))
es_primo = True

if numero <= 1:
    es_primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False

if es_primo:
    print("Es primo")
else:
    print("No es primo")
#7️⃣ Triángulo de asteriscos
for i in range(1, 6):
    print("*" * i)
#8️⃣ Promedio de 5 calificaciones
total = 0

for i in range(5):
    cal = float(input(f"Calificación {i+1}: "))
    total += cal

promedio = total / 5
print("Promedio:", promedio)
#9️⃣ Cuenta regresiva personalizada
numero = int(input("Desde qué número quieres contar: "))

for i in range(numero, 0, -1):
    print(i)

print("¡Tiempo!")
#🔥💀 RETO FINAL (JUEGO PRO)
import random

while True:
    print("========================================")
    print("     JUEGO DE ADIVINANZA v2.0")
    print("========================================")

    numero_secreto = random.randint(1, 10)
    intentos_max = int(input("¿Cuántos intentos quieres tener? "))

    for intento in range(1, intentos_max + 1):
        print("========================================")
        pregunta = int(input(f"Intento {intento} de {intentos_max} — ¿Cuál es el número? "))

        if pregunta == numero_secreto:
            print(f"🎯 ¡Correcto! Adivinaste en {intento} intentos")
            break
        elif pregunta < numero_secreto:
            print("📉 Mi número es mayor, sigue intentando")
        else:
            print("📈 Mi número es menor, sigue intentando")
    else:
        print(f"💀 Se acabaron los intentos. El número era {numero_secreto}")

    print("========================================")
    jugar = input("¿Jugar de nuevo? (si/no): ").lower()

    if jugar == "no":
        print("¡Hasta luego! 👋")
        break