diccionario = {
    "dinero": 20,
    "poder": "Mucho",
    "PC GAMER": "No"
}

clave = input("Agrega una clave: ")
valor = input("Agrega un valor")
try:
    diccionario = (clave, valor)
    print(f"{clave}: {valor}")
except KeyError:
    print("⚠️ Error: La clave no existe")