edad=int(input("Ingresa tu edad: "))

if edad<0:
    while edad<0:
        edad=int(input("Error, la edad no puede ser menor a 0, ingresa tu edad: "))

if edad>=18:
    print(f"Tienes {edad}, eres mayor de edad")
else:
    print(f"Tienes {edad}, no eres mayor de edad")