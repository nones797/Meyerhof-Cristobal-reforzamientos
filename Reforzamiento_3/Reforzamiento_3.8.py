"""Escribir un programa donde ingresará 8 nombres de países. Se quiere
hacer un clon de la lista, esta copia se le eliminará el primer y penúltimo
valor, mostrar finalmente el tamaño de la lista modificada, la lista original
y todos sus elementos de la lista modificada. """


lista_paises=["Rusia","EEUU","China","Alemania","Nigeria","Monaco","Austria","Bulgaria"]

lista_copia=lista_paises.copy()



del lista_copia[0]
del lista_copia[5]

print("Lista original: ",lista_paises)
print("Lista resultante: ",lista_copia)