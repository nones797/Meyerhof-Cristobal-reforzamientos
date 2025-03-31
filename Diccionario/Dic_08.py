
agenda={}

cantidad=int(input("Ingrese la cantidad de personas: "))

contador=0

while contador < cantidad:

    nombre = input("Ingrese el nombre: ")
    numero= input("Ingrese el número: ")

    agenda[nombre]=numero

    contador=contador+1

nombres=list(agenda.keys())
print("------------------------------------------------")
nomb=input("Ingrese el nombre que busca: ")

veces = nombres.count(nomb)
if veces == 0:
    print("No se encuentra registrado en la agenda")
