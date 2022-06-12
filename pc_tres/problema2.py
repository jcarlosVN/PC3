lista = list()
def calificaciones(msg:str="ingrese calificacion o digite salir para terminar: "):
    try:
        x = input(msg).lower()
        if x == "salir":
            print(f"su lista de notas es: {lista}")
            print("gracias")
        elif int(x) >= 0 and int(x) <= 20:
            lista.append(x)
            return calificaciones()
        elif int(x) < 0 or int(x) > 20:
            print("la nota no esta en el rango de 0 a 20, vuelva a intentarlo")
            return calificaciones()            
    except ValueError:
        print("no ingresaste correctamente el numero, vuelve a intentarlo")
        return calificaciones()