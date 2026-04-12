#Ejercicios básicos:

#Crea una lista con 5 de tus canciones favoritas e imprímelas numeradas
canciones_fav = ["ATM", "Hell of a life", "Let You Down", "I Really Want To Stay At Your House", "Chippin in"]
print(canciones_fav[0])
print(canciones_fav[1])
print(canciones_fav[2])
print(canciones_fav[3])
print(canciones_fav[4])
#Agrega 2 canciones más a esa lista con append e imprímela de nuevo
canciones_fav.append("Never Fade Away")
print(canciones_fav[5])
#Elimina la primera canción de la lista e imprime cuántas quedan
canciones_fav.remove("ATM")
print(canciones_fav)
#Crea una lista de números del 1 al 10 manualmente e imprime el mayor, el menor y la suma
lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max(lista_num))
print(min(lista_num))
print(sum(lista_num))
#Crea una función mostrar_lista(lista) que imprima cada elemento numerado
def mostrar_lista(lista):
    for i, elemento in enumerate(lista):
        print(f"{i + 1}. {elemento}")
#Crea una lista vacía, pide 5 números al usuario con un loop y agrégalos a la lista con append
lista_vacia = []

for i in range(5):
    numero = int(input(f"Ingresa el número {i+1}: "))
    lista_vacia.append(numero)

print("Lista final:", lista_vacia)
#Dada la lista [3, 1, 4, 1, 5, 9, 2, 6], imprímela ordenada sin modificar la original
lista = [3, 1, 4, 1, 5, 9, 2, 6]
print(sorted(lista))
#Verifica si un número que pida el usuario está en la lista del ejercicio anterior
lista = []

for i in range(9):
    usuario = int(input("Ingresa un número: "))
    
    if usuario in lista:
        print("Ese número ya está en la lista anterior")
    else:
        lista.append(usuario)

print("Lista final:", lista)
#Imprime solo los primeros 3 elementos de una lista usando slicing
lista_compras = ["pan", "leche", "huevos", "manzanas", "arroz"]

primeros_tres = lista_compras[:3]

print("Lista completa:", lista_compras)
print("Primeros 3 elementos:", primeros_tres)

#Crea una lista con los nombres de los días de la semana y #recórrela con enumerate
nombres_sem = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

for i, nombres_sem in enumerate(nombres_sem):
    print(f"i: {nombres_sem}")

#Ejercicios intermedios:

#Crea una función promedio_lista(lista) que reciba una lista de números y devuelva su promedio
def promedio_lista(lista):
    lista = [8, 9, 10, 11, 12, 11, 2222]
    
#Crea una función contar_pares(lista) que devuelva cuántos números pares hay en una lista
def contar_pares(lista):
    contador = 0
    for num in lista:
        if num % 2 == 0:
            contador += 1
    return contador

#Crea una función invertir_lista(lista) que devuelva la lista al revés sin usar [::-1]
def invertir_lista(lista):
    nueva_lista = []
    for i in range(len(lista) - 1, -1, -1):
        nueva_lista.append(lista[i])
    return nueva_lista
#Pide al usuario 5 calificaciones con un loop, guárdalas en una lista y muestra: promedio, mayor, menor y si aprobó (promedio >= 6)
calificaciones = []

for i in range(5):
    nota = float(input(f"Ingresa la calificación {i+1}: "))
    calificaciones.append(nota)

promedio = sum(calificaciones) / len(calificaciones)
mayor = max(calificaciones)
menor = min(calificaciones)

print("Promedio:", promedio)
print("Mayor:", mayor)
print("Menor:", menor)

if promedio >= 6:
    print("Aprobó ✅")
else:
    print("Reprobó ❌")

#Crea una función lista_sin_duplicados(lista) que reciba una lista y devuelva una nueva sin elementos repetidos:
def lista_sin_duplicados(lista):
    nueva = []
    for elemento in lista:
        if elemento not in nueva:
            nueva.append(elemento)
    return nueva

# prueba
print(lista_sin_duplicados([1, 2, 2, 3, 3, 3, 4]))

#pythonlista_sin_duplicados([1, 2, 2, 3, 3, 3, 4])
# devuelve: [1, 2, 3, 4]


