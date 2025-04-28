#Uso While
# clave=123
# intentos=0
# password=int(input("ingrese su clave"))

# while clave!=password and intentos<=3:
#     print("erroor ingrese una clave valida")
#     intentos=intentos+1
#     password=int(input("ingrese la pass"))

#______________________________________________________________
# suma = 0
# while True:                                                                      #arreglar porque no muestra el total
#     num=int(input("ingrese un numero, cero para salir:"))
#     if num==0:
#      suma +=num
#     print(suma)
#     print(f"la suma total es{suma}")

# #____________________________________________________________

# #Pida al usuario el limmite inferior y superior de un rango
# genere un numero al azar dentro de ese rango # usar random para generar un numero al azar
# el segundo numero,no debe ser menor que el primeropero debe darle
# la oportunidad al usuario de  ingresar otro

# import random

# print("ingrese 2 numeros")
# n1 =int(input("ingrese el primer numero"))

# n2 =int(input("ingrese otro numero mayor que el anterior"))

# while n2<=n1: 
#     print("El numero debe ser mayor que el anterior")
#     n2=int(input("ingrese otro numero mayor que el anterior"))
# numran=random.randint(n1,n2)

# print(numran)

#_____________________________________________________________  #!!!!!!!usar random,condicional while ////prueba

#adivina el numero entre el 1 y 50

# import random                               #verificar

# numran=random.randint(1,50)
# print("adivine el numero entre 1 y 50")
# num=int(input())
# while numran!=num: #!= distinto de/  igual a ==/ mayor a >/menor a </mayor o igual >= /menor o igual a <=/ -= quitarle 
#      if num>numran:
#           print("el numero a adivinar es menor")
#      else:
#         print("el numero a adivinar es mayor")

# print("adivinaste el numero")

#_________________________________________________________________
#adivina el numero entre el 1 y 50 y ponere cantidad de intentos

import random                              

# numran=random.randint(1,50)
# print("adivine el numero entre 1 y 50")          #ARREFLAR!!
# num=int(input())
# while numran!=num: #!= distinto de/  igual a ==/ mayor a >/menor a </mayor o igual >= /menor o igual a <=/ -= quitarle 
#      intentos -=1
#      if intentos==0:
#           break
#     if  num>numran
#           print("el numero a adivinar es menor")
#      else:
#         print("el numero a adivinar es mayor")
#         print(f"")
#   if intentos==0 

#  else:
#       print("adivinaste el numero")


#____________________________________________________________________
#designar 2 peleadores solicitando sus nombres
# caada eleador tiene 50 hp,debe mostrar la barra de energia ,las peleas son por turnos
# cad turno el peleador ataca 3 y 15
# existe posibilidad de ataque critico del 20% sera ataque doble
# gana el que le quita todo el hp al rival


# print("ingrese lso nombres de los peleadores")
# p1=input("peleador 1")
# p2= input ("peleador 2")
# hp1= 50
# hp2 = 50
# turno=random.randint (1,2)

# while hp1>0 and hp2>0:

#     if turno % 2==0:
#         print("turno de " , p1)
#         ataq=random.randint(3,15)
#         critical=random.randint(1,5)
#         if critical==3:
#             ataq*2
#             print("ATAQYE CRITICO")
#         hp2-= ataq
#         timee.sleep(1)
#         print(f"vida de{p2}")
#         print("/"*hp2)

# else: 
#         print("turno de " , p2)
#         ataq=random.randint(3,15)
#         critical=random.randint(1,5)
#         if critical==3:
#             ataq*2
#             print("ataque critico")
#         hp2-= ataq
#         time.sleep(1)
#         print(f"vida de{p1}")
#         print("/"*hp1)
#         turno+=1

#         if hp1>hp2:
#              print(f"ha ganado el {p1}")

#         else: 
#              print(f"ha ganado el {p2}")

#_______________________________________________________
# Crear un cajero automatico :
# tener en cuenta cajas de billetes de 5000,10000 y 20000
# cada caja tiene 30 billetes,verificar si el monto solicitado esta disponible en el cajero
# Verificar si el monto solicitado es posible por el multiplo de los billetes disponibles
# al termianr cada transaccion,debe mostrar saldo disponible
# debe haber 3 usuarios cada uno con su saldo correspondiente,usar clave secreta para iniciar y segun la clave
# asociar el saldo disponible 

