"""Crea una siguiente lista vacía y agregue ítems a partir de variables (los cuales
tendrán los siguientes tipos de datos: 3 floats, 3 ints y 3 strings) (append).
Sumar las dos listas creadas anteriormente y mostrar el resultado en consola. """



"""Listas anteriores"""

lista_a=[]

lista_a.append("Puno")
lista_a.append("Lima")
lista_a.append("Arequipa")
lista_a.append("Loreto")
lista_a.append("Tacna")

list_cursos=[]

list_cursos.append("Cálculo")
list_cursos.append("Física")
list_cursos.append("Dinámica")
list_cursos.append("Estática")
list_cursos.append("Dinámica")


"""Lista nueva"""
"""int"""
var_1=12
var_2=32
var_3=15
"""floats"""
var_4=12.3
var_5=12.7
var_6=17.2
"""strings"""
var_7="c++"
var_8="c#"
var_9="c"

list_3=[]

list_3.append(var_1)
list_3.append(var_2)
list_3.append(var_3)
list_3.append(var_4)
list_3.append(var_5)
list_3.append(var_6)
list_3.append(var_7)
list_3.append(var_8)
list_3.append(var_9)

print("La tercera lista es: ",list_3)

list_suma=list_3+list_cursos+lista_a

print("Suma de listas: ",list_suma)