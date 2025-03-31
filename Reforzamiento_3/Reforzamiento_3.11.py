"""Ingresar compañías relacionadas con al mundo de TI, copia los elementos
de la lista en otra lista pero estarán orden inverso, y muestra sus
elementos por la terminal y la lista original también."""

lista_TI=["CrowdStrike","Oracle","Atlassian","Microsoft","arm","HCL Software","IBM"]

lista_copia=lista_TI.copy()

lista_copia.reverse()


print("La lista orignal el: ",lista_TI)

print("La lista invertida es: ", lista_copia)