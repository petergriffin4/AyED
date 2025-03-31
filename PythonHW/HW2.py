def calcular_factura():

    articulo = input("Ingrese el nombre del articulo: ")
    precio_unitario = float(input("Ingrese el precio por unidad del articulo: "))
    cantidad = int(input("Ingrese la cantidad de articulos: "))
    

    subtotal = precio_unitario * cantidad
    
    iva = subtotal * 0.15
    
    if subtotal > 1000:
        descuento = subtotal * 0.12
    else:
        descuento = 0
    
    total = subtotal + iva - descuento
    
    print("\nFactura de Compra:")
    print(f"Articulo: {articulo}")
    print(f"Precio Unitario: ${precio_unitario:.2f}")
    print(f"Cantidad: {cantidad}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"IVA (15%): ${iva:.2f}")
    if descuento > 0:
        print(f"Descuento (12%): -${descuento:.2f}")
    print(f"Total a Pagar: ${total:.2f}")

while True:
    calcular_factura()
    
    continuar = input("\n¿Desea realizar otra compra? (SI/NO): ").upper()
    if continuar != 'SI':
        print("Gracias por su compra. ¡Hasta luego!")
        break