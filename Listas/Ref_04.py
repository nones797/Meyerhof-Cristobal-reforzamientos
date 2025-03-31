
"Oracle, Atlassian, Cisco, IBM, Salesforce "
lista_4=[]

cant_1=int(input("Ingrese el tamaño de la lista: "))

cont=0


while cont < cant_1:
    item=input("Ingrese el nombre de la compañia: ")
    lista_4.append(item)
    cont = cont+1



CopiaLista=lista_4.copy()

print("---------------------------------------")


item_01=input("Ingrese el nombre de una compañia: ")
item_02=input("Ingrese otra compañia: ")

CopiaLista.remove(item_01)
CopiaLista.remove(item_02)


print("---------------------------")
print("La lista es: ",lista_4)
print("La lista final es: ",CopiaLista)



