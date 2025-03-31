
dic_2={"Item1":"Loreto","Item2":"Puno","Item3":"Ucayali","Item4":"Lima","Item5":"Junin","Item6":"Ica"}

print("El diccionario es: ",dic_2)

del dic_2["Item2"]
dic_2["Item5"]="Pasco"

print("Diccionario actualizado: ",dic_2)

if "Item2" not in dic_2:
    print("Item2 eliminado")