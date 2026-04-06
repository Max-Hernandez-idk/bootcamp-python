#Pide un número y di si es par o impar

numero = int(input("Escribe un numero: "))

if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")

#2. Pide la edad del usuario y di si es menor de edad, joven (18-25), adulto (26-60) o adulto mayor (60+)

edad = int(input("Escrbe tu edad: "))

if edad < 18:
    print("Eres menor de edad")
elif edad <= 25:
    print("Eres joven")
elif edad <= 60:
    print("Eres adulto")
else:
    print("Eres adulto mayor")

#3. Pide dos números y di cuál es mayor, o si son iguales

numerouno = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))

if numerouno > numero2:
    print(f"El numero {numerouno} es mayor")
elif numero2 > numerouno:
    print(f"El numero {numero2} es mayor")
else:
    print("Son iguales")

#4. Pide una calificación del 0 al 100 e imprime su letra: A(90-100), B(80-89), C(70-79), D(60-69), F(0-59)
print("Escribe tu calificacion 0-100")
calificacion = int(input("Escribe tu calificación: "))


if calificacion <= 59:
    print("F")
elif calificacion <= 69:
    print("D")
elif calificacion <=79:
    print("C")
elif calificacion <= 89:
    print("B")
else:
    print("A")


#5. Pide un número y di si es positivo, negativo o cero

numero_pn0 = int(input("Escribe un numero: "))

if numero_pn0 > 0:
    print("Es positivo")
elif numero_pn0 < 0:
    print("ES negativo")
else:
    print("Es cero")


#6. Pide el nombre de un color en español e imprime su significado (inventa al menos 4 colores)

print("Rojo, Naranja, Amarillo, Verde, Azul")
nombre_color = input("Escribe un color: ").lower()

if nombre_color == "rojo":
    print("Pasión, amor, energía, peligro, urgencia, fuerza y poder. Estimula las emociones y llama la atención.")
elif nombre_color == "naranja":
    print("Entusiasmo, creatividad, calidez, vitalidad y optimismo. Es un color sociable y amigable.")
elif nombre_color == "amarillo":
    print("Alegría, felicidad, luz, inteligencia y advertencia. Evoca positividad pero en exceso puede generar ansiedad.")
elif nombre_color == "verde":
    print("Naturaleza, equilibrio, salud, esperanza y prosperidad. Es relajante y simboliza crecimiento y armonía.")
elif nombre_color == "azul":
    print("Confianza, calma, lealtad, profesionalismo y seguridad. Es el color más universalmente apreciado.")
else:
    print("Color no reconocido. Elige entre: Rojo, Naranja, Amarillo, Verde o Azul.")


#7. Pide la temperatura actual y di si hace frío (menos de 15°), templado (15-25°) o calor (más de 25°)

temperatura_actual = int(input("Escribe la temperatura actual: "))

if temperatura_actual <= 15:
    print("Esta templado")
elif temperatura_actual <= 25:
    print(" Hace calor")
else:
    print("Hace demasiado calor")

#8. Pide un número y di si es divisible entre 3, entre 5, entre ambos, o entre ninguno

print("Numero del 0-100")

numero_div = int(input("Escribe un numero: "))

if numero_div % 3 == 0 and numero_div % 5 == 0:
    print("Es divisible entre ambos")
elif numero_div % 3 == 0:
    print("Es divisible entre 3")
elif numero_div % 5 == 0:
    print("Es divisible entre 5")
else:
    print("No es divisible con ninguno")


#9. Pide el saldo de una cuenta bancaria e imprime: "Saldo positivo", "Saldo en cero" o "Saldo negativo — en deuda"


saldo_cuenta_bancaria = float(input("Ingresa tu salgo en tu cuenta bancaria: "))


if saldo_cuenta_bancaria > 0:
    print("Saldo positivo")
elif saldo_cuenta_bancaria < 0:
    print("Saldo Negativo")
else:
    print("Salldo en ceros")



#Pide el nombre de un día de la semana e imprime si es día hábil o fin de semana

dia_semana = input("Escribe un dia de la semana: ").lower()

if dia_semana == "lunes":
    print("Es dia habil")
elif dia_semana == "martes":
    print("Es dia habil")
elif dia_semana == "miercoles":
    print("Es dia habil")
elif dia_semana == "jueves":
    print("Es dia habil")
elif dia_semana == "viernes":
    print("Es dia habil")
