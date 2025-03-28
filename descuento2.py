#50 5
#100 10
#200 12
#100 20

compra = float(input("Ingrese el monto de compra: "))
unidades=int(input("Ingrese la cantidad de unidades: "))
validacionCompra=False
descuento=0
impuesto=0

if compra<0:
    print("El monto de la compra no puede ser negativo")

if unidades<=12: descuento=0
if unidades>=12: descuento=0.2

if compra>=10 and compra<50: impuesto=0.05
if compra>=50 and compra<100: impuesto=0.1
if compra>=100 and compra<200: impuesto=0.2
if compra>=200: impuesto=0.2

print("El impuesto a pagar es: $",compra*impuesto)
resultado=compra*impuesto
total=compra+resultado-(descuento*compra)
print(descuento*compra)
print("El total a pagar es $",total)

