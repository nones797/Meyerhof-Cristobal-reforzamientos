""" Tienes una lista con 7 diferentes nombres de BD relacionales. De la cual 3
BDs estarán repetidas adrede (en posiciones no consecutivas), sacar la
base de datos repetidas uno por valor y le otro por índice.
Finalmente mostrar la lista actualizada en consola. """


lista_BDs=["Oracle DBMS","SQLite","IBM DB2","SQLite","MongoDB","Oracle DBMS","IBM DB2"]
print("Lista original: ",lista_BDs)
lista_BDs.remove("Oracle DBMS")
del lista_BDs[5]

print("La lista actualizada es: ",lista_BDs)