elif dia_semana == "sabado":
    print("Es fin de semana")
elif dia_semana == "domingo":
    print("Es fin de semana")
else:
    print("Ese dia no existe")



#Ejercicios intermedios:

#Pide el precio de un producto. Si cuesta más de 500 aplica 10% de descuento, si cuesta más de 1000 aplica 20%. Imprime el precio final

precio_producto = float(input("Precio de tu producto: "))
precio_final = precio_producto

if precio_producto > 1000:
    precio_final = precio_producto * 0.80
elif precio_producto > 500:
    precio_final = precio_producto * 0.90
else:
    precio_final = precio_producto

    print(f"Precio final: {precio_final}")


#Pide usuario y contraseña. Si el usuario es "admin" y la contraseña es "1234" imprime "Acceso concedido", si no "Acceso denegado"


usuario = input("¿Cuál es tu usuario?: ")
contraseña = input("Tu contraseña: ")
es_admin = True

if contraseña == "1234" and es_admin:
    print("Acceso permitido")
else:
    print("Acceso denegado")

#Pide 3 números e imprime cuál es el mayor de los tres

numero_1 = int(input("Escribe el primer numero: "))
numero_2 = int(input("Escribe el segundo numero: "))
numero_3 = int(input("Escribe el tercer numero: "))

if numero_1 == numero_2 == numero_3:
    print("Los tres numeros son iguales")
elif numero_1 >= numero_2 and numero_1 >= numero_3:
    print(f"El numero mayor es {numero_1}")
elif numero_2 >= numero_1 and numero_2 >= numero_3:
    print(f"El numero mayor es {numero_2}")
else:
    print(f"El numero mayor es {numero_3}")


#Pide el nombre de un mes e imprime cuántos días tiene

nombre_mes = input("Escribe el nombre de un mes: ").lower()

if nombre_mes == "enero":
    print(f"{nombre_mes} tiene 31 dias")
elif nombre_mes == "febrero":
    print(f"{nombre_mes} tiene 28 dias y 29 si es año bisiesto")
elif nombre_mes == "marzo":
    print(f"{nombre_mes} tiene 31 dias")
elif nombre_mes == "abril":
    print(f"{nombre_mes} tiene 30 dias")
elif nombre_mes == "Mayo":
    print(f"{nombre_mes} tiene 31 dias")
elif nombre_mes == "junio":
    print(f"{nombre_mes} tiene 30 dias")
elif nombre_mes == "julio":
    print(f"{nombre_mes} tiene 31 dias")
elif nombre_mes == "agosto":
    print(f"{nombre_mes} tiene 31 dias")
elif nombre_mes == "septiembre":
    print(f"{nombre_mes} tiene 30 dias")
elif nombre_mes == "octubre":
    print(f"{nombre_mes} tiene 31 dias")
elif nombre_mes == "noviembre":
    print(f"{nombre_mes} tiene 30 dias")
elif nombre_mes == "diciembre":
    print(f"{nombre_mes} tiene 31 dias")
else:
    print(f"{nombre_mes} ese mes no existe wey ")


#Pide la velocidad de un auto. Si va a más de 120 imprime "Exceso de velocidad", si va entre 60 y 120 "Velocidad normal", si va menos de 60 "Muy lento"


velocidad = int(input("Ingresa la velocidad de tu auto: "))


if velocidad >= 120:
    print("Vas a exceso de velocidad")
elif velocidad >= 60 and velocidad < 120:
    print("Velocidad normal")
elif velocidad < 60:
    print("Vas muy lento ")


        #🔥 RETO DEL DÍA 4
#Crea juego_adivinanza.py — un juego donde el usuario intenta adivinar un número:

print("========================================")
print("JUEGO DE ADIVINANZA")
print("========================================")

print("Tengo un numero entre 1 y 10")
pregunta = int(input("¿Cuál crees que es? "))
numero_pensado = 8

if pregunta == numero_pensado:
    print("Es el numero correcto 🎯")
elif pregunta < numero_pensado:
    print("Tu numero es menor al correcto 📉")
elif pregunta > numero_pensado:
    print("Tu numero es mayor al correcto 📈")
else:
    print("Fallaste")

print("========================================")

jugar_de_nuevo = input("¿Quieres jugar de nuevo? ")

if jugar_de_nuevo.lower() == "no":
    print("Hasta luego 👋")
    quit()
elif jugar_de_nuevo.lower() == "si":
    print("Sigamos 😎")