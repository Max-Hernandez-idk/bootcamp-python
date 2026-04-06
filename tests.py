print("========================================")
print        ("JUEGO DE ADIVINANZA")
print("========================================")
print("Tengo unn numero entre 1 y 10")
pregunta = int(input("¿Cuál crees que es?"))
numero_pensado = 8

if pregunta in range(1,6):
    print("fallaste")
elif pregunta == 7:
    print("Tu numero es mayor al correcto")
elif pregunta in range(9,10):
    print("Tu numero es menor al correcto")
elif pregunta == numero_pensado:
    print("Es el numero correcto")
print("========================================")
jugar_de_nuevo = input("¿Quieres jugar de nuevo?")
if jugar_de_nuevo == "No":
    quit
    print("Hasta luego")
elif jugar_de_nuevo == "Si":
    print("Sigamos")