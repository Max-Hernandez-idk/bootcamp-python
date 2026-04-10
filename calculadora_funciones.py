while True:
    print("========================================")
    print("       CALCULADORA PROFESIONAL v2       ")
    print("========================================")

    a = float(input("Número 1: "))
    b = float(input("Número 2: "))

    print("=======================================")

    def mostrar_menu():
        print("Elige la operacion: ")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")
        print("6. División entera")
        print("7. Módulo")

    mostrar_menu()
    opcion = input("Opción: ")

    print("=======================================")

    def sumar(a, b):
        return a + b

    def restar(a, b):
        return a - b

    def multiplicar(a, b):
        return a * b

    def dividir(a, b):
        return a / b

    def potenciar(a, b):
        return a ** b

    def division_entera(a, b):
        return a // b

    def modular(a, b):
        return a % b


    def ejecutar_operacion(opcion, a, b):
        if opcion == "1":
            return sumar(a, b)
        
        elif opcion == "2":
            return restar(a, b)
        
        elif opcion == "3":
            return multiplicar(a, b)
        
        elif opcion == "4":
            if b == 0:
                print("❌ Error: No se puede dividir entre 0")
                return None
            return dividir(a, b)
        
        elif opcion == "5":
            return potenciar(a, b)
        
        elif opcion == "6":
            if b == 0:
                print("❌ Error: No se puede dividir entre 0")
                return None
            return division_entera(a, b)
        
        elif opcion == "7":
            if b == 0:
                print("❌ Error: No se puede hacer módulo con 0")
                return None
            return modular(a, b)
        
        else:
            print("❌ Opción inválida")
            return None


    resultado = ejecutar_operacion(opcion, a, b)

    if resultado is not None:
        print(f"Resultado: {resultado}")

    print("========================================")

    advice = input("¿Otra operación? si/no: ").lower()

    if advice == "no":
        print("¡Hasta luego! 👋")
        break   # 🔥 rompe el while y termina el programa
    elif advice != "si":
        print("Esa respuesta no es válida, cerrando programa...")
        break