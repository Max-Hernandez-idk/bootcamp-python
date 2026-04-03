#1. Pide el nombre del usuario e imprímelo con un saludo personalizado
nomre_usuario = input("¿Cual es tu usuario? ")
print(f"Hola, {nomre_usuario}, espero que tengas un dia feliz y lleno de alregria")

# Pide dos números enteros e imprime su suma
print(f"Hola, {nomre_usuario}, de favor a continuación escribe dos numeros enteros. Muchas gracias")
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))

suma = numero1 + numero2

print(f"Usuario: {nomre_usuario}, la suma de {numero1} y {numero2} es: {suma}")

#3. Pide el nombre y la edad del usuario e imprime cuántos años le faltan para los 100

nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuál es tu edad? "))
años_proporcionaos = 100
años_que_faltan = años_proporcionaos - edad
print(f"Hola, {nombre}, actualmente tu edad es de {edad}, te faltan {años_que_faltan} años para llegar a los 100 años de edad")

#4. Pide un número e imprime su cuadrado (número ** 2)
numero = float(input("Escribe un numero y te lo daré al cuadrado: "))

operación = numero ** 2
print(f"Tu numero {numero} al cuadrado es: {operación}")


#5. Pide un número e imprime si es par o no — un número es par cuando `numero % 2 == 0`

numero_x = int(input("Escribe un numero: "))

es_par = numero_x % 2 == 0
impar = numero_x % 2 != 0

print(f"¿Es par? {es_par}")
print(f"¿Es impar? {impar}")

#6. Pide el precio de un producto e imprime cuánto costaría comprar 3

producto = input("¿Cuál es tu producto? ")

precio_producto = float(input(f"¿Cuál es el precio del o de la {producto}? "))

cuanto_cuesta_comprar_3 = precio_producto * 3

print(f"El precio de o de la {producto} por 3 es de: {cuanto_cuesta_comprar_3}")

#7. Pide la base y la altura de un rectángulo e imprime su área (base * altura)

base_rec = float(input("Escribe la base: "))
altura_rec = float(input("Escribe la altura"))

area = base_rec * altura_rec

print(f"El área del rectangulo es de: {area}")

#8. Pide un número e imprime su doble, su triple y su mitad

numero_3 = float(input("Escribe un numero: "))

doble = numero_3 *2
triple = numero_3 *3
mitad = numero_3 / 2

print(f"El doble de tu numero es: {doble}")
print(f"El triple de tu numero es: {triple}")
print(f"La mitad de tu numero es: {mitad}")

#9. Pide dos números e imprime cuál operación da mayor resultado: suma o multiplicación

numero_uno = float(input("Escribe el primer numero: "))
numero_dos = float(input("Escribe el segundo numero: "))

multi = numero_uno * numero_dos
suma = numero_uno + numero_dos

print(f"Suma: {suma}")
print(f"Multiplicación: {multi}")
print(f"¿La suma es mayor? {suma > multi}")

#10. Pide el nombre del usuario y cuántos días lleva programando, imprime un mensaje motivacional

Usuario_pro = input("Escribe tu usuario: ")
dias_programando = input("¿Cuántos dias llevas programando?  ")

print(f"Felicicdades, {Usuario_pro}, llevas {dias_programando} estoy muy orgulloso de ti, sigue asi no te rindas ")

#**Ejercicios intermedios:**

#11. Pide el radio de un círculo e imprime su área. Área = 3.14159 * radio ** 2

radio_cir = float(input("Escribe el radio del circulo: "))
pi = 3.14159

area_cir = pi * (radio_cir ** 2)

print(f"El area del circulo es de: {area_cir}")

#12. Pide una temperatura en Celsius e imprímela en Fahrenheit. Fórmula: `(celsius * 9/5) + 32`


temp_c = float(input("Escribe una temperatura en celcius: "     ))


formula = (temp_c* 9/5) + 32

print(f"Tu temperatura celcius en fahrenheit es de: {formula}")


#Pide el precio de algo y un porcentaje de descuento, imprime el precio final

precio = float(input("Ingresa el precio del producto: "))
porcentaje_descuento = int(input("Ingresa su porcentaje de descuento: "))

descuento = precio * (porcentaje_descuento / 100)
total = precio - descuento

print(f"Tu precio con descuento en total es de: {descuento}")

#14. Pide 3 calificaciones e imprime el promedio

calif1 = float(input("Ingresa la primera calificación: "))
calif2 = float(input("Ingresa la segunda calificación: "))
calif3 = float(input("Ingresa la tercera calificación: "))

promedio = (calif1 + calif2 + calif3) / 3

print(f"Tu promedio de las 3 calificaciones es: {promedio}")

#15. Pide cuántas horas estudias al día e imprime cuántas horas estudiarás en 30 días, 6 meses y 1 año

horas_estudio = int(input("Cuantas horas estudias al día: "))


horas_est_30_dias = horas_estudio * 30
horas_est_6_meses = horas_estudio * 182
horas_est_1_año = horas_estudio * 365


print(f"En 30 dias estarias estudiando: {horas_est_30_dias}horas, en 6 meses: {horas_est_6_meses} horas, y en un año: {horas_est_1_año} horas.")


# 🔥 RETO DEL DÍA 3

print("========================================")
print("        CALCULADORA PROFESIONAL         ")
print("========================================")
numero1_calc = int(input("Escribe el primer numero: "))
numero2_calc = int(input("Escribe el segundo numero: "))
print("========================================")
suma_calc = numero1_calc + numero2_calc
resta_calc = numero1_calc - numero2_calc
multi_calc = numero1_calc * numero2_calc
divi_calc = numero1_calc / numero2_calc
divi_entera_calc = numero1_calc // numero2_calc
modulo_calc = numero1_calc % numero2_calc
potencia_calc = numero1_calc ** numero2_calc
print("========================================")
print(f"¿Son iguales? {numero1_calc == numero2_calc}")
print(f"¿El primero es mayor? {numero1_calc > numero2_calc}")
print(f"La suma es: {suma_calc}")
print(f"La resta es: {resta_calc}")
print(f"La multiplicación es: {multi_calc}")
print(f"La división es: {divi_calc}")
print(f"La división entera es: {divi_entera_calc}")
print(f"El módulo es: {modulo_calc}")
print(f"La potencia es: {potencia_calc}")