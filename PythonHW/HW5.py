import math

while True:
    print("\n===================================")
    print("CÁLCULO DE SUPERFICIES (versión 1.0)")
    print("===================================")
    print("1. Cuadrado       -> lado * lado")
    print("2. Círculo        -> pi * radio * radio")
    print("3. Rectángulo     -> base * altura")
    print("4. Trapecio       -> ((base1 + base2) * altura) / 2")
    print("5. Triángulo      -> (base * altura) / 2")
    print("===================================")

    opcion = int(input("Elige una opción (1-5) o 0 para salir: "))

    if opcion == 0:
        print("Saliendo del programa...")
        break
    elif opcion == 1:
        lado = float(input("Ingresa el lado del cuadrado: "))
        area = lado * lado
    elif opcion == 2:
        radio = float(input("Ingresa el radio del círculo: "))
        area = math.pi * radio * radio
    elif opcion == 3:
        base = float(input("Ingresa la base del rectángulo: "))
        altura = float(input("Ingresa la altura del rectángulo: "))
        area = base * altura
    elif opcion == 4:
        base1 = float(input("Ingresa la base menor del trapecio: "))
        base2 = float(input("Ingresa la base mayor del trapecio: "))
        altura = float(input("Ingresa la altura del trapecio: "))
        area = ((base1 + base2) * altura) / 2
    elif opcion == 5:
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        area = (base * altura) / 2
    else:
        print("Opción no válida. Intenta de nuevo.")
        continue

    print(f"El área calculada es: {area:.2f}")
