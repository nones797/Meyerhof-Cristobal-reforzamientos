dic={}
cant=int(input("Ingrese la cantidad de alumnos: "))
contador=0
while contador<cant:
    nombre=input("Ingrese el nómbre del alumno: ")
    nota=float(input("Ingrese la nota: "))
    dic[nombre]=nota

    contador =contador + 1

print("Diccionario: ",dic)

clave=list(dic.keys())
valor=list(dic.values())
num=cant
cont2=0
while cont2 < num:
    print(f"{clave[cont2]} tiene la nota de {valor[cont2]}")
    cont2=cont2+1
promedio= sum(valor) / len(valor)
print("El promedio es: ",promedio)
