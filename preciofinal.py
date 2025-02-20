print("Dinos los precios, ganacia e impuestos")

precio=input("Ingrese el precio: ")
precio=float(precio)

ganancia=input("Ingrese el precio: ")
ganancia=float(ganancia)

impuesto=input("Ingrese el precio: ")
impuesto=float(impuesto)

def calcularImpuesto(impuesto,precio):
    return impuesto*precio

def calcularGanancia(ganancia,precio):
    return ganancia*precio

def precioTotal(impuesto,precio,ganancia):
    precio1=calcularGanancia(ganancia,precio)+precio
    impuestoVenta=calcularImpuesto(impuesto,precio)
    return precio1+impuestoVenta

print(precioTotal(impuesto,precio,ganancia))