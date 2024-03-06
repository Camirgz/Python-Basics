def total_productos() -> dict:
    dic_productos ={}
    producto = input("Ingrese le nombre de su producto")
    precio = int(input("Ingrese el costo de su producto"))
    dic_productos[f'{producto}'] = precio
    return dic_productos

def imprimir_productos(dic_productos) -> None:
    sum_total = 0
    print("- - - - - - - - - - - - - - - - - - - - - - - ")
    for clave, valor in dic_productos.keys():
        print(f"Nombre: {clave}, Precio: {valor}")
        sum_total += valor
    
    print(f"El precio total de los articulos es: {sum_total}")
