
list3=["Pepe","Juan","Ana","Hugo","Cesar"]
print("La lista original es: ",list3)

item=input("Ingrese un nombre: ")

if item == "Pepe":

    list3.remove("Pepe")
else:
    if item == "Juan":
        list3.remove("Juan")
    else:
        if item == "Ana":
            list3.remove("Ana")
        else:
            if item == "Hugo":
                list3.remove("Hugo")
            else:
                if item == "Cesar":
                    list3.remove("Cesar")
                else:
                    list3.append(item)



print("La lista final es: ",list3)