"""Crear una lista (entre floats y bools, 6 elementos mínimo) donde imprimas el
penúltimo y antepenúltimo valor (por índice). Reconocer cada uno de los tipos
de datos en esta lista creada y mostrar los resultados en consola  """

"""Elimina ahora todos los elementos de la lista creada previamente y mostrar en 
consola la lista actualizada agregando tu nombre, apellido paterno, apellido 
materno y edad """

lista_5=[12.5,11.3,None,True,False,5.1]


print("El penultimo y antepenultimo items son: ", lista_5[4], "," ,lista_5[3])

item1= type(lista_5[0])
item2= type(lista_5[1])
item3= type(lista_5[2])
item4= type(lista_5[3])
item5= type(lista_5[4])
item6= type(lista_5[5])

print("Los tipos de la lista son respectivamente: ",item1,",",item2,",",item3,",", item4,",",item5,",",item6)

lista_5.clear()

lista_5.append("Meyerhof")
lista_5.append("Cristobal")
lista_5.append("Espinoza")
lista_5.append(22)
print("La lista actualizada es: ",lista_5)