#______________________________________________________________________
# 1- Pide un numero al usuario y muestra la cantidad de repeticiones

# num=int(input("ingrese  un numero"))
# for i in range(num):
#     print("Repetir",i+1)

#________________________________________________________________________
# 2-Pide un numero al usuario y muestra la tabla de ese numero hasta el 10

# num=int(input("ingrese  un numero"))
# for i in range(5):
#      print(num*(i+1))

#________________________________________________________________________
#3- For dentro de otro for

# for x in range(10):
#      for i in range (11):
#           print(x+1, "x", i+1, "=", (i+1)*(x+1))

#________________________________________________________________________
#4-Pedir al usuario la cantidad de notas ysacar promedio
 
# cant=int(input("ingrese la cantidad de notas "))
# suma=0
# for i in range(cant):
#     print("ingrese nota", i+1)
#     nota=float(input())
#     suma=suma+nota  #suma+=nota (es otra manera de hacerlo)
#     prom=suma/cant
#     print("el promedio es",prom)

#________________________________________________________________________
# 5-Pedir la cantidad de alumnos y luego la cantidad de notas x alumno
 
# cant=int(input("ingrese el numero de alumnos"))
# for x in range (cant):
#     print("ingresa el numero de notas del aumno", x+1)
#     suma=0
#     for i in range(cant):
#      print("ingrese nota", i+1,"del alumno",x+1,"usa decimales")
#      nota=float(input())
#      suma=suma+nota  #suma+=nota (es otra manera de hacerlo)
#      prom=suma/cant
#      print("el promedio es",prom)
#      if prom>=4:
#         print("Aprovaste")
#      else:
#         print("Reprobaste")

#________________________________________________________________________
# 6-Pedir al usuario un numero y suma todos los digitos,desde el 1 hasta ese numero ,mostrando la suma 

# cant=int(input("ingrese cantidad de numero"))

# for i in range(cant):
#     num=int(input("ingrese un numero"))

#     if num % 2==0:
#         print("el nunmero",num," es par")
#     else:
#         print("el numero",num, "es impar")

#___________________________________________________________________________
#7- Designar 2 cantidatos y de votantes  ,pedir voto a cada votante y mostar resultados y verificar quien gano

# c1="Inuy"                # se designa la cantidad de votantes en este caso 2 
# c2="kago"
# cv1=0
# cv2=0

# cant=int(input("Ingrese cantidad de votantes"))

# for i in range(cant):
#     print(f"por quien votara? 1-.{c1},2-.{c2}")
#     voto=int(input())
#     if voto==1:
#        cv1=cv1+1
#     else:
#         cv2=cv2+1

#     print(f"la cantidad e votos de {c1}es {cv1}")
#     print(f"la cantidad e votos de {c2}es {cv2}")

#     if cv1>cv2:
#         print(f"gano {c1}")
#     elif cv1<cv2:
#         print(f"gano {c2}")
#     else:
#         print("Es un empate")
#__________________________________________________________________________
#8-  Vocales

# frase=input("ingrese una frase")
# c=0
# cons=0
# v=0
# for i in frase:
#     if i.lower() in "a e i o u":   # Lower es una funcion convierte los carcteres de una cadena a minunusculasa
    
#         v=v=1 
#     else:
#      cons=cons+1
#      c=c=1
# print("la cantidad de vocales ", v)
# print("la cantidad de caracteres  es ", c)

#______________________________________________________________________________
# Otra manera de hacer el par e impar   

# num=int(input("Ingrese cantidaad de numeros "))

# for i in range(1,num+1)
#     if (i) %2==0:
#       print(f"el numero {i}es par")
#     else:
#       print(f" el numero{i} es impar")
#_______________________________________________________________________________
#Supermercado
# cant=int(input("Cuantos productos llevara?"))
# total=0
# for i in range(cant):
#     print('''
#           que producto llevara?
#           1- frac $600
#           2- Bon o bon $400
#           3-Ramitas $1000
#           ''')
#     op=int(input())
#     if op==1:
#         print("llevas frac")
#         total=total+600

#     elif op==2:
#         print("llevas Bon o bon")
#         total=total+400
#     elif op==3:
#          print("llevas ramitas")
#          total=total+1000

