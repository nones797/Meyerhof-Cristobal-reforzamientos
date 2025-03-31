"""Devuelve la cantidad de veces que se repite un curso que hayas llevado en
pregrado (agregarlos previamente a la lista con un mínimo de 5 cursos) luego
mostrarla, finalmente elimina el segundo ítem de la lista usando debidamente
su índice y mostrar en consola tu lista actualizada """

list_cursos=[]

list_cursos.append("Cálculo")
list_cursos.append("Física")
list_cursos.append("Dinámica")
list_cursos.append("Estática")
list_cursos.append("Dinámica")


print("El curso dinámica se repite : {} veces".format(list_cursos.count("Dinámica")))

del list_cursos[1]

print("La nueva lista es: ", list_cursos)