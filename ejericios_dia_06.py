#Crea una función saludar(nombre) que imprima un saludo personalizado

def saludar(nombre):
    print(f"Hola {nombre}, como estas, espero ye encuentres muy bien, mis mauores deseos!!")
saludar("Max")
saludar("Alicia")


#Crea una función mostrar_separador() que imprima una línea de = sin parámetros

def mostar_separador():
    print("========================================")
mostar_separador()


#Crea una función cuadrado(numero) que devuelva el número al cuadrado

def cuadrado(numero):
    return numero ** 2

numero = 8
resultado = cuadrado(numero)
print(f"El cuadrado del numero es: {resultado}")

#Crea una función es_par(numero) que devuelva True si es par y False si es impar

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print(es_par(8))   # True
print(es_par(12))  # True

#Crea una función mayor(a, b) que devuelva el número mayor de los dos
def mayor(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return a  # o b, son iguales3))
    
print(mayor(12, 5))   # 12
print(mayor(23, 50))  # 50

#Crea una función saludar_idioma(nombre, idioma="español") con valor por defecto

def saludar_idioma(nombre, idioma="Español"):
    if  idioma == "Español":
        print(f"Hola, {nombre}")
    elif idioma == "ingles":
        print(f"Hello, {nombre}")

saludar_idioma("Max")
saludar_idioma("Max", "Ingles")


#Crea una función celsius_a_fahrenheit(celsius) que convierta y devuelva la temperatura

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
resultado = celsius_a_fahrenheit(25)
print(resultado)


#Crea una función area_rectangulo(base, altura) que devuelva el área

def area_rectangulo(base, altura):
    return base * altura

area = area_rectangulo(11, 2)
print(f"El area es {area}")


#Crea una función contar_hasta(numero) que imprima del 1 hasta ese número
def contar_hasta(numero):
    contador = 1
    while contador <= numero:
        print(f"Contador: {contador}")
        contador += 1

contar_hasta(20)

#Crea una función es_mayor_de_edad(edad) que devuelva True o False

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True 
    else:
        return False
    
print(es_mayor_de_edad(22))  # True
print(es_mayor_de_edad(15))  # False


#Ejercicios intermedios:

#Crea una función calcular_promedio(a, b, c) que devuelva el promedio de 3 números

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

promedio = calcular_promedio(6, 7, 10)
print(f"Tu promedio de las 3 calificaciones juntas es: {promedio}")


#Crea una función numero_primo(numero) que devuelva True si es primo

def numero_primo(numero):
    if numero <= 1:
        return False
    
    i = 2
    while i < numero:
        if numero % i == 0:
            return False
        i += 1
    
    return True

print(numero_primo(7))   # True
print(numero_primo(10))  # False


#Crea una función factorial(numero) que devuelva el factorial
def factorial(numero):
    if numero == 0:
        return 1

    resultado = 1
    i = 1

    while i <= numero:
        resultado *= i
        i += 1

    return resultado


#Crea una función maximo_tres(a, b, c) que devuelva el mayor de 3 números

def maximo_tres(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
print(maximo_tres(12, 5, 30))
print(maximo_tres(100, 230, 10000))

#Crea una función describir_numero(numero) que devuelva un string diciendo si el número es par/impar, positivo/negativo y si es primo:

def describir_numero(numero):
    # Par o impar
    if numero % 2 == 0:
        tipo = "par"
    else:
        tipo = "impar"
    
    # Positivo o negativo
    if numero > 0:
        signo = "positivo"
    elif numero < 0:
        signo = "negativo"
    else:
        signo = "cero"
    
    # Primo
    if numero <= 1:
        primo = "no es primo"
    else:
        es_primo = True
        i = 2
        while i < numero:
            if numero % i == 0:
                es_primo = False
                break
            i += 1
        
        if es_primo:
            primo = "es primo"
        else:
            primo = "no es primo"
    
    return f"El número es {tipo}, {signo} y {primo}"

print(describir_numero(7))
print(describir_numero(-4))



#🔥 RETO DEL DÍA 6
#Crea calculadora_funciones.py — la calculadora del día 3, pero ahora con funciones:


