numeros = 1
contador = 0
while numeros != 0:
    numeros = int(input("Escribe un número: "))
    if numeros != 0:
        contador +=1
        print(f"Cantidad de numeros: {contador}")