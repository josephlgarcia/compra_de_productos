
###### MENSAJE DE BIENVENIDA ######


print("\nBienvenido a la tienda surtidora 'EL Manantial' \n")
print("En nuestra tienda encontrarás productos de la mejor calidad a los mejores precios \n")

###### ENTRADA DE DATOS ######


#Nombre del producto
producto = input("Ingrese el nombre del producto: ")
    

#Precio del producto: se utiliza un bucle para que el usuario ingrese un numero mayor a 0.
while True:
    try:
        precio_del_producto = float(input("Ingrese el precio del producto: "))
        if precio_del_producto <= 0:
            print("El precio debe ser mayor a 0")
        else:
            break #El bucle acaba cuando el usuario ingresa un numero mayor a 0.
    except ValueError: #si el usuario ingresa un valor que no es un numero, se imprime un mensaje de error.
        print("El precio debe ser un número mayor a 0")


#Se le solicita al usuario la cantidad de producto que desea, verificando que sea un número entero mayor a 0.
while True:
    try:
        cantidad_de_producto = int(input("Ingrese la candidad que desea: "))
        if cantidad_de_producto <= 0:
            print("La cantidad debe ser mayor a 0")
        else:
            break
    except ValueError:
        print("La cantidad debe ser un número entero mayor a 0")   


#Se le pregunta al usuario si el producto tiene descuento, verificando que la respuesta sea si o no.
while True:
        posible_descuento = input("¿El producto tiene descuento? (si/no): ").strip().lower()
        if posible_descuento != "si" and posible_descuento != "no":
            print("Ingrese 'si' o 'no'")
        else:    
            break


#Si el producto tiene descuento, se le solicita al usuario que ingrese el porcentaje de descuento, verificando que sea un número entre 0 y 100.
if posible_descuento == "si":
    while True:
        try:
            descuento = float(input("ingrese el descuento (0-100): "))
            if descuento < 0 or descuento > 100:
                print("El descuento debe ser entre 0 y 100")
            else:
                break
        except ValueError:
            print("El descuento debe ser un número entre 0 y 100")
else:
    descuento = 0 #Si el producto no tiene descuento, se le asigna el valor de 0.


#Cálculos necesarios para obtener el total de la compra y el total de la compra con descuento.
total_de_la_compra = precio_del_producto * cantidad_de_producto
total_de_la_compra_con_descuento = (total_de_la_compra) - ((total_de_la_compra * descuento)/100)


###### SALIDA DE DATOS ######
print(f"\nproducto: {producto} \nCantidad de {producto}: {cantidad_de_producto} \nValor total de la compra: {total_de_la_compra:.2f}")

if descuento > 0:
    print(f"Descuento: {descuento}%. Total de la compra con descuento aplicado: {total_de_la_compra_con_descuento:.2f}")
else:
    print("No hay descuento para esta compra")

print("\n¡Gracias por preferirnos en su compra! \n")