"""Crea dos listas (una de datos string y la otra de datos numéricos) para luego
usar los métodos de orden (los elementos tienen que estar desordenados),
mostrar las listas antes y después de aplicarle los métodos de orden"""

lista_num=[4.3,3,9,3,6,4,1,23,64,74]
lista_datos=["Toyota","Audi","Mercedes Benz","BMW","Lotus","Infinity","Honda"]

print("Lista numerica antes: ",lista_num)
print("Lista de dartos antes: ",lista_datos)

print("---------------------")

lista_num.sort()

lista_datos.sort()

print("Lista numerica ordenada: ",lista_num)

print("Lista de datos ordenada: ",lista_datos)