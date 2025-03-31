


num=54
num_ceros="{:05d}".format(num)
factura_canceladas={num_ceros:1200}


print("La lsita de facturas pagadas original es: ",factura_canceladas)

continuar=input("Desea ingresar otra factura si[s] no[n]:")

if continuar == "s":

    n_factura=int(input("Ingrese el número de la factura(##): "))
    valor_factura=input("Ingrese el precio: ")
    num_factura="{:05d}".format(n_factura)
    factura_canceladas[num_factura]=valor_factura

print("La factura final es: ",factura_canceladas)

comsulta=int(input("Ingrese el número de la factura: (##)"))

num_consulta="{:05d}".format(comsulta)

facturas_key=list(factura_canceladas.keys())

num_de_veces=facturas_key.count(num_consulta)

if num_de_veces == 0:
    print("El número de factura no existe")
else:
    print("La factura ya está cancelada")