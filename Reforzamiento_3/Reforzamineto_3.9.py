"""Crear un programa en Python donde tendrás una lista con 5
departamentos, ingresarás 2 departamentos adicionales por posición, el
cual el segundo departamento estará en la posición ‘1’ y el primero en
penúltimo lugar, finalmente mostrar la lista original y la lista actualizada
en terminal"""

lista_depart=["Lima","Junin","Pasco","Puno","Ica"]
print("Lista Original")
lista_depart.insert(4,"Arequipa")
lista_depart.insert(0,"Loreto")

print("Lista modificada ", lista_depart)