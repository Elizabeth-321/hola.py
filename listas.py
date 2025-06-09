#uso ejemplo listas
#######################################################
# lista=[2,2,4,1,5]
# print(lista)

         #-5-4-3-2-1
# numeros=[2,3,4,5,6]   #Se debe poner corchete para ver el numero comienza en 0 ej: 2:0 3:1 4:2  5:3 como en este caso 6:4
#         #0,1,2,3,4

# print(numeros[3])
         #-5-4-3-2-1
# numeros=[2,3,4,5,6]   #Se debe poner corchete para ver el numero comienza en 0 ej: 2:0 3:1 4:2  5:3 
# #         #0,1,2,3,4
# # print(numeros[-3])
# for numero in numeros :
#     print("numero",numero*2)

# nombres=["eli", "ale", "ana","victor"]
# print(nombres[-2]) # si pones 2 igual sale lo mismo
#######################################################
#funciones para listas
#append   #append siempre agrega un elemnt0 al final de la lista

# nombres=["eli", "ale", "ana","victor"]
# print(nombres)
# nombres.append("eli")   #append siempre agrega un elemnt0 al final de la lista
# print(nombres)

#////////////////////////////////////////////////////////////
#hacer un programa donde se deba ingresar un nombre y mostrar nombre (en menu)debe ser la misma cantidad de nombre y apellidos
#print nombres
# n=["eli","ale", "ana"]
# a=["lagos", "pino","teran"]

# c=0  #contador
# for i in a:
#   print(n[c], a[c])

# name=[] 
# ape=[]
# while True:
#     print('''

#     1.-Ingresar nombre
#     2.-Mostrar nombre y apellido
#     3.-salir
#             ''')
    
#     op=int(input())
#     match op:
#         case 1:
#             nombres=input("ingrese su name")
#             name.append(nombres)
#             apellido=input("ingrese su apellido")
#             ape.append(apellido)

#         case 2 :
#             c=0
#             for i in name:
#                 print(name[c], ape[c])
#                 c+=1
#         case 3: 
#             print("saliendo")
#             break
#         case _:
#             print("invalido")
        

#///////////////////////////////////////////////////////
# n=["eli","ale", "ana"]
# a=["lagos", "pino","teran"]

# c=0  #contador
# for i in a:
#   print(n[c], a[c])

# name=[] 
# ape=[]
# while True:
#     print('''

#     1.-Ingresar nombre
#     2.-Mostrar nombre y apellido
#     3.-Buscar name
#     4.-salir
#             ''')
    
#     op=int(input())
#     match op:
#         case 1:
#             nombres=input("ingrese su name")
#             name.append(nombres)
#             apellido=input("ingrese su apellido")
#             ape.append(apellido)

#         case 2 :
#             c=0
#             for i in name:
#                 print(name[c], ape[c])
#                 c+=1
#         case 3: 
#             busca=int(input("ingrese el name que buscara"))
#             if busca in nombres:
#                 print(f"el nombre {busca} esta en la lista ")
#                 print(f"el nombre {busca}no esta en la lista")
#         case 4:
#             print("saliendo")
#             break
#         case _:
#             print("invalido")
#///////////////////////////////////////////////////////////////////
#selecciona una opcin
#agregar productos (nombre producto y precio)
#comprar (submenu mostrando productos y precios)
#crear boleta
#salir


while True:
    op=int(input('''
            
        1.- Agregar productos(nombre producto y precio)
        2.-comprar (submenu mostrando productos y precios)
        3.- Crear boleta
        4.- Salir
                 
            '''))
        
    match op:
         case 1:
            while True:
                op=int(input('''
                    1.- chessecake $1500
                    2.- Tiramisu $2000
                    3.- kuchen $2500
                       '''))
                
                match op :
                    cas2 







