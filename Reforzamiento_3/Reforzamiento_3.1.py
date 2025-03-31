"""Agregar 5 Objetos nuevos a tu lista (append) y quitar 2 elementos de esta
lista por valor. Mostrar la lista final en la terminal.
Obtén también la cantidad total ítems que tienes en tu lista ya creada para
agregar este valor a tu lista y mostrar también el resultado final de cantidad
total de elemento y la lista actualizada en consola. """


lista_a=[]

lista_a.append("Puno")
lista_a.append("Lima")
lista_a.append("Arequipa")
lista_a.append("Loreto")
lista_a.append("Tacna")

print("Lista departamentos:{}".format(lista_a))

lista_a.remove("Lima")
lista_a.remove("Loreto")
print("\n----------------------------------------")
print("Lista actualizada:{}".format(lista_a))
print("\n----------------------------------------")
cant_items=len(lista_a)
print("El tamaño de la lista es: ",cant_items)
print("\n----------------------------------------")
lista_a.append(cant_items)
print("Lista final {}".format(lista_a))
print("La cantidad de items final es: {}".format(len(lista_a)))