#     else:
#         print("escoga una opcion valida")     
#______________________________________________________________________________________
#otros ejercicios de for
#perros de caza
#pida al usuario la cantidad de perros
#muestre cual es la cuota minima de conejos
#luego consulte cuantos conejos trajo
#si el perro trajo la cantidad minima
#cumplio la cuota,sino se queda sin filete
#mostrar resumen de perro que cumplieron y los que no 

# import random


        
# cuotC=3
# cumple =0
# while True:
#     try:

#         cant=int(input("ingrese la cantidad de perritos"))
#         for i in range (cant):
#           cone=random.randint (0,4)
#           print(f"el perrito {i+1} trajo {cone} conejito")

#           if cone>=cuotC:
#              print("tienes filete perrito, buen chico c:")
#              cumple+=1
#           else:
#              print("Se queda sin filete, perdon perrito :c")

# #resumen de perro que cumplieron y los que no ///////////////////////

# #los que cumplieron 
#         print("los perritos que cumplieron la cuota son ", cumple)
# #los que no cumplieron
#         print(f"los perritos que no cumplieron la cuota :c  son {cant-cumple}")
#         break 

#     except:
#        print("ingrese solo nuneros enteros")



# try:
#     #codigo a aejecutar
#     print("Ejecuta algo")
# except Exception:
#     # mensaje de error
#     print("Error")



#___________________________________________________________
# PASAR EL RAMO                             #prueba uso de for,condicionantes,try ,except

#Pregunta la cantidad de rojos en el curso
#los talleres que hay en el semestre son 4
# por cada taller asisitido obtiene 0.3 decimas 
# Si el alumno  tiene mas de 1 punto obtiene la bendicion del profe,sino no se le puede ayudar
# ingrese la nota final y sume las decimas acumuladas
# muestre si aprueba o reprueba

# talleres=4
# asistido=0
# decimas=0
# rojos=float(input("ingrese la cantidad de rojos en el curso"))
 
# for roj in range(rojos):
#     for tall in range(tall):
#         asis=int(input(f"asistio al taller number {tall+1}? 1.- si/ No"))  #se le va sumando uno
#         if asis.lower()=="si":
#             decimas+=0.3

#             if decimas>=1:
#                 print("tienen la bencion del prof")
    
#     else:
#         print("nada mas que hacer")


#     notafinal=float(input("ingrese su nota final"))
#     notafinal+=decimas
#     print("su nota final es", notafinal) #
#     if notafinal>=4:
#         print("el alumno aprobo")
#     else:
#         ("el alumno reprobo")
#______________________________________________________________________________________________
#LAVADO DE AUTO

#Crear un menu para lavar autos


# 1.-Cursar pago del lavado
# 2.- ver ventas diarias
# 3.- Salir

#el lavado tiene 3 niveles:
#1.- Full $15.000 2.- standard 10.000. 3.- Basico $7.000
#al mostrar las ventas diarias,debe mostrar la cantidad de autos que han ingresado y el monto total
#recaudado.Tambien debe mostrar el monto mas alta pagado

# ventatotal=0
# nivel=0
# opc=0
# print(''' Niveles de lavado 
      
#     1- Basico $7000
#     2.-Standar $10.000
#     3.- Full $ 15.000    
#       ''')
    
# cant=int(input("ingrese una opcion"))

# if cant==1:
#     nivel+=7000
# elif cant==2:
#     nivel+=10000
# elif cant==3:
#     nivel+=15000
# else:
#     print("ingrese una opcion valida")

# print(''' Ingrese la operacion que desea realizar 
      
#       1.-Cursar pago del lavado
#       2.-Ver ventas diarias
#       3.-Salir
      
#       ''')
# op=int(input("ingrese una opcion"))

# if op==1:
#     opc=1
# elif op==2:
#     opc=2
# elif op==3:
#     opc=3
# else:
#     print("")
#  #calculos
#  # 
# ventatotal=

#_____________________________________________________________________________________

# El programa debe tener un menú de opciones de donde se pueda realizar el pago
# del cupo de la tarjeta de crédito, como también simular nuevas compras, y estas
# una vez sumadas se resten al cupo disponible.
# Las opciones disponibles deben estar construidas de la siguiente forma:

