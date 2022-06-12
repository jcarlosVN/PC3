def num1(msg:str="ingrese un numero entero"):
    try:
        x = int(input(msg))
        return x
    except ValueError:
        print("no ingresaste correctamente el numero, vuelve a intentarlo")
        return num1()

def num2(msg:str="ingrese un numero entero"):
    try:
        y = int(input(msg))
        return y
    except ValueError:
        print("no ingresaste correctamente el numero, vuelve a intentarlo")
        return num2()

def calculo(x:int, y=int)->int:
    try:
        c= int(x/y*100)
        return c
    except ZeroDivisionError:
        print("Ha ocurrido un error, el denominador es 0, introduce bien el segundo número")

def main():
    x=num1("ingresa primer numero: ")
    y=num2("ingresa segundo numero: ")
    if x<0 or y<=0:
        print("ingresaste un valor no valido, vuelve a intentarlo")
        return main()
    c=calculo(x, y)
    if c>100:
        print("los valores ingresados no son validos")
        return main()
    elif c>99 and c<=100:
        print("el resultado es: F")
    elif c<1:
        print("el resultado es: E")
    else:
        print(f"el resultado es: {c}%")

main()