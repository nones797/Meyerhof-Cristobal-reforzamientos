
lista=[]

numero =int(input("Ingrese el tamaño de la lista: "))

contador=0
"Usando iterativa"

while contador < numero:

    elemento=input("Ingrese el nombre de el alumno: ")

    lista.append(elemento)

    contador =contador +1

print("EL tamaño de lista es: ",len(lista))

print("Los nombres son: ",lista)