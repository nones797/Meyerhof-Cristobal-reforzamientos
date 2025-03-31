"""Crea una lista vacía, luego ingresa sus valores (10 valores numéricos) y
finalmente muestra la suma y la media de los números ingresado insertados en
la terminal"""


var_1=[]

var_1.append(12.1)
var_1.append(17.2)
var_1.append(18)
var_1.append(13)
var_1.append(11)
var_1.append(16)
var_1.append(15.1)
var_1.append(17.2)
var_1.append(12)
var_1.append(17.8)

suma_lista=sum(var_1)
cant_items=len(var_1)

print("La suma de los elementos es: ",suma_lista)
print("La media de los números es: ",suma_lista/cant_items)