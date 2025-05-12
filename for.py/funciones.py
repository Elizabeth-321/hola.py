def suma():             #funcion
    n1=int(input("ingrese un numero"))
    n2=int(input("ingrese un numero"))
    print("la suma es", n1, n2)

def resta():             #funcion
    n1=int(input("ingrese un numero"))
    n2=int(input("ingrese un numero"))
    print("la resta es", n1, n2)
def multiplicacion():             #funcion
    n1=int(input("ingrese un numero"))
    n2=int(input("ingrese un numero"))
    print("la multiplicacion es", n1, n2)
def division():             #funcion
    n1=int(input("ingrese un numero"))
    n2=int(input("ingrese un numero"))
    print("la division es", n1, n2)


    try:
        resultado=n1/n2
        print("la division es", resultado)
    except ZeroDivisionError:
        print("la division por cero no esta permitida")

def calcu():  
    while True:
      op=int(input('''seleccione una opcion
                 1.- suma
                 2.- Resta
                 3.- multiplicacion
                 4.- division
                 5.- salir 
                     '''))
match op: #estructura de control que permite comparar un valor con múltiples patrones y ejecutar un bloque de código específico basado en la coincidencia
        case 1:
          print("Suma")
          suma()
     
        case 2:
          print("Resta")
          resta()
        case 3:
          print("Multiplicacion")
          multiplicacion()
        case 4:
          print("Division")
          division()
          break
    


    #realizar programa que incluya match y llame a otras 3 funciones estas funciones deben incluir
    #if ,if else for y/0 while el programa debe ser recursivo
       
       