# 1. Pago de Tarjeta de Crédito:
# a. El usuario comienza con una deuda de $100.000
# b. El usuario puede ingresar un monto para realizar un pago en la
# tarjeta de crédito.
# c. Se debe verificar que el monto ingresado sea mayor o igual a cero.
# d. Se debe verificar que el monto a pagar no exceda el saldo actual de
# la tarjeta.
# e. Al pagar el sistema debe descontar de la deuda total
# f. Si las verificaciones son exitosas, se realiza el pago y se actualiza el
# saldo de la tarjeta.

# 2. Simulación de Compras:
# a. El usuario puede simular realizar un número ilimitado de compras.
# b. Para cada compra, se solicita al usuario ingresar el monto de la
# compra. El programa suma los montos de cada compra.
# c. Se verifica que el monto de la compra sea mayor o igual a cero.
# d. Se realiza la compra y se actualiza el saldo de la tarjeta para cada
# iteración del bucle for.

# 3. Salir:
# a. Al seleccionar esta opción, el programa debe cerrarse o finalizar.
# A considerar:
# 1. Manejo de Errores:
# a. Se utilizan bloques try y except para manejar posibles errores al
# ingresar datos, validar valores no numéricos y errores inesperados.

# pago=0
# deuda=100000
# print('''Seleccione una opcion
      
#       1.-Pago de tarjeta de credito
#       2.-Simulacion de compra
#       3.-Salir

#       ''')
# print(f"la deuda inicial es {deuda}")
# op=int(input("que desea hacer?"))

# # if op==1:
# #     print("desea pagar")
# # elif op==2:
# #     print("simular una compra")
# # elif op==3:
# #     print("salir")

# pago=int(input("cuanto desea pagar?"))
# if pago>= 0 and pago<=deuda:
#     deuda-=pago
# print(f"el monto a pagar no debe exceder el saldo actual: {deuda}")
# # la tarjeta.")

# print("el saldo actual es ", deuda)

# sim=int(input())

#_____________________________________________________________________________________

# ETAPAS:
# Debe crear un menú de inicio de sesión, en el cual se debe mostrar los siguientes campos:
# 1) iniciar sesión
# 2) registrar usuario
# 3) salir
# Para lo cual usted deberá haber creado 3 variables de usuario y 3 variables de contraseña,
# ambas con valor inicial vacío, ejemplo:
# • usuario1= None
# • usuario2=None
# • usuario3=None
# • contrasena1= None
# • contrasena2=None
# • contrasena3= None

# Si se selecciona la opción 1 y no existen registros de usuarios, el sistema deberá indicar que
# es necesario registrar un usuario antes, y volverá al menú principal, en el caso de que
# ingrese el usuario y contraseña correctamente, entonces el sistema mostrará el siguiente
# menú:
# 1) Realizar llamada
# 2) Enviar correo electrónico
# 3) Cerrar sesión
# 2
# Donde la opción 1 debe solicitar un número de celular, éste deberá comenzar con 9 y su
# tamaño es de 9 dígitos (ejemplo: 985447561).
# La opción 2, solicita un correo electrónico, el cual debe tener por lo menos un carácter de
# “@” (validar usando for y while) y lo guardará en una variable llamada “correo”.
# También solicitará el mensaje a enviar y lo guardará en una variable llamada “mensaje”
# Finalmente cerrar sesión, volverá al menú principal.
# El sistema no acepta que se ingresen opciones distintas a 1, 2 y 3 en ambos menús, si ocurre
# esto, entonces el sistema emite un error y vuelve a solicitar la opción.
# Recuerde utilizar try Exception en caso de ser necesario.

#variables de usuarios
usuario1= None
usuario2=None 
usuario3=None
#variables de contraseñas 
contrasena1= None
contrasena2=None
contrasena3= None

while True:
   
 op=int(input(''' ingrese una opcion :)
              
 1. iniciar sesión
 2.-registrar usuario
 3.- salir
'''))
 
 match op:
  
  case 1:

    if usuario1==None and usuario2==None and usuario3==None:
      print("No hay registros")

    print("Es necesario registrarse antes de continuar...")
    user=int(input("ingrese un usuario"))
    print("Debe indicar una contraseña con un minumo de 6 digitos ")
    cont=int(input("ingrese una contraseña"))
    #  print("su contraseña es correcta")

    # elif cont != contrasena1:
    #  print("contrseña incorrecta, intentelo nuevamente")

    #  menú:
#  1) Realizar llamada
#  2) Enviar correo electrónico
#  3) Cerrar sesión



   
   









