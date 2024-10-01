from tienda import Restaurante, Supermercado, Farmacia

def main():
    print("Bienvenido al sistema de gestión de tiendas")
    nombre_tienda = input("Ingrese el nombre de la tienda: ")
    costo_delivery = float(input("Ingrese el costo de delivery de la tienda: "))
    tipo_tienda = input("Ingrese el tipo de tienda (Restaurante, Supermercado, Farmacia): ")

    if tipo_tienda.lower() == "restaurante":
        tienda = Restaurante(nombre_tienda, costo_delivery)
    elif tipo_tienda.lower() == "supermercado":
        tienda = Supermercado(nombre_tienda, costo_delivery)
    elif tipo_tienda.lower() == "farmacia":
        tienda = Farmacia(nombre_tienda, costo_delivery)
    else:
        print("Tipo de tienda no válido.")
        return

    while True:
        print("\nOpciones:")
        print("1. Ingresar producto")
        print("2. Listar productos")
        print("3. Realizar venta")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_producto = input("Ingrese el nombre del producto: ")
            precio_producto = float(input("Ingrese el precio del producto: "))
            stock_producto = int(input("Ingrese el stock del producto (opcional, presione Enter para 0): ") or 0)
            tienda.ingresar_producto(nombre_producto, precio_producto, stock_producto)

        elif opcion == "2":
            print(tienda.listar_productos())

        elif opcion == "3":
            nombre_producto = input("Ingrese el nombre del producto a vender: ")
            cantidad_producto = int(input("Ingrese la cantidad a vender: "))
            tienda.realizar_venta(nombre_producto, cantidad_producto)

        elif opcion == "4":
            print("Gracias por usar el sistema. ¡Adiós!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
