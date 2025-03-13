# if una opción
# condición true o false

#Número es par, impar, negativo o positivo

respuesta=int(input("Ingresa el número: "))

if respuesta %2==0:
    print("Es par")
else:
    print("Es impar")

if respuesta<0:
    print("Es negativo")
elif respuesta>0:
    print("Es positivo")
else:
    print("Es 0")

print("_________________________________________________")

respuesta1="Es par" if respuesta %2==0 else "Es impar"
respuesta2="Es negativo" if respuesta<0 else "Es positivo"

print(f"{respuesta1},{respuesta2}")

#Definir el número par
#def nombre()

def modulo(valor):
    valor=True if respuesta %2==0 else False
    print(valor)
    return valor

#Las funciones son estrucutras de código que se ejecutan cuando son llamadas nombre()
#funcion si es positivo

def signo(valor):
    valor=False if respuesta <0 else True
    print(valor)
    return valor

def detectarLetras(valor):
    if any(c.isalpha() for c in str(valor)):
        print(True)
        return True
    else:
        print(False)
        return False

#any() es una funcion de python
#si hay un elemento que sea true devuelve true, sino false
#for c es una variable temporal, dará las vueltas necesarias para terminar el número según sus caracteres

def ejercutar():
    pedirValor=int(input("Ingrese el número: "))
    if pedirValor==True:
        ejercutar()
    else:
        #valor=True if respuesta <0 else False
        Mrespuesta=modulo(pedirValor)
        #valor=True if respuesta %2==0 else False
        Srespuesta=signo(pedirValor)
        
        if Mrespuesta and Srespuesta==True:
            print("Positivo y par")
        elif Mrespuesta or Srespuesta==False:
            print("Negativo e impar")

ejercutar()