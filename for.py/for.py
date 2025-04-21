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
#7- Designar 2 votantes y pedir cantidad de votantes  ,pedir voto a cada votante y mostar resultados y verificar quien gano

cant=int(input("Ingrese cantidad de votantes"))
for i in range(cant):
