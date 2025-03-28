import random

intentos=5
numero=random.randint(1,50)

digitado=input("Ingresa un número entero entre 1 y 50 o salir para terminar el programa: ")

while intentos>0 and digitado.lower()!="salir":

    if not digitado.isnumeric():
        print("\nError, solo puedes ingresar números enteros")
    else:

        digitado=int(digitado)

        if digitado<1 or digitado>50:
            print("Error, el número debe estar entre 1 y 50")
        else: 
        
            if digitado<numero:
                print("\nEl número secreto es mayor")

            elif digitado>numero:
                print("\nEl número secreto es menor")

            else:
                print(f"\nGanaste, el número secreto era: {numero}")
                break
            intentos-=1
            print(f"Te quedan {intentos} intentos")
        
    if intentos>0:
        digitado=input("Ingresa un número entero entre 1 y 50 o salir para terminar el programa: ")
    
if intentos==0:
    print(f"Perdiste, el número era: {numero}")

elif digitado.lower()=="salir":
    print("Saliste del programa")