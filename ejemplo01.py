# voy a comprar pan 
presupuesto = 1
valorPan = 0.5 
valorCafe = 0.5
#> es unicamente mayors al numero sin incluir el numero de inicio 
#>= si se incluye el valor del elemento.
if presupuesto >= valorPan + valorCafe:
    print("Pansito con cafe")

if  presupuesto < valorPan:
    print("No me alcanza para el pan")

valorNaranja = valorCafe +1

if valorCafe == valorNaranja:
    print("Igual")

else:
    print("El valor es diferente")

if not False :
    print("Solo saldre si es verdad")


v1 = (4+7) > 15+4+5/2  #parentesis 
                            # /
                            #suma 
                            # >
print("Respuesta " , v1)

v2 = (1+2 +1 **2)/10 <= 42 *7  # lo que esta dentro de los parentesis
                               # potencia 
                               # *
                               #  /
print("Respuesta " , v2)

#(7 == 7) || (2 > 5)

v4 = (7==7) or 2 >5                  
print('v4 = (7==7) or 2 > 5 ', v4)

#or 
# v + f = v
# 1 true
# 0 false 
# 1 + 0  = 1

#!(4 <= 4) && (6 != 3)
v5 = not 4 <= 4 and 6 !=3
print("v5 = not 4 <= 4 and  6 ==3  ", v5)

#and *
# 1 
# 0 
# 1 * 0 = 0
# 1  * 1 = 1
