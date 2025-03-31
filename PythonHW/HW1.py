def calcular_importe(vehiculo, distancia_km=0, toneladas=0):
    if vehiculo == "bicicleta":
        return 100
    elif vehiculo == "moto" or vehiculo == "carro":
        return 30 * distancia_km
    elif vehiculo == "camion":
        return (30 * distancia_km) + (25 * toneladas)
    else:
        return "Tipo de vehículo no válido"
vehiculo = input("Ingrese el tipo de vehiculo (bicicleta, moto, carro, camion): ").strip().lower()
distancia_km = 0
toneladas = 0

if vehiculo in ["moto", "carro", "camion"]:
    distancia_km = float(input("Ingrese la distancia en Km: "))
    
if vehiculo == "camion":
    toneladas = float(input("Ingrese el peso en toneladas: "))

importe = calcular_importe(vehiculo, distancia_km, toneladas)
print(f"El importe a pagar es: {importe} cordobas")
